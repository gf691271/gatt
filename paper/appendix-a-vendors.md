# Appendix A. Full Vendor List with Confidence Ratings (May 9, 2026)

The full vendor table from GATT v0.82, ordered by daily token throughput. All figures in trillions of tokens per day. Confidence ratings per Section 3.2. The dataset is the canonical source; this appendix is a reproducible extract.

| Rank | Vendor | Country | Daily Tokens (T) | Confidence | Tier | Source date | Notes |
|------|--------|---------|-----------------:|:----------:|:----:|-------------|-------|
| 1 | Doubao (ByteDance) | CN | 129.0 | High | 1 | 2026-04-07 | All-sources scope; Volcengine official 120T baseline (Apr 1) |
| 2 | Google Gemini (All Surfaces) | US | 73.0 | High | 1 | 2026-04-09 | Pichai 16B tokens/min API; 3.2× All Surfaces multiplier |
| 3 | OpenAI (ChatGPT + API) | US | 45.0 | High | 1 | 2026-05-05 | 15B tokens/min API; GPT-5.5 + 5.5 Instant launches |
| 4 | Anthropic Claude | US | 22.0 | High | 1 | 2026-04-16 | Opus 4.7 + 35% tokenizer expansion + MAU +44% |
| 5 | DeepSeek | CN | 9.2 | Low | 2 | 2026-04-24 | V4 Pro/Flash launch; 1M context; #3 enterprise SDK |
| 6 | Microsoft Azure + Copilot | US | 10.0 | Medium | 1 | 2026-04-29 | Q3 FY26: $37B AI ARR; 20M Copilot seats |
| 7 | Qwen (Alibaba Cloud) | CN | 6.2 | Medium | 1 | 2026-04-02 | Qwen 3.6-Plus; Alibaba Token Hub reorg |
| 8 | OpenRouter (aggregator) | US | 3.0 | High | 1 | 2026-04-30 | Aggregator overlap with vendor totals; 20T/week April |
| 9 | Hy3 / Hunyuan 3.0 (Tencent) | CN | 2.7 | Low | 2 | 2026-04-23 | Open-sourced; 295B-A21B MoE; 256K context |
| 10 | Kimi (Moonshot AI) | CN | 2.5 | Medium | 1 | 2026-04-20 | K2.6 launch; ARR doubled; $20B valuation |
| 11 | ERNIE (Baidu) | CN | 1.85 | Medium | 1 | 2026-01-25 | 2.4T params MoE; 202M MAU; IDC #3 (17%) |
| 12 | Spark (iFlytek) | CN | 1.62 | Medium | 1 | 2025-Q4 | iFlytek Q4 2025 earnings |
| 13 | Mistral AI | FR | 0.74 | Low | 2 | 2025-Q4 | $400M ARR back-calculation |
| 14 | Grok (xAI) | US | 0.55 | Low | 2 | 2026-04-15 | First negative-growth vendor (-5%/mo) |
| 15 | MiniMax | CN | 0.42 | Medium | 1 | 2026-02 | OpenRouter + HuggingFace data |
| 16 | Perplexity AI | US | 0.35 | Medium | 1 | 2026-04-30 | 45M MAU; $200M ARR Sep 2025 |
| 17 | Groq | US | 0.32 | Low | 2 | 2026-01-15 | LPU capacity back-calc |
| 18 | MiMo-V2-Pro (Xiaomi) | CN | 0.30 | Low | 2 | 2026-03-18 | NEW v0.81; 1T params MoE; 1M context |
| 19 | Llama API (Meta) | US | 0.23 | Low | 2 | 2026-03-15 | "Virtually no standalone users vs OpenAI" |
| 20 | Amazon Bedrock | US | 0.17 | Low | 2 | 2025-Q4 | AWS revenue ÷ price |
| 21 | GLM (Zhipu AI) | CN | 0.13 | Medium | 1 | 2026-02 | OpenRouter data |

**Confidence distribution:** 4 High · 2 Medium-high · 5 Medium · 10 Low (totals to 21)
**Tier distribution:** 12 Tier-1 (direct or strong indirect) · 9 Tier-2 (back-calc / proxy)
**Country distribution:** 10 US · 10 CN · 1 FR (totals to 21)

**Vendor sum:** 309.28T per day across 21 vendors. The reported global total of 310T per day in the main text rounds the vendor sum (309.28T) and adds a small (~0.7T) Rest-of-World residual for activity in non-tracked geographies (Saudi Arabia, India, Brazil, Indonesia, etc.) not attributable to any tracked vendor headquarters. The `token_gdp.breakdown` regional totals in the dataset (US 154T + CN 154T + EU 9T + ROW 6T = 323T) include a further allocation of country-level non-vendor-attributable usage, which is why the regional sum exceeds the vendor sum by ~13T (~4%). This residual is documented in the dataset's `correction_log` and represents enterprise / consumer AI usage in tracked countries that uses non-tracked vendors or self-hosted open-weight models.

**Source files:**
- Live data: `data/tci-latest.json`
- Immutable snapshot: `data/snapshots/2026-05-09.json`
- Per-vendor revision history: each vendor entry's `revision_history` array
