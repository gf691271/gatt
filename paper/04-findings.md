# 4. Empirical Findings

This section reports headline findings from the GATT v1.5.2 dataset as of May 20, 2026 (post-Google-I/O 2026). All figures are reproducible from `data/tci-latest.json` (immutable v1.0 baseline at `data/snapshots/2026-05-09.json`; v1.3 vendor expansion, v1.4 methodology integration, and v1.5.2 Gemini I/O 2026 update layered in current). Where a figure depends on extrapolation between disclosures, the source date and growth-rate assumption are documented in the corresponding vendor entry's `revision_history`.

## 4.1 Global Volume

Global daily AI inference output stands at **345 trillion tokens per day** as of May 20, 2026 (post-Google-I/O 2026). The headline figure aggregates 24 tracked vendors across 12 countries (21 vendors at v1.0 publication state plus Apple Intelligence cloud-routed, Cohere, and Sarvam AI added in v1.3), with a small "Rest of World" residual covering geographies not yet broken out individually. Growth has run at approximately 22% per month over the preceding eight weeks — a doubling time of roughly 3.5 months. Extrapolating this rate forward through year-end 2026 yields a projection band of **1.2 to 1.4 quadrillion tokens per day** by December 2026, with the conservative end of the band assuming growth deceleration to 18% per month and the aggressive end assuming sustained 22% per month.

The 345T figure is itself the result of substantial recent revisions. GATT v0.79 (May 4, 2026) reported 264T per day; v0.80 raised this to 305T after seven vendor anchor upgrades reflecting Pichai's 16-billion-tokens-per-minute Q1 disclosure, Anthropic's Opus 4.7 launch and 44% MAU surge, Microsoft's Q3 FY26 $37B AI ARR earnings release, Kimi K2.6's launch and ARR doubling, DeepSeek V4 Pro/Flash's launch, and minor adjustments to Qwen and Hunyuan. v0.81 added 5 trillion tokens per day from third-party revisions (OpenRouter platform data, Perplexity user metrics, and the new Xiaomi MiMo entry); v1.3 added Apple Intelligence cloud-routed plus Cohere and Sarvam to reach 311T at v1.4 (May 11, 2026). **The v1.5.2 update on May 20, 2026 added 34 trillion tokens per day in a single keynote-grade disclosure**: Sundar Pichai's Google I/O 2026 opening keynote of May 19-20 [42] disclosed that Google now processes 3.2 quadrillion tokens per month across all surfaces — a 7× year-over-year increase from approximately 480 trillion/month at I/O 2025 — equivalent to roughly 107 trillion tokens/day, replacing v1.4's 73T composite. The April 1 to May 20 window was unusually rich in publishable signals; I/O 2026's structural twin disclosure (all-surfaces total plus API portion) is the most consequential of the window because it eliminates editorial-multiplier dependency from the largest US vendor's all-surfaces composite (§3.3 details).

### 4.1.1 Sensitivity Band on the Headline

The 345T point estimate carries methodological uncertainty that warrants explicit bracketing. Following the parameter classification template from Inference Bottleneck [12] (observed / inferred / judgment-based), GATT publishes three scenarios for the headline global figure:

| Scenario | Global daily tokens (T) | Methodology |
|---|---:|---|
| Conservative | 285 | Photons=Tokens-anchored: trim Doubao all-sources by 5% (cache adjustment); apply 15% reduction across vendors with low-confidence ratings; Gemini All-Surfaces no longer requires editorial trim (multiplier disclosed at I/O 2026 [42]) |
| **Best estimate** | **345** | **GATT v1.5.2 published values; vendor-volume-weighted, all-sources, May 20, 2026 anchored (post-I/O 2026)** |
| Aggressive | 450 | 22%/mo growth assumption holds through end-Q2 2026; assumes 1-2 additional Pichai-class US disclosures by mid-June |

The conservative bound (285T) maintains all five qualitative GATT findings — US volume lead post-I/O 2026 (US 55% / CN 45% in best; closer to parity 52/48 in conservative), US Token GDP dominance ≥87%, per-capita gap ≥550× US/India, growth trajectory positive, and the 2.5× tension with the Photons=Tokens 2028 ceiling persists (450K conservative US per-capita > 225K ceiling). A notable v1.5.2 update to the conservative bound: the Gemini All-Surfaces multiplier (formerly the principal candidate over-estimate vector flagged by Sokolov's v1.0 peer review) is now disclosed rather than editorial [42], so the v1.4-era conservative trim of 3.2× → 2.5× no longer applies. The qualitative robustness of GATT's headline claims to conservative recalibration is, in our judgment, the strongest argument for citing GATT figures despite the unavoidable measurement uncertainty in the underlying vendor data.

## 4.2 Volume Parity Between China and the United States — Broken at I/O 2026

The China-US token-volume parity established at v0.81 (January 2026) and held through v1.4 (May 11, 2026) **broke at Google I/O 2026 on May 19-20, 2026**. As of May 20 (post-v1.5.2 Gemini upgrade): **United States 55% of global volume (190 trillion tokens per day, of which 188T attributable via the per-capita-tracked vendor base)**, **China 45% (154 trillion tokens per day)**, with Europe at ~0.21% (0.74 trillion, dominated by Mistral and Cohere) and the Rest of World residual at the remainder. The United States is now 36 trillion tokens per day ahead of China, a margin established by a single Pichai keynote disclosure (3.2 quadrillion Gemini tokens/month all-surfaces [42], lifting Gemini 73T → 107T).

The parity history is instructive. On April 6, 2026, GATT v0.75 measured China at 58% and the United States at 35%. The 5-week shift to 50/50 in early May 2026 reflected new United States hard-data disclosures rather than slowed Chinese growth: Pichai's 16-billion-tokens-per-minute Cloud Next disclosure (a 60% quarter-over-quarter increase from Q4 2025's 10 billion) raised Gemini's All Surfaces estimate from 57T to 73T; Microsoft's Q3 FY26 disclosure of $37 billion AI business ARR (+123% year-over-year) and 20 million paid Copilot seats raised Microsoft's estimate from 8.1T to 10T; OpenAI's GPT-5.5 launch (April 23) and GPT-5.5 Instant rollout (May 5) raised OpenAI's estimate from 40T to 45T; Anthropic's Opus 4.7 launch (April 16, with a new tokenizer producing up to 35% more tokens per equivalent input) plus 44% Claude monthly-active-user growth raised Anthropic from 15T to 22T. The I/O 2026 keynote then layered a second, larger US-side disclosure (Gemini 73T → 107T) on top of this already-fresh state, breaking the equilibrium to US 55% / CN 45%. China's leaders held steady on extrapolation through the same I/O 2026 window, with no comparably large new disclosures during May 13–20.

The 50/50 volume parity is the headline geo-economic finding *for v0.81 through v1.4*. The v1.5.2 finding (post-I/O 2026) is volume *near-parity* with a US lead of 10 percentage points and growing. Both observations are durable insights: the 50/50 parity established that capacity has converged across the two jurisdictions; the parity break establishes that *single disclosures can move the index by 5-10 percentage points overnight*, an operational risk for any tracker running against a quarterly-disclosing supply side. Neither observation implies economic parity — see Section 4.3.

## 4.3 Token GDP Asymmetry

Daily Token GDP — vendor volume × regional blended price (Section 3.5) — totals **$316.7 million per day** ($115.6 billion annualized) post-I/O 2026. The regional split widens beyond v1.4's already-asymmetric structure:

- **United States: $285 million per day, 90% of global Token GDP, on 55% of volume.**
- **China: $15.4 million per day, 5% of global Token GDP, on 45% of volume.**
- Europe: $10.8 million per day, 3% of Token GDP, on 0.21% of volume.
- Rest of World: $5.6 million per day, 2% of Token GDP, on 1.8% of volume (post-v1.3 Cohere + Sarvam additions).

The driver is a 15× pricing gap between United States and Chinese vendors. Anthropic's Opus 4.7 prices at $5 per million input tokens and $25 per million output (a blend of approximately $7.50 per million); GPT-5.5 prices at $5/$30 per million ($8 blended); Doubao prices at approximately $0.10 per million blended; DeepSeek V4 Pro at $0.145 input / $1.74 output. The break of 50/50 volume parity to 55/45 (§4.2) compounds with the unchanged 15× pricing gap to produce economic value at 90/5 — sharpening the central paradox of the May 2026 Token Economy: pre-I/O the asymmetry was 50/50 volume against 88/6 GDP (a 15× pure-pricing leverage); post-I/O it is 55/45 volume against 90/5 GDP (the same 15× pricing leverage *plus* a 10-point volume gain for the higher-priced jurisdiction). Token GDP grew faster than volume in v1.5.2 (+19% versus +11%) precisely because the incremental 34T from Gemini all flow through the US frontier-pricing tier at $1.50/M.

This finding has implications for governance. Token-volume *near-*parity (post-I/O 2026 it is no longer parity simpliciter) is consistent with claims of Chinese AI parity at the *capacity* level, but the 90/5 GDP split shows that capacity does not equal economic value. Conversely, the United States now leads on *both* dimensions — a stronger structural position than at v1.4. Both observations are durable: the pricing gap has held at roughly 15× across the past year, despite substantial Chinese-vendor pricing pressure.

## 4.4 Per-Capita Inequality

Dividing country tokens by national population produces the AI-inequality findings:

- **United States: 561,200 tokens per resident per day** (rank 1, up from 459,700 at v1.4 following the Pichai I/O 2026 Gemini All-Surfaces upgrade [42])
- **China: 110,000 tokens per resident per day** (rank 2)
- United Kingdom: 59,700 (rank 3)
- France: 35,300 (rank 4)
- Canada: 29,000 (rank 5)
- Germany: 26,200 (rank 6)
- South Korea: 24,400 (rank 7)
- Japan: 14,900 (rank 8)
- Saudi Arabia: 14,000 (rank 9)
- Brazil: 4,600 (rank 10)
- Indonesia: 940 (rank 11)
- India: 770 (rank 12)

The headline ratio is **United States to India = 729×**. As recently as April 6, 2026, this gap stood at 394×; six weeks later it has widened to 729× — far faster than absolute United States token growth alone, because the United States per-capita base is leveraging upward via product launches, tokenizer changes, and the I/O 2026 keynote disclosure, while India's per-capita base is barely moving from 0.66K to 0.77K over the same window. The gap is wider than the corresponding income ratio (approximately 30× by GDP per capita) and substantially wider than the digital-divide gap measured by mobile or internet penetration. We treat this as the most striking inequality finding in the dataset, and note that the v1.5.2 step-change (597× → 729× in roughly five days) reflects the sensitivity of the metric to single-vendor disclosures concentrated in the higher-per-capita jurisdiction.

### 4.4.1 Distributional Summary: Gini and Lorenz

The 729× United States-India ratio is a single-pair statistic. To summarize the full distribution, we compute the **population-weighted Gini coefficient** and the implied Lorenz curve across the twelve countries broken out in the dataset (which collectively cover approximately 51% of global population; the unrepresented residual is mostly low-per-capita and would push the global Gini higher rather than lower). The reproducibility script is `paper/scripts/token_gini.py`.

The result (v1.5.2, post-I/O 2026):

| Measure | v1.4 (May 11) | v1.5.2 (May 20, post-I/O) |
|---|---:|---:|
| Population-weighted Gini coefficient (12 countries) | 0.674 | **0.698** |
| Top 10% of population's share of token consumption | 50.2% | **55.0%** |
| Top 1% of population's share | 6.0% | **6.6%** |
| Bottom 50% of population's share | 1.4% | **1.2%** |

For comparison: cross-country income Gini (PPP-adjusted, 2024 World Bank) is approximately 0.62; pre-tax US wealth Gini is approximately 0.85. **Token consumption inequality has already exceeded global income inequality and is now meaningfully closer to wealth-distribution levels of concentration.** The Gini stepped from 0.674 to 0.698 in a single Pichai keynote — the v1.5.2 update made the metric 36% of the way to US-wealth-Gini-style concentration (0.674 → 0.698 against a 0.62 → 0.85 reference span). This is consistent with Crawford [19]'s framing of AI infrastructure as a planetary-scale system whose access concentrates among a small number of populations and regions; the Gini number is the empirical scalar form of that concern.

The Lorenz curve (formal computation in the script) shows a sharp inflection at the China-US transition: the bottom 92% of the represented population (everyone outside the United States) collectively accounts for 45% of token volume, while the top 8% (the United States) accounts for the remaining 55%. This is the structural consequence of the post-I/O 2026 US 55% / CN 45% volume split combined with China's 4.2× larger population — a sharper inflection than v1.4's 48/52 split (which corresponded to the 50/50 volume parity).

**A caveat on interpretation.** The Gini above captures *vendor-attributed* per-capita consumption; it does not measure individual-level consumption within countries (which would require a wholly different data source, since GATT cannot observe per-user activity). Within-country distribution may also be highly unequal: a small fraction of US users likely accounts for a disproportionate share of US token volume. The 0.698 figure therefore *under*-states the true individual-level Gini, possibly substantially. We flag a within-country decomposition as future work but emphasize that even the conservative cross-country measurement establishes that token consumption is more unequally distributed than income at the global scale — already, in 2026, before the technology is broadly diffused.

## 4.5 Top Vendor Findings

The top four vendors account for **87% of global volume**:

- **Doubao (ByteDance, China): 129 trillion tokens per day**, 37% of global. All-sources scope including external Volcengine MaaS, Douyin AI Search, the Doubao consumer app, the Jimeng image-generation pipeline, and internal Volcengine workflows. The May 7, 2026 IDC China Public Cloud MaaS report independently confirms Volcengine #1 in China at 49.5% market share for full-year 2025 [4]. The all-sources vs. external-MaaS scope reconciliation is detailed in Section 3.3.

- **Gemini (Google, All Surfaces): 107 trillion tokens per day**, 31% of global. Anchored in Sundar Pichai's Google I/O 2026 opening keynote of May 19-20 [42], which disclosed both the all-surfaces total (3.2 quadrillion tokens/month, equivalent to roughly 107 trillion/day) and the API portion (19 billion tokens/minute = 27.4 trillion/day) — a 7× year-over-year jump from approximately 480 trillion/month at I/O 2025. The implied All-Surfaces multiplier 3.9× is now disclosed via the twin numbers rather than chosen editorially, resolving Sokolov's v1.0 peer-review critique of v1.4's editorial 3.2× multiplier. Pichai also disclosed that internal Gemini 3.5 Flash usage exceeds 3 trillion tokens/day, doubled every few weeks from 0.5 trillion/day in March 2026, with 8.5 million developers building monthly. Section 5 retains the v1.4-era over-estimate discussion for vendors whose all-surfaces composites have not been independently disclosed; for Gemini specifically, the multiplier dependency is closed.

- **OpenAI (ChatGPT and API): 45 trillion tokens per day**, 15% of global. Anchored in the March 31, 2026 official disclosure of "more than 15 billion tokens per minute" across the OpenAI API, supplemented by consumer-side activity (2.5 billion ChatGPT prompts per day, 9 million paid business users) and the GPT-5.5 / GPT-5.5 Instant launches in late April and early May.

- **Anthropic (Claude): 22 trillion tokens per day**, 7% of global. The Opus 4.7 launch on April 16, 2026 introduced a tokenizer producing up to 35% more tokens per equivalent input — a direct lift to GATT's volume estimate. Claude's monthly-active-user count grew 44% from March to April (the highest growth among major AI applications in that window), reaching 23 million.

These four vendors anchor the global volume index. Confidence on all four is "High" per Section 3.2. The remaining 17 vendors collectively account for the residual 12% of volume.

## 4.6 Dynamic Findings

Three vendor-level dynamics in the April 1 – May 9 window are worth highlighting:

**Kimi (Moonshot AI) is the fastest-growing vendor**, climbing from 1.54T per day on April 6 to 2.5T per day on May 9 — a 62% increase over 33 days. Three causes compound: the K2.6 model launch on April 20 (1 trillion total parameters in a Mixture-of-Experts architecture, 262K context window, performance tied with GPT-5.5 on SWE-Bench Pro at 80% lower cost); annual recurring revenue doubling from $100 million in March to $200 million in April; and a $2 billion funding round closing May 6 at a $20 billion post-money valuation. Kimi K2.6 is now the second-most-trafficked model on OpenRouter weekly, at 1.85 trillion tokens.

**Grok (xAI) is the first negative-growth vendor in GATT's history**, falling from 0.65T per day on April 6 to 0.55T on May 9 — a roughly 15% decline. Three causes: monthly active users dropped 12.5% from March to April (per Similarweb), with Grok tumbling from second to fifth place in global mobile app rankings; Claude (+44%) and Gemini (+19%) gained share at Grok's expense; and 80+ staff including several co-founders departed xAI per Fast Company reporting. The growth-rate assumption was flipped from +15% per month to -5% per month in v0.81.

**OpenRouter passed 3 trillion tokens per day** in v0.81's third-party data sweep, a 136% upward revision from v0.80's 1.27T estimate. The revision was driven by the a16z and OpenRouter "100 Trillion Token Study" [5] confirming the platform passed 1 trillion tokens per day in December 2025, and OpenRouter's April 2026 disclosure of 20 trillion tokens per week — a 4× year-over-year increase. The OpenRouter row is reported with an explicit aggregator overlap note (Section 3.1); its volume is not additive to the global total.

These dynamics — one vendor accelerating to 30% per month, one vendor declining at -5% per month, and one aggregator passing a measurement milestone — span the range of behavior the index needs to capture. The next section returns to the central question with which the paper opened: how to reconcile this empirical picture with the physics-grounded ceiling of Litowitz, Polson, and Sokolov (2026).
