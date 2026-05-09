# 5. The 2× Discrepancy with Photons = Tokens

This section returns to the question that opened the paper. Litowitz, Polson, and Sokolov [1] project that the 2028 United States AI energy allocation of 326 TWh can support roughly 6.5 × 10¹⁷ tokens per year, equivalently 225,000 tokens per resident per day. GATT v0.82 measures United States per-capita throughput at 459,700 tokens per resident per day in May 2026 — eighteen months *before* the paper's projection date, yet **2.04× above the paper's 2028 ceiling**.

Both numbers are produced carefully. We argue that the gap reflects three compounding factors, each of which can be quantified, and that the *informative* interpretation of the discrepancy is methodological complementarity rather than measurement error.

**This section is offered as a falsifiable hypothesis for joint refinement, not as a closed argument.** GATT v1.0 has been substantially revised in response to peer review from the Litowitz-Polson-Sokolov co-author team itself; we acknowledge the resulting decomposition is under-identified (three latent factors against one observable) and report a Bayesian sensitivity analysis (Appendix C) rather than a unique solution. Section 5.5.7 below proposes specific empirical measurement work — a co-authored energy-per-token benchmarking study on representative 2026 inference deployments — as the natural next step for jointly tightening the parameter ranges. The *companion paper* framing of this manuscript is real: this section is the pitch document for that collaboration.

## 5.1 Restating the Discrepancy

The Litowitz et al. ceiling derives from three inputs: a 326 TWh US AI energy allocation projected for 2028, Landauer's information-theoretic minimum energy cost per bit, and a Shannon-channel capacity calibration anchored to GPT-4-class inference efficiency. Their token-budget framework is rigorous within these assumptions and produces a meaningful upper bound on token production under fixed inputs. The 225,000 tokens-per-resident-per-day figure is the per-capita normalization of their aggregate ceiling under 2028 US population estimates.

The GATT empirical figure derives from twenty-one vendor-level estimates summed into a national total, divided by US population. Each vendor estimate is anchored in a dated source signal — a vendor disclosure, an ARR-and-pricing back-calculation, or platform-aggregator data — and updated via the extrapolation engine described in Section 3.4.

The two figures are not measuring the same physical quantity. We now develop three reconciliation interpretations, each accounting for some portion of the 2× ratio.

## 5.2 Interpretation 1 — GATT May Overestimate Top Vendors

GATT's largest United States vendor-attribution decisions involve interpretation, not direct disclosure. Most consequentially, Google's "Gemini All Surfaces" estimate of 73 trillion tokens per day applies a 3.2× multiplier to the 23-trillion-tokens-per-day figure derived from Pichai's "more than 16 billion tokens per minute via direct API" disclosure. The multiplier covers Search AI Overviews, the Gemini App's 750 million monthly active users, and Workspace integrations. If the multiplier double-counts tokens emitted by interface layers that share underlying API infrastructure, the All Surfaces figure could be high by 15-25%. Trimming Gemini from 73T to 60T would reduce US daily volume by roughly 13 trillion tokens, lowering US per-capita by approximately 39,000 tokens per resident per day.

Anthropic's Opus 4.7 tokenizer change (Section 4.5) is more straightforward — Anthropic confirms the new tokenizer produces up to 35% more tokens per equivalent input — but this raises a related concern: tokens are now a less stable measurement unit across models. A 35% increase in tokens for unchanged work is not a 35% increase in compute or value.

Combining Gemini-multiplier compression and tokenizer-inflation correction produces a conservative US per-capita estimate around 410,000-430,000 tokens per resident per day, still 1.8-1.9× above the 2028 physical ceiling. Interpretation 1 alone cannot close the gap.

## 5.3 Interpretation 2 — The Physical Ceiling Calibration is Conservative

The Litowitz et al. framework itself is not dated — Landauer's principle and Shannon channel capacity are thermodynamic and information-theoretic bounds that hold across any technological era. What we propose is that the *calibration* of tokens-per-Joule that anchors the 2028 projection was set against early-2024 GPT-4-class deployment patterns, and that 2026 production inference operates measurably above that calibration baseline. The framework remains valid; the calibration inputs deserve updating.

Four mechanisms produce inference-stack efficiency above a 2024 dense-FP16 baseline. Each must be characterized carefully — naive headline multipliers from each mechanism overstate the realized efficiency lift in production.

**Mixture-of-Experts (MoE) sparse activation.** DeepSeek V4 Pro activates 49B of 1.6T parameters (~3%); Tencent's Hy3 activates 21B of 295B (~7%); Kimi K2.6 activates 32B of 1T (~3.2%). The naive arithmetic — that activating 3% of parameters does 33× less parameter-touching work — applies only to the expert-FFN component of inference cost. Attention runs over the full sequence and head dimension regardless of expert routing. On the long-context workloads characteristic of modern reasoning models (Kimi K2.6's 262K context, DeepSeek V4 Pro's 1M context), attention can dominate over expert-FFN computation. The effective tokens-per-Joule lift from MoE in a mixed long-and-short-context production environment is approximately **2-4×**, not the 10-30× implied by the activation ratio alone.

**4-bit quantization.** Production deployments using GPTQ, AWQ, or DeepSeek-style quantization stacks reduce weight memory footprint by 4×. However, the practical throughput gain is more modest because (a) KV-cache is typically maintained at FP8 or BF16 for numerical stability, (b) dequantization adds compute overhead that partially offsets bandwidth savings, and (c) batch-size effects mean the bandwidth advantage is fully realized only at certain batch geometries. Empirical wall-clock throughput gains from vLLM and TensorRT-LLM benchmarks on H100-class hardware show **2-2.5× improvement** versus FP16 in production-realistic conditions, not the headline 4× memory reduction.

**Speculative decoding.** The published 2-3× throughput multiplier is workload-dependent. Speculative gains are highest on predictable, low-entropy outputs (code completion, templated responses) where draft-model acceptance rates exceed 70%. For reasoning-heavy outputs — which constitute approximately 31% of GATT-tracked traffic per the v0.87 reasoning_split block — acceptance rates drop below 50-60%, and effective speculative gains shrink to **1.2-1.5×**. The blended gain across the volume mix is approximately **1.5-2×**, not the 2-3× peak.

**Dedicated inference ASICs.** Groq LPUs, Google TPU 8th-generation, and the inference-optimized stacks deployed by ByteDance and Xiaomi achieve substantial efficiency gains on workloads matched to their architectural assumptions: fixed-batch, decode-heavy, mid-size models. Public benchmarks support **3-5× watts/token improvement on optimized decode workloads**, with significantly smaller advantages on prefill-dominated long-context workloads. The blended advantage across representative production mixes is closer to 3× than to the 5-10× peak claimed in vendor marketing.

**Composing the factors.** The four mechanisms are not statistically independent. Quantization reduces memory bandwidth pressure that ASIC architectures are also designed to alleviate. MoE sparse activation overlaps with the workload assumptions baked into ASIC efficiency claims. Speculative decoding gains and KV-cache reuse both exploit output predictability. Naively multiplying the per-factor multipliers (2-4 × 2-2.5 × 1.5-2 × 3-5) produces a range of approximately 18× to 200× — clearly an overstatement, since real systems cannot compound efficiency multipliers without architectural penalties. The conservative compositional discount captures the *dominant* factor (whichever provides the largest single architectural advantage on a given workload mix) plus modest additional contributions from the others. We estimate the resulting effective ceiling-recalibration multiplier at **2.5-3× central, with plausible range 2× to 4×** for representative 2026 deployment mixes. This is materially less than the "5-10×" earlier drafts of this section claimed, in deference to Sokolov's critique that compounding efficiency multipliers without architectural penalties is not how real production systems behave, and Litowitz's critique that the framework's structural validity must not be conflated with calibration-input updates.

## 5.4 Interpretation 3 — Different Units of Measurement

The third interpretation is the cleanest and the most likely. GATT measures **emitted tokens** — every token delivered to a user surface, regardless of the compute pathway. The Litowitz et al. paper models **fresh-compute tokens** — tokens that actually traverse the full inference pipeline.

Production inference systems extensively reuse compute. Prefix caching (KV-cache hits) means a substantial fraction of a typical conversation's tokens are emitted without re-running attention over the cached prefix. Cache hit rates of 30-50% are routinely reported in production deployments — particularly for chat applications where users iterate on the same context. Batched inference shares attention computation across simultaneous tenants. Multi-tenant agent loops emit tokens that, from the operator's view, represent reused work.

These efficiency gains are real but invisible to a physics-ceiling computation that budgets Joules per emitted token. They are equally invisible to a tokens-per-Joule efficiency optimization that asks "how can we make each computation more efficient" rather than "how can we avoid the computation entirely."

The closest analogy is the distinction between **kilowatt-hours delivered to consumer outlets** and **kilowatt-hours of fuel input at the power plant**. Power-plant efficiency, transmission losses, and demand-side measurement all separate the two. Both are valid quantities; the ratio between them is informative but not a critique of either.

We estimate that prefix-caching and batching collectively produce a 1.5-2× multiplier between fresh-compute tokens and emitted tokens in current production systems. This multiplier alone closes a substantial portion of the GATT-vs-paper gap.

## 5.5 Synthesis: A Quantitative Decomposition

The previous three subsections each describe a candidate explanation for the 2.04× discrepancy. This subsection attempts a more rigorous accounting. We are not claiming to *uniquely identify* the contribution of each interpretation; the data does not yet permit that. We are claiming that **plausible parameter ranges within each interpretation, when combined, are sufficient to account for the observed 2.04×** without invoking measurement error in either methodology. The decomposition below is offered as a falsifiable hypothesis: each multiplier has a stated central value and range, and each can be empirically tightened by future work.

### 5.5.1 Reference Frame

We seek to explain why GATT's empirical $G$ = 459.7K tokens/US-resident/day exceeds the Litowitz-Polson-Sokolov 2028 physical ceiling $L$ = 225K by a factor of $G/L = 2.04$.

Decomposing:

$$
\frac{G}{L} = \underbrace{\frac{G}{G^{*}}}_{\text{Interp. 1}} \cdot \underbrace{\frac{L^{*}}{L}}_{\text{Interp. 2}} \cdot \underbrace{\frac{G^{*}}{L^{*}}}_{\text{Interp. 3}}
$$

where $G^{*}$ is "GATT corrected for overestimation" (the true emitted-token figure), $L^{*}$ is "the physical ceiling re-calibrated to 2026 deployment efficiency" (the corrected fresh-compute capacity), and $G^{*}/L^{*}$ is the emitted-vs-fresh-compute ratio (units adjustment). Solving for the multiplicative composition: each factor must combine to produce the observed 2.04 ratio.

### 5.5.2 Interpretation 1: GATT Overestimation Factor

Section 5.2 identified two principal sources of GATT overestimation: the Gemini All Surfaces multiplier (3.2× the API-disclosed throughput) and the Doubao all-sources scope (132T/day including internal first-party usage with possible cache replication).

Quantifying: trimming the Gemini multiplier from 3.2× to 2.5× reduces Gemini's contribution from 73T to 57T, a -16T effect on US daily volume. This is roughly 39K tokens/resident/day. Applying a separate 5% trim to the Doubao all-sources scope (cache-hit adjustment) reduces China's volume by 6.6T but does not affect US per-capita directly. The Anthropic tokenizer change (35% inflation per equivalent input) suggests Anthropic's nominal 22T may be 15-25% inflated relative to comparable-pre-tokenizer volume; trimming 17% reduces by 3.7T (11K tokens/resident/day).

Net US per-capita correction: -50K, yielding $G^{*} \approx$ 410K. This is a corrective factor of $G/G^{*} = 459.7 / 410 \approx 1.12$ (12% overestimation, central estimate). Plausible range: 1.05 to 1.20.

### 5.5.3 Interpretation 2: Physical-Ceiling Recalibration Factor

Section 5.3 details the four mechanisms (MoE sparse activation, 4-bit quantization, speculative decoding, dedicated inference ASICs) by which 2026 inference operates above an early-2024 dense-FP16 calibration baseline, with each mechanism's per-factor multiplier carefully tightened from headline marketing claims to production-realized effective values: MoE 2-4×, quantization 2-2.5×, speculative decoding 1.5-2× (blended), ASICs 3× blended.

The compositional discount is the methodological crux. Naive multiplication of the per-factor ranges produces a product spanning 18× to 200× — clearly impossible in practice, since real production systems cannot compound efficiency multipliers without architectural penalties. The substantive question is which factor dominates on a representative production workload mix.

Our compositional assumption is that each workload pattern is dominated by one architectural advantage at a time: long-context reasoning workloads benefit primarily from MoE sparse activation (~2-4×) with secondary contributions from speculative decoding (~1.2-1.3×) and quantization (~2×). Decode-heavy chat workloads benefit primarily from ASIC efficiency (~3×) plus speculative decoding (~1.5-2×). Across the workload mix, the dominant-factor-plus-secondary contribution produces an effective ceiling-recalibration multiplier of **2.5-3× central, with plausible range 2× to 4×**. Specifically: $L^{*}/L = 2.5$ at the conservative end (where MoE attention dominance + reasoning workload mix limits speculative gains), 3.0 central, and 4.0 at the aggressive end (where ASIC-optimized decode workloads compound with quantization on chat-heavy traffic).

At the 2.5× central, the corrected ceiling is $L^{*}$ = 562K tokens/resident/day; at 3×, 675K; at 4×, 900K. All exceed the GATT empirical 460K, but with much narrower margins than the earlier 5-10× range claimed, which is appropriate given Sokolov's correction to the per-factor multipliers and Litowitz's reminder that the framework's structural validity is not dated.

### 5.5.5 Combined Decomposition

After the per-factor tightening, the decomposition table reads:

| Factor | Central | Low | High | Source revision |
|---|---:|---:|---:|---|
| Interp. 1 (G/G*) | 1.12 | 1.05 | 1.20 | unchanged |
| Interp. 2 (L*/L) | 3.0 | 2.0 | 4.0 | tightened from 4× per Sokolov engineering correction |
| Interp. 3 (G*/L*) | 1.4 | 1.25 | 1.65 | tightened from 1.54× per Sokolov / batching exclusion |

The decomposition is fundamentally under-identified — three latent factors, one observable (G/L = 2.04). We acknowledge this directly. Section 5.5.6 falsification conditions and Appendix C Bayesian sensitivity analysis together constrain the joint parameter space rather than uniquely identifying a single solution. Polson is right that consistency-checking is not identification; the appropriate methodological honesty is to report the *posterior over the joint factor space* given the observable, which Appendix C does formally.

What we can say without unique identification: the corrected ceiling at central values is $L^{*} = L \cdot 3 = 675$K tokens/resident/day. Converting to emitted-token-equivalent capacity using the Interpretation 3 multiplier: $L^{*} \cdot (G^{*}/L^{*}) = 675 \cdot 1.4 = 945$K. The corrected GATT estimate is $G^{*} = G / 1.12 = 410$K. The empirical 2026 utilization is therefore 410/945 ≈ 43% of the recalibrated emitted-equivalent ceiling.

A reader who finds 43% utilization implausibly high or low can adjust the Interpretation 2 factor accordingly: at $L^{*}/L = 2$ (conservative), the ceiling becomes 450K and utilization is 91%; at $L^{*}/L = 4$ (aggressive), the ceiling is 1260K and utilization is 33%. The 91% figure at the conservative bound is a meaningful constraint — it implies that under the most modest assumptions about ceiling recalibration, the 2026 AI economy is operating very near its effective capacity, which has implications for capital-expenditure sensitivity and is consistent with the $602B 2026 hyperscaler capex behavior. The 33% figure at the aggressive bound implies substantial headroom and is consistent with continued expansion through 2027.

**Removing the unprincipled overlap correction.** Earlier drafts of this section divided the combined product 1.12 × 4 × 1.54 by 4 to recover the observed 2.04 ratio. Litowitz, Polson, and Sokolov independently flagged this as unprincipled — Polson noted correctly that it inserted a free parameter to close the gap; Litowitz called it "the algebraic cleanup move that obscures rather than resolves the overlap"; Sokolov noted the suspicious self-cancellation. We have removed the /4 correction. Instead, we acknowledge that the three Interpretations are not statistically independent — Interpretation 2's ASIC efficiency factor partially overlaps with Interpretation 3's compute-reuse mechanism, since both exploit workload-pattern predictability — and we model this overlap explicitly in the Appendix C Bayesian analysis via correlation coefficient $\rho = 0.4$ between the L*/L and G*/L* factors. The combined product 1.12 × 3.0 × 1.4 ≈ 4.7 is therefore the *upper-bound* combined effect under the false assumption of independent factors. The Appendix C posterior under explicit correlation centers near 2.07, consistent with the observed 2.04 within a tight credibility band.

The 2.04× headline ratio is consistent with:
- GATT being modestly inflated (~12% high)
- The Litowitz-Polson-Sokolov ceiling being conservatively calibrated to early-2024 hardware (~3× central, plausible 2-4×)
- A ~1.4× units-of-measurement wedge between emitted and fresh-compute tokens (cache-hit dominant)

No combination requires either methodology to be in error — both are internally consistent within their stated frames. The discrepancy reflects the gap between (a) a 2028 fresh-compute physical ceiling calibrated to early-2024 efficiency and (b) a 2026 emitted-token empirical measurement, with the gap fully explainable by realistic 2026-vintage inference-stack efficiency improvements operating *within* the Litowitz-Polson-Sokolov framework.

### 5.5.6 Falsification Conditions

The decomposition is a falsifiable hypothesis. The earlier draft of this section listed thresholds (cache hit rates below 20%, efficiency gains below 2×) calibrated to the *extreme* tail of the plausible parameter space, which Litowitz noted correctly was decorative rather than constraining. The revised conditions below tighten the falsification thresholds to the *plausible center* of each parameter's range, making the test scientifically meaningful rather than rhetorical.

The decomposition is rejected if **any of the following three conditions hold simultaneously with the others**:

- **Cache-hit rates on the four largest GATT vendors below 30% (not 20%).** A direct measurement of effective compute reuse below 30% would shrink Interpretation 3 to ≤1.30 and require Interpretation 2 to absorb most of the gap. This threshold sits at the conservative edge of our 20-35% adopted range, which means measurements below 30% are not extraordinary outcomes — they are within the band where the decomposition starts to strain.
- **Per-token energy on representative 2026 inference deployments showing less than 2.5× efficiency gain over a 2024 GPT-4-class dense-FP16 baseline.** Below 2.5×, Interpretation 2 cannot reach its central 3× value, and the reconciliation requires Interpretation 1 to absorb more than 25% of the gap — implying GATT overestimation greater than the empirical evidence supports. The 2.5× threshold corresponds to the lower edge of our 2-4× range.
- **Audit of GATT's vendor-attribution multipliers revealing weighted-average errors above 20% (not 25%).** GATT's headline confidence rests on the assumption that vendor-attribution choices (Gemini All Surfaces 3.2× multiplier, Doubao all-sources scope, Anthropic 35% tokenizer expansion as upper-not-average) are within ±20%. Errors above 20% push Interpretation 1 beyond 1.25 and shift the decomposition's center beyond the plausible joint range.

The joint condition: if any single one of these thresholds is breached, the central decomposition becomes implausible and the parameter ranges must be re-estimated. If two are simultaneously breached, the decomposition is falsified and a different reconciliation framework is required. If all three are breached, the 2.04× discrepancy implies a structural error in either GATT or the Litowitz-Polson-Sokolov framework that the decomposition cannot bridge.

These are deliberately tighter conditions than v0.92 stated. Each threshold sits at the edge of plausible empirical evidence, not in the extreme tail. A serious empirical measurement program could confirm or reject these conditions within 6-12 months.

### 5.5.7 The Joint Calibration Proposal

The §5.5 decomposition cannot be uniquely identified without empirical measurement of the parameters it relies on. The natural next step is a co-authored joint calibration study with the Litowitz-Polson-Sokolov framework authors. Specifically, we propose three coordinated empirical measurements:

**Measurement 1 — Per-token energy benchmark.** Apply the Litowitz-Polson-Sokolov framework directly to representative 2026 inference deployments (DeepSeek V4 Pro on H100 cluster, Anthropic Opus 4.7 on Anthropic infrastructure, Gemini Flash on Google TPU 8th-gen) using their own Landauer-Shannon calibration methodology, but with 2026 hardware and architecture inputs. The output is an updated tokens-per-Joule ceiling that is no longer "calibrated to GPT-4-class deployment patterns." This measurement directly resolves Interpretation 2's central value.

**Measurement 2 — Production cache-hit characterization.** Coordinate with one or more major chat-platform operators (vLLM, OpenRouter, or a participating frontier-model vendor) to publish KV-cache hit-rate distributions across representative chat and reasoning workloads. This is non-proprietary platform-engineering data; the obstacle is publication willingness, not measurement. This measurement directly resolves Interpretation 3's central value.

**Measurement 3 — GATT vendor-attribution audit.** Conduct an external audit of GATT's vendor-attribution choices, particularly the Gemini All Surfaces 3.2× multiplier and the Doubao all-sources scope. The audit could be conducted by the IDC or CAICT teams whose data already triangulates GATT's regional aggregates. This measurement directly resolves Interpretation 1's central value.

Each measurement is independently valuable (each could publish as a methodology note in its own right) and jointly sufficient to convert the §5.5 decomposition from a hypothesis into a tested model. We invite the Litowitz-Polson-Sokolov team to co-design Measurement 1, IDC/CAICT teams to co-design Measurement 3, and the OpenRouter/vLLM communities to co-design Measurement 2. The output of all three would be a follow-up paper bearing the appropriate co-authorship — likely Litowitz, Polson, Sokolov, and Gao for Measurement 1's results, with appropriate co-authorship from the platform-data and audit-data contributors. This paper, v1.0 of GATT, is the pitch document for that program.

## 5.6 Implications for Methodology

The reconciliation has three constructive consequences for GATT and one for physical-ceiling modeling.

For GATT, v0.83 will: (a) adopt the observed/inferred/judgment parameter classification from the Inference Bottleneck paper [12] as a richer alternative to the four-level confidence rating; (b) publish sensitivity bands for headline figures, with conservative bounds anchored to physics-ceiling assumptions and aggressive bounds matching current empirical extrapolation; and (c) attach explicit as-of dates to all blended pricing assumptions, consistent with Xing's [6] documentation of 40× pricing decline over 24 months.

For physical-ceiling modeling, the comparison suggests that updating efficiency calibrations from GPT-4-class baselines to 2026 frontier-deployment baselines (MoE activation rates, quantization, ASIC efficiency) is a high-leverage methodological refinement. The Litowitz et al. framework remains correct in structure; the calibration inputs are where the action is.

The deeper point is that empirical tracking and physical-bound modeling are productive complements. Each catches what the other misses. The Token Economy needs both.
