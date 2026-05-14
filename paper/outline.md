# Paper Outline

**Title:** Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference

**Author:** Frank Gao (independent researcher)

**Length target:** ~8,000 words + references + appendices

**arXiv categories:** cs.CY (Computers and Society) primary, econ.GN cross-list

---

## Abstract (~250 words)
- Hook: 2.04× tension between GATT empirical (459.7K tokens/US person/day, May 2026) and Litowitz et al. 2028 physical ceiling (225K)
- Three reconciliation interpretations
- Contribution: first global, all-sources, daily token throughput index across 21 vendors
- Method: tiered confidence model + extrapolation engine + Token GDP normalization
- Headline findings: 310T/day global; CN/US 50/50 volume parity; US 88% Token GDP; 597× US-India per-capita gap

## 1. Introduction (~1000 words)

### 1.1 The Measurement Gap
Existing AI economic measurement falls into three buckets:
- USD-priced (IDC infra spending, Gartner total AI spending) — useful for budgeting, blind to volume
- Single-jurisdiction (IDC China MaaS report — only China, only external)
- Single-platform (a16z/OpenRouter 100T study — aggregator only)
- Training-FLOPs (Epoch AI) — different unit, doesn't capture inference

None measures **global, all-sources, daily token throughput**.

### 1.2 The 2× Discrepancy
Open with the Litowitz/Polson/Sokolov (2026) 2028 ceiling vs GATT v0.82 May 2026 empirical:
- 225K tokens/US person/day (paper) vs 459.7K (GATT) = 2.04× ratio
- Whichever interpretation is correct, this is a methodologically important conversation

### 1.3 Contributions
This paper:
1. Introduces GATT — a daily empirical index of global AI inference token throughput
2. Documents an all-sources scope methodology (vs IDC's external-MaaS-only)
3. Surfaces and reconciles a 2× discrepancy with the physics-ceiling literature
4. Proposes "Token GDP" as a regional-comparable economic-value metric

### 1.4 Roadmap
Sec 2 places GATT in the existing literature. Sec 3 details methodology. Sec 4 reports empirical findings. Sec 5 reconciles with the physical ceiling. Sec 6 discusses policy implications. Sec 7 concludes.

---

## 2. Related Work (~1500 words)

### 2.1 Commercial Research (USD-priced)
- IDC Worldwide AI Infrastructure Tracker — $758B by 2029, US 76%/CN 11.6%
- Gartner Worldwide AI Spending — $1.5T 2025, $2T 2026 forecast
- Both useful for capex/opex; blind to volume

### 2.2 Token-Volume Research (sparse)
- IDC China Public Cloud MaaS report (May 7, 2026) — China-only, external-MaaS-only, 1,944T/year 2025
- Caixin / Volcengine official disclosures — vendor-specific
- a16z + OpenRouter "100T Token Study" (arXiv 2601.10088, Jan 15 2026) — aggregator-only

### 2.3 Physics & Economics of Inference
- **Litowitz, Polson, Sokolov (2026, arXiv 2603.06630)** — physics ceiling
- Xing (2026, arXiv 2603.21690) — token futures market
- Zhuang et al. (2025, arXiv 2510.26136) — LLM Inference Production Frontier
- Inference Bottleneck (arXiv 2604.17431) — methodological template

### 2.4 Empirical Comparison Studies
- Cross-Platform User Survey (arXiv 2603.25220) — 388 users, multi-home >80%
- TokenPowerBench (arXiv 2512.03024) — energy per token

### 2.5 Where GATT fits
GATT occupies a unique position: empirical, global, all-sources, daily, free. No competitor combines these properties.

---

## 3. Methodology (~2000 words)

### 3.1 Vendor Coverage (21 vendors, May 2026)
- Top 10 detail (Doubao, Gemini, OpenAI, Anthropic, DeepSeek, Microsoft, Qwen, OpenRouter, Hy3, Kimi, Ernie)
- Tier classification (1: official disclosure / 2: estimated)

### 3.2 Confidence Hierarchy
- High: direct vendor disclosure, ≤30 days old
- Medium: corroborated indirect (ARR / queries × tokens-per-query)
- Low: single proxy signal
- Note: planned v0.83 adoption of observed/inferred/judgment classification (per arXiv 2604.17431)

### 3.3 All-Sources Scope (vs IDC)
- GATT counts: external API + internal first-party (e.g., Douyin AI Search, Doubao App, Jimeng) + consumer apps + on-device
- IDC counts: external public-cloud MaaS only
- Worked example: Volcengine 120T/day all-sources vs ~2.64T/day external MaaS = >95% internal

### 3.4 Extrapolation Engine
- Each vendor's daily value = source_value × (1 + monthly_growth)^(days_since_source / 30)
- Live recomputed from snapshot file in browser
- Caps and adjustments when vendor-specific signals (e.g., Grok MAU drop) override extrapolation

### 3.5 Token GDP
- Token GDP = Σ (vendor_volume × regional_blended_price)
- Pricing: US ~$1.50/M, EU ~$1.20/M, CN ~$0.10/M, ROW ~$0.90/M
- Caveat: pricing fell 40× from 2023 to 2025 (Xing 2026); blended figures are point-in-time

### 3.6 Per-Capita Calculation
- Country tokens / population
- 12 countries tracked

### 3.7 Revision Discipline
- Every vendor entry has `revision_history` array
- Public correction log
- Open data (CC BY 4.0)

---

## 4. Empirical Findings (~1500 words)

### 4.1 Global Volume (May 9, 2026)
- 310T tokens/day
- Year-over-year growth: ~22%/mo, doubling every ~3.5 months
- Year-end 2026 projection: 1.1-1.5 petatokens/day

### 4.2 Volume Parity
- China 50% (153.92T/day), US 49.7% (154.62T/day), EU 0.24%, ROW residual
- Volume gap closed from 58/35 (April 6) to 50/50 (May 9) as US hard data accumulated

### 4.3 Token GDP Asymmetry
- US 88%, China 6%, EU 4%, ROW 2%
- 15× pricing gap between US and Chinese vendors persists
- Annualized $95.8B globally

### 4.4 Per-Capita Inequality
- US 459.7K, China 110K, India 0.77K
- US/India = 597× — wider than the income divide
- Widened from 448× one month ago

### 4.5 Top Vendor Findings
- Doubao 132T (43% global share, all-sources)
- Gemini 73T (Pichai 16B tokens/min × 3.2 All Surfaces multiplier)
- OpenAI 45T, Anthropic 22T
- Cross-validated against IDC May 7 (Volcengine 49.5% China MaaS)

### 4.6 Dynamic Findings
- Kimi K2.6 fastest-growing vendor (+62% in 5 weeks)
- Grok first negative-growth vendor (-15% in 5 weeks)
- OpenRouter aggregator passed 3T/day

---

## 5. The 2× Discrepancy with Photons = Tokens (~1000 words)

### 5.1 Setup
GATT US per-capita = 459.7K (May 2026)
Litowitz et al. 2028 ceiling = 225K (under 326 TWh allocation)
Ratio = 2.04×

### 5.2 Interpretation 1: GATT may overestimate
- Gemini All Surfaces 3.2× multiplier — could double-count Search AI Overviews
- Doubao all-sources 132T — could include cached / replicated agent calls
- Estimated correction: ~10-15% downward

### 5.3 Interpretation 2: Paper's physical ceiling is conservative
- Landauer/Shannon assumes uniform GPT-4-level efficiency
- Real 2026 inference uses MoE (3% activation), 4-bit quantization, speculative decoding, ASICs
- Effective tokens/Joule could be 5-10× the baseline
- Estimated effective ceiling correction: ~5-10× upward

### 5.4 Interpretation 3: Different units
- GATT: empirical all-surface output (every token, including from cached prefixes, batched, multi-tenant)
- Paper: theoretical physical capacity assuming fresh compute per token
- Like "kWh delivered to outlet" vs "kWh of fuel input at plant"
- Both correct in their own units

### 5.5 Synthesis
- Interpretations 2 + 3 are most likely dominant
- Interpretation 1 contributes a smaller share
- Both numbers are correct in their own units; the conversation between empirical tracking and physical-bound modeling is the right way for token economy measurement to mature

### 5.6 Implications for Methodology
- v0.83 will publish sensitivity bands per arXiv 2604.17431 template
- Pricing as-of dates per Xing 2026 40× decline
- Production-frontier sensitivity per Zhuang et al. 2025

---

## 6. Discussion (~700 words)

### 6.1 Policy Implications
- Token volume parity ≠ AI parity (GDP gap)
- Per-capita rather than total-volume metrics for governance
- Token futures market (Xing 2026) needs an empirical index — GATT prototype

### 6.2 Geo-Economic Implications
- China's 50% volume share comes from internal-first-party usage; external MaaS is much smaller
- Export controls on inference chips operate on a 2× efficiency margin (per Photons=Tokens)
- 597× per-capita gap is the central Token Economy inequity

### 6.3 Limitations
- Vendor disclosure asymmetry — Chinese vendors disclose volume, US vendors disclose ARR
- Aggregator overlap (OpenRouter ↔ vendor totals)
- Pricing volatility (40× decline in 24 months per Xing 2026)
- Confidence still mostly "low"/"medium" outside top 5

### 6.4 Sovereign / Strategic-Resource Policy Trajectories (v1.5 NEW)
- Three trajectories: laissez-faire / regulated utility / state monopoly
- GATT signature discriminates between them; 36-month falsification window
- Fiscal-extraction worked illustration (5% token excise → $4.85B → $200B+)
- Sovereign Token Reserve hypothesis (analog to Strategic Petroleum Reserve)

### 6.5 Future Work
- v0.83: observed/inferred/judgment parameter classification + sensitivity bands
- v0.84: per-domain breakdowns (coding / chat / search / agent)
- v1.0: peer-reviewed methodology with reproducible data pipeline

---

## 7. Conclusion (~250 words)
- Recap: GATT is the first global, all-sources, daily token throughput index
- 2× tension with academic physical-ceiling literature is productive
- The Token Economy needs measurement infrastructure now, not later
- Open data + open methodology is the right approach
- Invitation to collaborate

---

## References (~30 citations)

**Token economy / inference economics:**
- Litowitz, Polson, Sokolov (2026) — arXiv:2603.06630
- Xing (2026) — arXiv:2603.21690
- Zhuang et al. (2025) — arXiv:2510.26136
- Inference Bottleneck (2026) — arXiv:2604.17431
- a16z + OpenRouter (2026) — arXiv:2601.10088
- Cross-Platform Survey (2026) — arXiv:2603.25220
- TokenPowerBench (2025) — arXiv:2512.03024

**Commercial research:**
- IDC China Public Cloud MaaS report (May 7, 2026) — news.qq.com / 163.com coverage
- IDC Worldwide AI Infrastructure Tracker — pr release
- Gartner AI Spending press release (Sep 2025)

**Vendor disclosures:**
- OpenAI 15B tokens/min (Mar 31, 2026) — openai.com/index/accelerating-the-next-phase-ai/
- Pichai 16B tokens/min (Apr 2026) — Google Cloud Next 2026
- Volcengine 120T/day (Apr 1, 2026) — Wuhan AI Innovation Expo
- Microsoft Q3 FY26 earnings (Apr 29, 2026)
- Anthropic Opus 4.7 (Apr 16, 2026) — anthropic.com/news
- DeepSeek V4 (Apr 24, 2026) — api-docs.deepseek.com/news
- Kimi K2.6 (Apr 20, 2026) — Moonshot AI

**Methodology:**
- Landauer's principle (Landauer 1961)
- Shannon channel capacity (Shannon 1948)
- MacKay's information accounting framework

---

## Appendices

### A. Full vendor list with confidence ratings (May 9, 2026)
- All 21 vendors with token volume, source date, confidence, scope notes

### B. Token GDP worked example
- Step-by-step calculation for one day
- Sensitivity to pricing assumptions
