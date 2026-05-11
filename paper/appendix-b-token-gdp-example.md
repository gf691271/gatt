# Appendix B. Token GDP Worked Example (May 9, 2026 — v1.0 publication-state)

This appendix walks through the Token GDP calculation in full, demonstrating how regional aggregations are derived from per-vendor estimates and how the v1.0 headline $95.8 billion annualized figure was obtained.

**v1.4 update note (2026-05-11):** The worked example below is preserved as the v1.0 reproducible tutorial anchored to the immutable snapshot `data/snapshots/2026-05-09.json` (21 vendors, $95.8B annualized). The v1.3 vendor expansion added Apple Intelligence Private Cloud Compute (US, +2T, ~+$3M/day at $1.50/M), Cohere (CA, +0.10T, ~+$0.15M/day at $1.50/M), and Sarvam AI (IN, +0.05T, ~+$0.025M/day at $0.50/M), shifting the v1.4 headline to **$97.0 billion annualized** ($265.8M/day on 311T/day across 24 vendors). Readers wishing to reproduce the v1.4 headline should apply these three additions to the v1.0 base below; readers wishing to follow the worked-example pedagogy intact should use the v1.0 numbers as published.

## B.1 Per-Vendor Volume by Region

Vendor token volumes from Appendix A are summed by country of operation (vendor headquarters):

**United States vendors (10):**
| Vendor | Daily T |
|--------|--------:|
| Gemini (All Surfaces) | 73.00 |
| OpenAI (ChatGPT + API) | 45.00 |
| Anthropic Claude | 22.00 |
| Microsoft Azure + Copilot | 10.00 |
| OpenRouter | 3.00 |
| Grok (xAI) | 0.55 |
| Perplexity AI | 0.35 |
| Groq | 0.32 |
| Llama API (Meta) | 0.23 |
| Amazon Bedrock | 0.17 |
| **US Subtotal** | **154.62** |

**China vendors (9):**
| Vendor | Daily T |
|--------|--------:|
| Doubao (ByteDance) | 129.00 |
| DeepSeek | 9.20 |
| Qwen (Alibaba Cloud) | 6.20 |
| Hy3 / Hunyuan 3.0 (Tencent) | 2.70 |
| Kimi (Moonshot AI) | 2.50 |
| ERNIE (Baidu) | 1.85 |
| Spark (iFlytek) | 1.62 |
| MiniMax | 0.42 |
| MiMo-V2-Pro (Xiaomi) | 0.30 |
| GLM (Zhipu AI) | 0.13 |
| **CN Subtotal** | **153.92** |

**Europe vendors (1):**
| Vendor | Daily T |
|--------|--------:|
| Mistral AI | 0.74 |
| **EU Subtotal** | **0.74** |

**Vendor sum:** 154.62 + 153.92 + 0.74 = 309.28T per day.

The reported global total of 310T per day rounds the vendor sum and includes a small Rest of World residual (~0.7T) covering non-tracked vendor activity in Saudi Arabia, India, Brazil, etc. For Token GDP purposes, the regional breakdown below uses adjusted figures of US = 154T, CN = 154T, EU = 9T (vendor + non-vendor European usage), ROW = 6T to maintain consistency with the country-level breakdown in the main dataset.

## B.2 Regional Blended Pricing

Pricing assumptions applied to each region (May 2026, vendor-volume-weighted blends across input/output rates and model lineups):

| Region | Price ($ per million tokens) | Rationale |
|--------|------------------------------:|-----------|
| United States | $1.50 | Blended across GPT-5.5 ($5/$30 → $8 weighted), Opus 4.7 ($5/$25 → $7.50 weighted), Gemini 3.x mid-tier (~$0.30), and aggregator-routed lower-cost models. Volume-weighted by vendor share. |
| Europe | $1.20 | Mistral pricing tier; lower than US frontier but Western-pricing structure. |
| China | $0.10 | Blended across Doubao (~$0.06), DeepSeek V4 ($0.145/$1.74 → $0.34 weighted), Qwen, Kimi K2.6 ($0.60/$2.50 → $1.10 weighted). Volume-weighted; Doubao's dominant share pulls the blend down. |
| Rest of World | $0.90 | Mid-tier average. |

**Pricing volatility caveat:** Per Xing [6], GPT-4-equivalent output pricing fell from approximately $60 per million tokens (early 2023) to under $1.50 per million (early 2025) — a 40-fold reduction in 24 months. The May 2026 blended figures above will likely shift within months. All Token GDP figures must be cited with as-of dates.

## B.3 Token GDP Calculation

For each region:

$$ \text{Token GDP}_{\text{region}} = V_{\text{region}} \cdot p_{\text{region}} $$

Where V is in trillions of tokens per day and p is in dollars per million tokens. Conversion: 1 trillion tokens = 1,000,000 million tokens, so multiply by p directly to get dollars per day.

| Region | Volume (T/day) | Price ($/M) | Daily GDP ($M) | Annualized ($B) |
|--------|---------------:|------------:|---------------:|----------------:|
| United States | 154 | $1.50 | $231.0 | $84.3 |
| China | 154 | $0.10 | $15.4 | $5.6 |
| Europe | 9 | $1.20 | $10.8 | $3.9 |
| Rest of World | 6 | $0.90 | $5.4 | $2.0 |
| **Global** | **323** | — | **$262.6** | **$95.8** |

**Reconciliation of the three volume bases.** Three distinct sums appear in this paper: (a) the per-vendor sum (309.28T), the strict aggregate of GATT's 21 tracked vendor estimates; (b) the rounded global total in the main text (310T); and (c) the regional Token GDP base (323T = US 154T + CN 154T + EU 9T + ROW 6T). The 13T (4%) residual between (b) and (c) represents country-level enterprise and consumer AI usage in tracked countries that is not attributable to any of GATT's 21 tracked vendor headquarters — primarily self-hosted open-weight model deployments (Llama, Qwen-OSS, Mistral-OSS) and smaller regional providers in the UK, Germany, France, Japan, South Korea, Canada, India, Brazil, Saudi Arabia, and Indonesia. The 13T residual is allocated to regions in proportion to country-level estimated AI usage (per-capita scaling). Token GDP is computed on the regional base (323T) because the regional pricing assumptions implicitly cover all in-region consumption; computing Token GDP on the strict vendor sum (309.28T) would understate the regional aggregates by 4%. We adopt the regional base for Token GDP figures throughout this paper.

**Annualized:** $262.6M per day × 365 = $95.85B per year.

## B.4 GDP Share Decomposition

| Region | Volume Share | Token GDP Share | Pricing Multiple |
|--------|-------------:|----------------:|-----------------:|
| United States | 49.7% | 88.0% | 1.77× |
| China | 49.7% | 5.9% | 0.12× |
| Europe | 2.9% | 4.1% | 1.42× |
| Rest of World | 1.9% | 2.0% | 1.05× |

The "Pricing Multiple" column is the ratio of GDP share to volume share. The United States produces 1.77× more economic value per token than the global average; China produces 0.12× — a 15× pricing gap.

## B.5 Sensitivity Analysis

Token GDP is sensitive to pricing assumptions. We bracket headline figures with three pricing scenarios:

| Scenario | US blended | CN blended | Daily GDP ($M) | Annualized ($B) |
|----------|-----------:|-----------:|---------------:|----------------:|
| Conservative (current GATT) | $1.50 | $0.10 | $262.6 | $95.8 |
| Aggressive (US frontier-weighted) | $3.00 | $0.10 | $493.4 | $180.1 |
| Decline-adjusted (Xing 40× projection) | $0.50 | $0.05 | $97.7 | $35.7 |

The "Aggressive" scenario reflects a reader who interprets US blended pricing as anchored to frontier models (Opus 4.7, GPT-5.5) rather than the volume-weighted blend. The "Decline-adjusted" scenario applies Xing's [6] projected pricing trajectory forward. Both are within reasonable interpretive ranges.

GATT v0.83 will publish these sensitivity bands directly in the dataset rather than only in this paper, addressing the most common reader-feedback question on Token GDP figures.
