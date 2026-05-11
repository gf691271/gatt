# STU v0.1 — Standardized Token Unit Calibration Matrix

**Status**: Scaffolding only. NOT executed. Awaits user go/no-go.

**Purpose**: Calibration data for GATT's `Section 3 — Methodology`. Cross-vendor tokenizer ratio matrix.

**Honest framing** (post-Petrov-Ahia 2023 discovery): This is a **2026 frontier-vendor refresh of Petrov et al. NeurIPS 2023 + Ahia et al. EMNLP 2023 methodology**, applied as prerequisite calibration for GATT's empirical token-economy measurement. NOT a standalone "STU framework" stake claim.

## Prior work cited

- Petrov et al. 2023 NeurIPS — *Language Model Tokenizers Introduce Unfairness Between Languages* (arXiv:2305.15425). 22 models × 70+ languages. We refresh with 2024-2026 frontier vendors.
- Ahia et al. 2023 EMNLP — *Do All Languages Cost The Same?* (arXiv:2305.13707). Tokenization × pricing across languages. We integrate with GATT's measured Token Economy.
- OpenRouter QuadChars — first production cross-vendor normalization. We cite as the only deployed precedent.
- Velasco et al. 2025 (Max Planck) — argues for character-billing as fix for tokenization billing fraud. We cite as motivation.

## Scope

| Element | Decision |
|---|---|
| Verified HF tokenizers | ~12 (Qwen, DeepSeek, Mistral, Llama, Yi, Cohere Command R, GLM, MiniMax, Sarvam, MiMo, Hunyuan, Phi) |
| Surrogate tokenizers | 3-5 (Doubao = ByteDance Seed-OSS; Kimi = K2 third-party; Spark excluded as too narrow snapshot) |
| OpenAI via tiktoken | cl100k_base + p50k_base + o200k_base (3 encodings, treated as 1 vendor row) |
| Anthropic + Gemini API | Optional appendix only — rate-limit gated, may defer to v0.2 |
| Languages | 12 (English, Chinese, Hindi, Arabic, Spanish, French, German, Japanese, Korean, Russian, Portuguese, Indonesian) |
| Samples per cell | N=200 (1.18× over 167 Bonferroni minimum; saves 60% API quota vs N=500) |
| Metrics per cell | mean chars/token, mean UTF-8 bytes/token, variance, sample size, status tag |
| Corpus source | FLORES-200 (BY-SA 4.0, redistributable as BY-SA) — sentences only, no proprietary corpus |
| License | Output: aggregate stats only as CC BY 4.0; sample provenance: row IDs + SHA256 only, NO redistributed text |

## Output

- `output/tokenizer_ratio_matrix_v0.1.parquet` — main matrix
- `output/tokenizer_registry.json` — provenance (repo, revision SHA, surrogate flag)
- `output/sample_manifest.json` — upstream dataset row IDs + hashes (no text)
- `output/dataset_card.md` — HuggingFace dataset card with limitations
- `output/methodology_note.md` — 1-page methodology

## What we are NOT producing

- A standalone arXiv paper (Petrov + Ahia already published the foundational work)
- A "Standardized Token Unit framework" stake claim (premature; needs sustained output first)
- The full Section 6 critique catalog (Token Velocity cut, Token GDP rename, etc.) — separate paper-revision concern
- Reasoning-token measurement (deferred to v0.2 with $1-2K budget)
- Multimodal measurement (deferred to v0.2)
- I/O ratio measurement (deferred to v0.2)
- Hardware/FLOP equivalence (deferred to v1.0)

## Implementation plan

3-day wall-clock, 18-25 work hours:

**Day 1 (8h, $0)**: Run tokenizer matrix on verified HF + tiktoken (no API calls)
**Day 2 (6h, $1-5)**: Surrogate validation — call real Volcengine/Kimi APIs 50× each to compare Seed-OSS vs production tokenizer. If gap > 15% on headline vendors, halt and rethink.
**Day 3 (4h, $0)**: HuggingFace dataset publication + dataset card + MLCommons WG email

## Environment blocker (2026-05-11)

Python 3.13 has an `importlib.metadata` bug that breaks `transformers` import (`Distribution.files() missing 'name' argument`). Workaround options:
- Use `tokenizers` (Rust-backed) library directly instead of `transformers.AutoTokenizer`
- Downgrade to Python 3.12
- Patch the corrupted `.dist-info` (need to identify which package)

Decision: STU v0.1 will use **direct `tokenizers` library** to sidestep the bug. Trade-off: slightly more boilerplate code, no `trust_remote_code=True` support (cuts DeepSeek, GLM, MiniMax — which we replace with their published `tokenizer.json` if available, else skip).

## Go/no-go checkpoint

Day 2 surrogate-validation gate:
- If Doubao Seed-OSS vs Volcengine production tokenizer gap ≤ 5%: proceed
- If gap 5-15%: proceed with explicit warning in dataset card
- If gap > 15%: **halt**. Surrogate approach is insufficient for headline vendor. Reconsider entire approach.

Without this gate, the matrix could be misleading on the most-consumed vendor in GATT (Doubao at 129T/day = 41% of global volume).
