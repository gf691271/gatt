# 4. Empirical Findings

This section reports headline findings from the GATT v0.82 dataset as of May 9, 2026. All figures are reproducible from `data/snapshots/2026-05-09.json` in the project repository. Where a figure depends on extrapolation between disclosures, the source date and growth-rate assumption are documented in the corresponding vendor entry's `revision_history`.

## 4.1 Global Volume

Global daily AI inference output stands at **310 trillion tokens per day** as of May 9, 2026. The headline figure aggregates 21 tracked vendors across 12 countries, with a small "Rest of World" residual covering geographies not yet broken out individually. Growth has run at approximately 22% per month over the preceding eight weeks — a doubling time of roughly 3.5 months. Extrapolating this rate forward through year-end 2026 yields a projection band of **1.1 to 1.5 quadrillion tokens per day** by December 2026, with the conservative end of the band assuming growth deceleration to 18% per month and the aggressive end assuming sustained 22% per month.

The 310T figure is itself the result of substantial recent revisions. GATT v0.79 (May 4, 2026) reported 264T per day; v0.80 (also May 9) raised this to 305T after seven vendor anchor upgrades reflecting Pichai's 16-billion-tokens-per-minute Q1 disclosure, Anthropic's Opus 4.7 launch and 44% MAU surge, Microsoft's Q3 FY26 $37B AI ARR earnings release, Kimi K2.6's launch and ARR doubling, DeepSeek V4 Pro/Flash's launch, and minor adjustments to Qwen and Hunyuan. v0.81 added 5 trillion tokens per day from third-party revisions (OpenRouter platform data, Perplexity user metrics, and the new Xiaomi MiMo entry). The week-over-week swing from 264T to 310T (+17%) reflects measurement-update density rather than a single underlying growth event; vendor activity in the April 1 to May 9 window was unusually rich in publishable signals.

### 4.1.1 Sensitivity Band on the Headline

The 310T point estimate carries methodological uncertainty that warrants explicit bracketing. Following the parameter classification template from Inference Bottleneck [12] (observed / inferred / judgment-based), GATT publishes three scenarios for the headline global figure:

| Scenario | Global daily tokens (T) | Methodology |
|---|---:|---|
| Conservative | 250 | Photons=Tokens-anchored: trim Gemini All-Surfaces multiplier 3.2× → 2.5×; trim Doubao all-sources by 5% (cache adjustment); apply 15% reduction across vendors with low-confidence ratings |
| **Best estimate** | **310** | **GATT v0.86 published values; vendor-volume-weighted, all-sources, May 9, 2026 anchored** |
| Aggressive | 400 | 22%/mo growth assumption holds through end-Q2 2026; assumes 1-2 additional Pichai-class US disclosures by mid-June |

The conservative bound (250T) maintains all five qualitative GATT findings — China-US volume near-parity (53/47 in conservative), US Token GDP dominance ≥85%, per-capita gap ≥450× US/India, growth trajectory positive, and the 2× tension with the Photons=Tokens 2028 ceiling persists (350K conservative US per-capita > 225K ceiling). The qualitative robustness of GATT's headline claims to conservative recalibration is, in our judgment, the strongest argument for citing GATT figures despite the unavoidable measurement uncertainty in the underlying vendor data.

## 4.2 Volume Parity Between China and the United States

For the first time since GATT began publishing in February 2026, the China and United States token-volume shares are essentially tied. As of May 9: **China 50.0% of global volume (153.92 trillion tokens per day)**, **United States 49.7% (154.62 trillion tokens per day)**, with Europe at 0.24% (0.74 trillion, dominated by Mistral) and the Rest of World residual at the remainder.

The convergence is recent. On April 6, 2026, GATT v0.75 measured China at 58% and the United States at 35%. The 5-week shift to 50/50 reflects new United States hard-data disclosures rather than slowed Chinese growth: Pichai's 16-billion-tokens-per-minute API disclosure (a 60% quarter-over-quarter increase from Q4 2025's 10 billion) raised Gemini's All Surfaces estimate from 57T to 73T; Microsoft's Q3 FY26 disclosure of $37 billion AI business ARR (+123% year-over-year) and 20 million paid Copilot seats raised Microsoft's estimate from 8.1T to 10T; OpenAI's GPT-5.5 launch (April 23) and GPT-5.5 Instant rollout (May 5) raised OpenAI's estimate from 40T to 45T; Anthropic's Opus 4.7 launch (April 16, with a new tokenizer producing up to 35% more tokens per equivalent input) plus 44% Claude monthly-active-user growth raised Anthropic from 15T to 22T. China's leaders held steady on extrapolation through the same window, with no comparably large new disclosures.

The volume parity is the headline geo-economic finding of the v0.82 release. It does not, however, imply economic parity — see Section 4.3.

## 4.3 Token GDP Asymmetry

Daily Token GDP — vendor volume × regional blended price (Section 3.5) — totals **$262.6 million per day** ($95.8 billion annualized). The regional split is the inverse of volume:

- **United States: $231 million per day, 88% of global Token GDP, on 49.7% of volume.**
- **China: $15.4 million per day, 6% of global Token GDP, on 50.0% of volume.**
- Europe: $10.8 million per day, 4% of Token GDP, on 0.24% of volume.
- Rest of World: $5.4 million per day, 2% of Token GDP, on 1.4% of volume.

The driver is a 15× pricing gap between United States and Chinese vendors. Anthropic's Opus 4.7 prices at $5 per million input tokens and $25 per million output (a blend of approximately $7.50 per million); GPT-5.5 prices at $5/$30 per million ($8 blended); Doubao prices at approximately $0.10 per million blended; DeepSeek V4 Pro at $0.145 input / $1.74 output. Volume parity at 50/50 thus produces economic value at 88/6 — the central paradox of the May 2026 Token Economy.

This finding has implications for governance. Token-volume parity is consistent with claims of Chinese AI parity at the *capacity* level, but the 88/6 GDP split shows that capacity does not equal economic value. Conversely, the United States retains a substantial economic-value moat even as raw volume normalizes. Both observations are durable: the pricing gap has held at roughly 15× across the past year, despite substantial Chinese-vendor pricing pressure.

## 4.4 Per-Capita Inequality

Dividing country tokens by national population produces the AI-inequality findings:

- **United States: 459,700 tokens per resident per day** (rank 1)
- **China: 110,000 tokens per resident per day** (rank 2)
- United Kingdom: 59,700 (rank 3)
- France: 35,300 (rank 4)
- Canada: 29,000 (rank 5)
- Germany: 26,200 (rank 6)
- South Korea: 24,400 (rank 7)
- Japan: 14,900 (rank 8)
- Saudi Arabia: 14,000 (rank 9)
- Brazil: 4,600 (rank 10)
- India: 770 (rank 11)
- Indonesia: 940 (rank 12 by absolute, rank 11 by per-capita)

The headline ratio is **United States to India = 597×**. As recently as April 6, 2026, this gap stood at 394×; one month later it has widened to 597× — meaningfully faster than absolute United States token growth alone, because the United States per-capita base is leveraging upward via product launches and tokenizer changes while India's per-capita base is barely moving from 0.66K to 0.77K over the same window. The gap is wider than the corresponding income ratio (approximately 30× by GDP per capita) and substantially wider than the digital-divide gap measured by mobile or internet penetration. We treat this as the most striking inequality finding in the dataset.

## 4.5 Top Vendor Findings

The top four vendors account for **88% of global volume**:

- **Doubao (ByteDance, China): 129 trillion tokens per day**, 42% of global. All-sources scope including external Volcengine MaaS, Douyin AI Search, the Doubao consumer app, the Jimeng image-generation pipeline, and internal Volcengine workflows. The May 7, 2026 IDC China Public Cloud MaaS report independently confirms Volcengine #1 in China at 49.5% market share for full-year 2025 [4]. The all-sources vs. external-MaaS scope reconciliation is detailed in Section 3.3.

- **Gemini (Google, All Surfaces): 73 trillion tokens per day**, 24% of global. Anchored in Pichai's Cloud Next 2026 / Q1 2026 earnings disclosure of "more than 16 billion tokens per minute via direct API," up from 10 billion in Q4 2025. The 73T figure applies a 3.2× All Surfaces multiplier to the disclosed API rate (23T API-only); the multiplier accounts for Search AI Overviews, the Gemini App's 750 million monthly active users, and Google Workspace integrations. Section 5 considers whether this multiplier may overestimate.

- **OpenAI (ChatGPT and API): 45 trillion tokens per day**, 15% of global. Anchored in the March 31, 2026 official disclosure of "more than 15 billion tokens per minute" across the OpenAI API, supplemented by consumer-side activity (2.5 billion ChatGPT prompts per day, 9 million paid business users) and the GPT-5.5 / GPT-5.5 Instant launches in late April and early May.

- **Anthropic (Claude): 22 trillion tokens per day**, 7% of global. The Opus 4.7 launch on April 16, 2026 introduced a tokenizer producing up to 35% more tokens per equivalent input — a direct lift to GATT's volume estimate. Claude's monthly-active-user count grew 44% from March to April (the highest growth among major AI applications in that window), reaching 23 million.

These four vendors anchor the global volume index. Confidence on all four is "High" per Section 3.2. The remaining 17 vendors collectively account for the residual 12% of volume.

## 4.6 Dynamic Findings

Three vendor-level dynamics in the April 1 – May 9 window are worth highlighting:

**Kimi (Moonshot AI) is the fastest-growing vendor**, climbing from 1.54T per day on April 6 to 2.5T per day on May 9 — a 62% increase over 33 days. Three causes compound: the K2.6 model launch on April 20 (1 trillion total parameters in a Mixture-of-Experts architecture, 262K context window, performance tied with GPT-5.5 on SWE-Bench Pro at 80% lower cost); annual recurring revenue doubling from $100 million in March to $200 million in April; and a $2 billion funding round closing May 6 at a $20 billion post-money valuation. Kimi K2.6 is now the second-most-trafficked model on OpenRouter weekly, at 1.85 trillion tokens.

**Grok (xAI) is the first negative-growth vendor in GATT's history**, falling from 0.65T per day on April 6 to 0.55T on May 9 — a roughly 15% decline. Three causes: monthly active users dropped 12.5% from March to April (per Similarweb), with Grok tumbling from second to fifth place in global mobile app rankings; Claude (+44%) and Gemini (+19%) gained share at Grok's expense; and 80+ staff including several co-founders departed xAI per Fast Company reporting. The growth-rate assumption was flipped from +15% per month to -5% per month in v0.81.

**OpenRouter passed 3 trillion tokens per day** in v0.81's third-party data sweep, a 136% upward revision from v0.80's 1.27T estimate. The revision was driven by the a16z and OpenRouter "100 Trillion Token Study" [5] confirming the platform passed 1 trillion tokens per day in December 2025, and OpenRouter's April 2026 disclosure of 20 trillion tokens per week — a 4× year-over-year increase. The OpenRouter row is reported with an explicit aggregator overlap note (Section 3.1); its volume is not additive to the global total.

These dynamics — one vendor accelerating to 30% per month, one vendor declining at -5% per month, and one aggregator passing a measurement milestone — span the range of behavior the index needs to capture. The next section returns to the central question with which the paper opened: how to reconcile this empirical picture with the physics-grounded ceiling of Litowitz, Polson, and Sokolov (2026).
