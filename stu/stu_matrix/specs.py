"""Tokenizer specifications for STU v0.1 calibration matrix.

Each TokSpec declares:
- vendor: human-readable vendor name
- name: tokenizer identifier
- kind: "tokenizers_hf" | "tiktoken"
- repo_or_encoding: HF repo or tiktoken encoding name
- revision: HF commit SHA (set at run time; here use 'main' for development)
- status: "verified" | "surrogate" | "third_party_unverified" | "excluded"
- attribution_caveat: short caveat string for dataset card

Status meanings:
- verified: HF repo is the production tokenizer (e.g., Mistral, Llama)
- surrogate: HF repo is a proxy for production (e.g., Doubao -> Seed-OSS)
- third_party_unverified: HF repo is community-maintained, not official (e.g., some Kimi mirrors)
- excluded: identified as too narrow / specialized to represent production (e.g., Spark)
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal


@dataclass(frozen=True)
class TokSpec:
    vendor: str
    name: str
    kind: Literal["tokenizers_hf", "tiktoken"]
    repo_or_encoding: str
    revision: str = "main"
    status: Literal["verified", "surrogate", "third_party_unverified", "excluded"] = "verified"
    attribution_caveat: str = ""
    expected_chars_per_token: tuple[float, float] = (0.5, 6.0)  # sanity range (en, NFC)


# ============================================================================
# VERIFIED (12) — HF repo IS or contains the production tokenizer
# ============================================================================

VERIFIED = [
    TokSpec(
        vendor="OpenAI",
        name="o200k_base",
        kind="tiktoken",
        repo_or_encoding="o200k_base",
        status="verified",
        attribution_caveat="GPT-4o family. Does not include hidden reasoning tokens from o-series.",
    ),
    TokSpec(
        vendor="OpenAI",
        name="cl100k_base",
        kind="tiktoken",
        repo_or_encoding="cl100k_base",
        status="verified",
        attribution_caveat="GPT-3.5 / GPT-4 family pre-2024.",
    ),
    TokSpec(
        vendor="Qwen",
        name="qwen2.5",
        kind="tokenizers_hf",
        repo_or_encoding="Qwen/Qwen2.5-7B-Instruct",
        status="verified",
        attribution_caveat="Alibaba production. Qwen 3.x revisions may diverge.",
    ),
    TokSpec(
        vendor="DeepSeek",
        name="deepseek-v3",
        kind="tokenizers_hf",
        repo_or_encoding="deepseek-ai/DeepSeek-V3",
        status="verified",
        attribution_caveat="Production for V3+ series. V1/V2 tokenizers different.",
    ),
    TokSpec(
        vendor="Mistral",
        name="mistral-v3",
        kind="tokenizers_hf",
        repo_or_encoding="mistralai/Mistral-7B-Instruct-v0.3",
        status="verified",
    ),
    TokSpec(
        vendor="Meta Llama",
        name="llama3",
        kind="tokenizers_hf",
        repo_or_encoding="meta-llama/Meta-Llama-3-8B-Instruct",
        status="verified",
        attribution_caveat="Llama 3 family. Earlier Llama tokenizers were SentencePiece, different shape.",
    ),
    TokSpec(
        vendor="01.AI Yi",
        name="yi-1.5",
        kind="tokenizers_hf",
        repo_or_encoding="01-ai/Yi-1.5-9B-Chat",
        status="verified",
    ),
    TokSpec(
        vendor="Cohere",
        name="command-r",
        kind="tokenizers_hf",
        repo_or_encoding="CohereForAI/c4ai-command-r-v01",
        status="verified",
    ),
    TokSpec(
        vendor="Zhipu GLM",
        name="glm-4",
        kind="tokenizers_hf",
        repo_or_encoding="THUDM/glm-4-9b-chat",
        status="verified",
        attribution_caveat="Production GLM-4 line.",
    ),
    TokSpec(
        vendor="MiniMax",
        name="minimax-text",
        kind="tokenizers_hf",
        repo_or_encoding="MiniMaxAI/MiniMax-Text-01",
        status="verified",
    ),
    TokSpec(
        vendor="Sarvam",
        name="sarvam-1",
        kind="tokenizers_hf",
        repo_or_encoding="sarvamai/sarvam-1",
        status="verified",
        attribution_caveat="22 Indian languages optimized.",
    ),
    TokSpec(
        vendor="Microsoft Phi",
        name="phi-3.5",
        kind="tokenizers_hf",
        repo_or_encoding="microsoft/Phi-3.5-mini-instruct",
        status="verified",
        attribution_caveat="Represents Microsoft on-device / Copilot+ PC inference family.",
    ),
]


# ============================================================================
# SURROGATE (4) — HF repo is a PROXY, not the production tokenizer
# ============================================================================

SURROGATE = [
    TokSpec(
        vendor="ByteDance Doubao",
        name="seed-oss-surrogate",
        kind="tokenizers_hf",
        repo_or_encoding="ByteDance-Seed/Seed-OSS-36B-Instruct",
        status="surrogate",
        attribution_caveat=(
            "Doubao production tokenizer (Volcengine) is not public. Seed-OSS is "
            "ByteDance's open-source family and the closest available proxy. "
            "v0.1 reports the gap if measurable via API; treat headline numbers "
            "as approximate for Doubao."
        ),
    ),
    TokSpec(
        vendor="Moonshot Kimi",
        name="kimi-k2-thirdparty",
        kind="tokenizers_hf",
        repo_or_encoding="moonshotai/Moonlight-16B-A3B-Instruct",  # Moonshot's own published variant
        status="surrogate",
        attribution_caveat=(
            "Kimi production K2.x tokenizer not directly published. Moonlight is "
            "Moonshot AI's published model and likely shares tokenizer family."
        ),
    ),
    TokSpec(
        vendor="Tencent Hunyuan",
        name="hunyuan-large",
        kind="tokenizers_hf",
        repo_or_encoding="tencent/Hunyuan-Large",
        status="surrogate",
        attribution_caveat=(
            "Hunyuan Large is Tencent's open release; production Hy3 may differ."
        ),
    ),
    TokSpec(
        vendor="Anthropic Claude",
        name="claude-no-public-tokenizer",
        kind="tokenizers_hf",
        repo_or_encoding="",
        status="excluded",
        attribution_caveat=(
            "Anthropic does not publish production tokenizer. count_tokens API "
            "is rate-limited (Tier 1 = 100 RPM). Deferred to v0.2 API-backed appendix."
        ),
    ),
]


# ============================================================================
# EXCLUDED — explicit decisions to leave out of v0.1
# ============================================================================

EXCLUDED = [
    TokSpec(
        vendor="iFlytek Spark",
        name="excluded",
        kind="tokenizers_hf",
        repo_or_encoding="",
        status="excluded",
        attribution_caveat="HF only has narrow specialized snapshots (Chemistry-X1 etc.). Not representative.",
    ),
    TokSpec(
        vendor="Google Gemini",
        name="deferred-to-api",
        kind="tokenizers_hf",
        repo_or_encoding="",
        status="excluded",
        attribution_caveat="No public tokenizer. count_tokens API rate-limited; deferred to v0.2.",
    ),
    TokSpec(
        vendor="Baidu ERNIE",
        name="deferred",
        kind="tokenizers_hf",
        repo_or_encoding="baidu/ERNIE-4.5-21B-A3B-PT",
        status="excluded",
        attribution_caveat="Open variant exists but production ERNIE 4.5 may differ. Re-evaluate for v0.2.",
    ),
]


def all_active() -> list[TokSpec]:
    """Return only specs that will be measured (verified + surrogate, excluding excluded)."""
    return [s for s in VERIFIED + SURROGATE if s.status != "excluded"]


def by_status(status: str) -> list[TokSpec]:
    return [s for s in VERIFIED + SURROGATE + EXCLUDED if s.status == status]


if __name__ == "__main__":
    active = all_active()
    print(f"STU v0.1 active tokenizer count: {len(active)}")
    print(f"  verified:   {len([s for s in active if s.status == 'verified'])}")
    print(f"  surrogate:  {len([s for s in active if s.status == 'surrogate'])}")
    print(f"  excluded:   {len(by_status('excluded'))} (not measured)")
    print()
    for s in active:
        marker = "[s]" if s.status == "surrogate" else "[v]"
        print(f"  {marker} {s.vendor:<22s} {s.name}")
