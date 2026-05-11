"""STU v0.1 Phase 1 — Tokenizer Ratio Matrix.

Computes chars/token and bytes/token for all active TokSpecs across 12 languages.

Output: output/tokenizer_ratio_matrix_v0.1.parquet
Schema: vendor, tokenizer, source, repo, revision, status, lang, n,
        mean_chars_per_token, var_chars_per_token,
        mean_bytes_per_token, var_bytes_per_token,
        median_chars_per_token, p10_chars_per_token, p90_chars_per_token

USAGE:
    cd stu/
    python -m stu_matrix.run_phase1 --samples-dir samples/ --output output/

Uses `tokenizers` (Rust-backed HF library) directly to sidestep transformers
metadata bug on Python 3.13.x.
"""
from __future__ import annotations
import argparse
import gc
import hashlib
import json
import unicodedata
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pandas as pd
import tiktoken
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

from .specs import all_active, TokSpec


def normalize_text(s: str) -> str:
    """NFC normalization, BOM strip, newline canonicalization."""
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = s.removeprefix("﻿")
    return unicodedata.normalize("NFC", s)


def load_hf_tokenizer(spec: TokSpec) -> Tokenizer:
    """Load via direct tokenizer.json download, bypassing transformers.

    For vendors that ship a `tokenizer.json` in their HF repo (most modern
    tokenizers do), this works without needing `transformers` or
    `trust_remote_code=True`.
    """
    tokenizer_path = hf_hub_download(
        repo_id=spec.repo_or_encoding,
        filename="tokenizer.json",
        revision=spec.revision,
    )
    return Tokenizer.from_file(tokenizer_path)


def count_tokens_hf(tok: Tokenizer, texts: list[str]) -> list[int]:
    encoded = tok.encode_batch(texts, add_special_tokens=False)
    return [len(e.ids) for e in encoded]


def count_tokens_tiktoken(encoding_name: str, texts: list[str]) -> list[int]:
    enc = tiktoken.get_encoding(encoding_name)
    return [len(enc.encode(t)) for t in texts]


def summarize(spec: TokSpec, lang: str, texts: list[str]) -> dict:
    texts = [normalize_text(t) for t in texts if t.strip()]
    if not texts:
        return {"vendor": spec.vendor, "tokenizer": spec.name, "lang": lang, "n": 0}

    try:
        if spec.kind == "tokenizers_hf":
            tok = load_hf_tokenizer(spec)
            counts = count_tokens_hf(tok, texts)
            del tok
            gc.collect()
        elif spec.kind == "tiktoken":
            counts = count_tokens_tiktoken(spec.repo_or_encoding, texts)
        else:
            raise ValueError(f"Unknown kind: {spec.kind}")
    except Exception as e:
        return {
            "vendor": spec.vendor,
            "tokenizer": spec.name,
            "lang": lang,
            "n": 0,
            "error": str(e)[:200],
        }

    chars = np.array([len(t) for t in texts], dtype=float)
    bytes_ = np.array([len(t.encode("utf-8")) for t in texts], dtype=float)
    toks = np.array(counts, dtype=float)
    valid = toks > 0

    chars_per_token = chars[valid] / toks[valid]
    bytes_per_token = bytes_[valid] / toks[valid]

    return {
        "vendor": spec.vendor,
        "tokenizer": spec.name,
        "source": spec.kind,
        "repo_or_encoding": spec.repo_or_encoding,
        "revision": spec.revision,
        "status": spec.status,
        "lang": lang,
        "n": int(valid.sum()),
        "mean_chars_per_token": float(np.mean(chars_per_token)),
        "var_chars_per_token": float(np.var(chars_per_token, ddof=1)) if len(chars_per_token) > 1 else 0.0,
        "median_chars_per_token": float(np.median(chars_per_token)),
        "p10_chars_per_token": float(np.percentile(chars_per_token, 10)),
        "p90_chars_per_token": float(np.percentile(chars_per_token, 90)),
        "mean_bytes_per_token": float(np.mean(bytes_per_token)),
        "var_bytes_per_token": float(np.var(bytes_per_token, ddof=1)) if len(bytes_per_token) > 1 else 0.0,
        "attribution_caveat": spec.attribution_caveat,
    }


def load_samples(samples_dir: Path) -> dict[str, list[str]]:
    """Load samples; expect samples/<lang>.txt format, one sample per line."""
    data: dict[str, list[str]] = {}
    if not samples_dir.exists():
        return data
    for p in samples_dir.glob("*.txt"):
        lines = p.read_text(encoding="utf-8").splitlines()
        lines = [ln for ln in lines if ln.strip()][:200]  # cap at N=200 per cell
        data[p.stem] = lines
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples-dir", default="samples")
    ap.add_argument("--output", default="output")
    args = ap.parse_args()

    samples_dir = Path(args.samples_dir)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    samples_by_lang = load_samples(samples_dir)
    if not samples_by_lang:
        print(f"No samples found in {samples_dir}/. Run fetch_samples.py first.")
        return

    print(f"Loaded {len(samples_by_lang)} languages: {list(samples_by_lang.keys())}")

    rows = []
    for spec in all_active():
        print(f"Processing {spec.vendor:<22s} {spec.name} ({spec.status})")
        for lang, texts in samples_by_lang.items():
            row = summarize(spec, lang, texts)
            if "error" in row:
                print(f"    {lang}: ERROR {row['error'][:80]}")
            else:
                print(f"    {lang}: n={row['n']:>4d}  c/t={row['mean_chars_per_token']:.2f}  b/t={row['mean_bytes_per_token']:.2f}")
            rows.append(row)

    df = pd.DataFrame(rows)
    out_parquet = out_dir / "tokenizer_ratio_matrix_v0.1.parquet"
    df.to_parquet(out_parquet, index=False)
    print(f"\nWrote {out_parquet}")
    print(f"Rows: {len(df)}; vendors: {df['vendor'].nunique()}; langs: {df['lang'].nunique()}")


if __name__ == "__main__":
    main()
