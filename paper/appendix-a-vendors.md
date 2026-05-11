# Appendix A. Full Vendor List with Confidence Ratings (May 11, 2026)

The full vendor table from GATT v1.4, ordered by daily token throughput. All figures in trillions of tokens per day. Confidence ratings per Section 3.2 (4-level upgrade in v1.1). The dataset is the canonical source; this appendix is a reproducible extract. The v0.82 table below has been augmented with the three v1.3 additions (Apple Intelligence cloud-routed, Cohere, Sarvam AI) re-ranked into the global volume ordering; the v0.82 snapshot remains immutable at `data/snapshots/2026-05-09.json`.

| Rank | Vendor | Country | Daily Tokens (T) | Confidence | Tier | Source date | Notes |
|------|--------|---------|-----------------:|:----------:|:----:|-------------|-------|
| 1 | Doubao (ByteDance) | CN | 129.0 | High | 1 | 2026-04-07 | All-sources scope; Volcengine official 120T baseline (Apr 1) |
| 2 | Google Gemini (All Surfaces) | US | 73.0 | Medium | 1 | 2026-04-09 | Pichai 16B tokens/min API observed; 3.2× All Surfaces multiplier is editorial (downgraded from High in v1.0 per Sokolov critique) |
| 3 | OpenAI (ChatGPT + API) | US | 45.0 | High | 1 | 2026-05-05 | 15B tokens/min API; GPT-5.5 + 5.5 Instant launches |
| 4 | Anthropic Claude | US | 22.0 | High | 1 | 2026-04-16 | Opus 4.7 + 35% tokenizer expansion + MAU +44% |
| 5 | Microsoft Azure + Copilot | US | 10.0 | Medium-High | 1 | 2026-04-29 | Q3 FY26: $37B AI ARR; 20M Copilot seats |
| 6 | DeepSeek | CN | 9.2 | Low | 2 | 2026-04-24 | V4 Pro/Flash launch; 1M context; #3 enterprise SDK |
| 7 | Qwen (Alibaba Cloud) | CN | 6.2 | Medium | 1 | 2026-04-02 | Qwen 3.6-Plus; Alibaba Token Hub reorg |
| 8 | OpenRouter (aggregator) | US | 3.0 | High | 1 | 2026-04-30 | Aggregator overlap with vendor totals; 20T/week April |
| 9 | Hy3 / Hunyuan 3.0 (Tencent) | CN | 2.7 | Low | 2 | 2026-04-23 | Open-sourced; 295B-A21B MoE; 256K context |
| 10 | Kimi (Moonshot AI) | CN | 2.5 | Medium | 1 | 2026-04-20 | K2.6 launch; ARR doubled; $20B valuation |
| 11 | Apple Intelligence (Private Cloud Compute) | US | 2.0 | Low | 2 | 2026-05-11 | v1.3 NEW. Cloud-only estimate; on-device excluded; WWDC 2026-pending |
| 12 | ERNIE (Baidu) | CN | 1.85 | Medium | 1 | 2026-01-25 | 2.4T params MoE; 202M MAU; IDC #3 (17%) |
| 13 | Spark (iFlytek) | CN | 1.62 | Medium | 1 | 2025-Q4 | iFlytek Q4 2025 earnings |
| 14 | Mistral AI | FR | 0.74 | Low | 2 | 2025-Q4 | $400M ARR back-calculation |
| 15 | Grok (xAI) | US | 0.55 | Low | 2 | 2026-04-15 | First negative-growth vendor (-5%/mo) |
| 16 | MiniMax | CN | 0.42 | Medium | 1 | 2026-02 | OpenRouter + HuggingFace data |
| 17 | Perplexity AI | US | 0.35 | Medium | 1 | 2026-04-30 | 45M MAU; $200M ARR Sep 2025 |
| 18 | Groq | US | 0.32 | Low | 2 | 2026-01-15 | LPU capacity back-calc |
| 19 | MiMo-V2-Pro (Xiaomi) | CN | 0.30 | Low | 2 | 2026-03-18 | v0.81; 1T params MoE; 1M context |
| 20 | Llama API (Meta) | US | 0.23 | Low | 2 | 2026-03-15 | "Virtually no standalone users vs OpenAI" |
| 21 | Amazon Bedrock | US | 0.17 | Low | 2 | 2025-Q4 | AWS revenue ÷ price |
| 22 | GLM (Zhipu AI) | CN | 0.13 | Medium | 1 | 2026-02 | OpenRouter data |
| 23 | Cohere (Command R+ / Command A) | CA | 0.10 | Low | 2 | 2026-05-11 | v1.3 NEW. First Canada-HQ entry; enterprise-only; $80M ARR back-calc |
| 24 | Sarvam AI (Sarvam-M, Sarvam-1) | IN | 0.05 | Low | 2 | 2026-05-11 | v1.3 NEW. First India-HQ vendor; 22 Indian languages; IndiaAI Mission |

**Confidence distribution (v1.4):** 3 High · 2 Medium-High · 8 Medium · 11 Low (totals to 24). The Gemini All Surfaces composite was downgraded from High to Medium in v1.0 (Sokolov critique on 3.2× All-Surfaces multiplier as editorial). v1.1 introduced the 4-level taxonomy (adding Medium-High between High and Medium). v1.3 added 3 Low-confidence entries (Apple Intelligence, Cohere, Sarvam) — all judgment-based until WWDC 2026 and other vendor disclosures land.

**Parameter classification (v1.4, per Inference Bottleneck arXiv:2604.17431 [12], downsunk to vendor row in v1.1):** Each estimate is classified by source quality. *Observed* (4 vendors): Doubao Volcengine official + IDC validation; OpenAI 15B tokens/min API official; Pichai Gemini 16B tokens/min API; Anthropic ARR trajectory. *Inferred* (10 vendors): Microsoft, Qwen, OpenRouter, Hy3, Kimi, ERNIE, Spark, MiniMax, Perplexity, DeepSeek — corroborated indirect signals. *Judgment-based* (10 vendors): Mistral, Grok, Groq, Xiaomi MiMo, Llama API, Bedrock, GLM, plus v1.3 additions (Apple, Cohere, Sarvam). The All Surfaces multiplier for Gemini (3.2×) and Anthropic 35% tokenizer expansion factor remain judgment-based even though the underlying vendor signals are observed.
**Tier distribution:** 12 Tier-1 (direct or strong indirect) · 12 Tier-2 (back-calc / proxy / judgment)
**Country distribution:** 11 US · 10 CN · 1 FR · 1 CA · 1 IN (totals to 24)

**Vendor sum:** 311.43T per day across 24 vendors. The reported global total of 311T per day in the main text rounds the vendor sum. The `token_gdp.breakdown` regional totals in the dataset (US 156T + CN 154T + EU 9T + ROW 6.15T = 325T) include a further allocation of country-level non-vendor-attributable usage; the regional sum exceeds the vendor sum by ~14T (~4.4%). This residual is documented in the dataset's `correction_log` and represents enterprise / consumer AI usage in tracked countries that uses non-tracked vendors or self-hosted open-weight models.

**Source files:**
- Live data: `data/tci-latest.json`
- Immutable snapshot: `data/snapshots/2026-05-09.json`
- Per-vendor revision history: each vendor entry's `revision_history` array
