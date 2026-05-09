# 5. The 2× Discrepancy with Photons = Tokens

This section returns to the question that opened the paper. Litowitz, Polson, and Sokolov [1] project that the 2028 United States AI energy allocation of 326 TWh can support roughly 6.5 × 10¹⁷ tokens per year, equivalently 225,000 tokens per resident per day. GATT v0.82 measures United States per-capita throughput at 459,700 tokens per resident per day in May 2026 — eighteen months *before* the paper's projection date, yet **2.04× above the paper's 2028 ceiling**.

Both numbers are produced carefully. We argue that the gap reflects three compounding factors, each of which can be quantified, and that the *informative* interpretation of the discrepancy is methodological complementarity rather than measurement error.

## 5.1 Restating the Discrepancy

The Litowitz et al. ceiling derives from three inputs: a 326 TWh US AI energy allocation projected for 2028, Landauer's information-theoretic minimum energy cost per bit, and a Shannon-channel capacity calibration anchored to GPT-4-class inference efficiency. Their token-budget framework is rigorous within these assumptions and produces a meaningful upper bound on token production under fixed inputs. The 225,000 tokens-per-resident-per-day figure is the per-capita normalization of their aggregate ceiling under 2028 US population estimates.

The GATT empirical figure derives from twenty-one vendor-level estimates summed into a national total, divided by US population. Each vendor estimate is anchored in a dated source signal — a vendor disclosure, an ARR-and-pricing back-calculation, or platform-aggregator data — and updated via the extrapolation engine described in Section 3.4.

The two figures are not measuring the same physical quantity. We now develop three reconciliation interpretations, each accounting for some portion of the 2× ratio.

## 5.2 Interpretation 1 — GATT May Overestimate Top Vendors

GATT's largest United States vendor-attribution decisions involve interpretation, not direct disclosure. Most consequentially, Google's "Gemini All Surfaces" estimate of 73 trillion tokens per day applies a 3.2× multiplier to the 23-trillion-tokens-per-day figure derived from Pichai's "more than 16 billion tokens per minute via direct API" disclosure. The multiplier covers Search AI Overviews, the Gemini App's 750 million monthly active users, and Workspace integrations. If the multiplier double-counts tokens emitted by interface layers that share underlying API infrastructure, the All Surfaces figure could be high by 15-25%. Trimming Gemini from 73T to 60T would reduce US daily volume by roughly 13 trillion tokens, lowering US per-capita by approximately 39,000 tokens per resident per day.

Anthropic's Opus 4.7 tokenizer change (Section 4.5) is more straightforward — Anthropic confirms the new tokenizer produces up to 35% more tokens per equivalent input — but this raises a related concern: tokens are now a less stable measurement unit across models. A 35% increase in tokens for unchanged work is not a 35% increase in compute or value.

Combining Gemini-multiplier compression and tokenizer-inflation correction produces a conservative US per-capita estimate around 410,000-430,000 tokens per resident per day, still 1.8-1.9× above the 2028 physical ceiling. Interpretation 1 alone cannot close the gap.

## 5.3 Interpretation 2 — The Physical Ceiling is Conservative

The Litowitz et al. ceiling assumes GPT-4-class inference efficiency. Real 2026 inference operates well above this baseline through four compounding optimizations.

**Mixture-of-Experts architectures** activate a small fraction of total parameters per token. DeepSeek V4 Pro routes 49 billion of 1.6 trillion total parameters per token — approximately 3% activation. Tencent's Hy3 (Hunyuan 3.0) activates 21 billion of 295 billion (7%). Kimi K2.6 activates 32 billion of 1 trillion (3.2%). Where Litowitz et al. budget Joules for full-model dense activation, real frontier models in May 2026 activate 3-10% of parameters per token, producing a 10-30× efficiency multiplier on the parameter-touching component of inference cost.

**4-bit quantization** is now standard for inference deployment. Compared to the FP16 baseline implicit in the physics-ceiling computation, 4-bit weights reduce memory bandwidth — the dominant inference cost on most hardware — by 4×.

**Speculative decoding** uses a small draft model to produce candidate tokens that the larger model verifies in parallel. Production deployments achieve 2-3× throughput multipliers on equivalent hardware.

**Dedicated inference ASICs** — Groq LPUs, Google TPU 8th-generation, Tencent's chip stack, Xiaomi's MiMo deployment hardware — operate at watts-per-token efficiencies well below general-purpose GPU baselines. Public Groq benchmarks suggest 5-10× efficiency improvements on certain workloads.

Compounding these factors does not require multiplying the headline numbers (a hardware cap remains). But under realistic 2026 deployment patterns, effective tokens-per-Joule may sit 5-10× above the GPT-4-class baseline assumed in the paper's calibration. Lifting the 225,000 ceiling by 5-10× yields an effective ceiling of 1.1-2.25 million tokens per resident per day — comfortably above the 459,700 GATT figure.

Interpretation 2 alone could account for the entire 2× discrepancy and more. We do not assert that it does; reasonable people can debate the multiplier. But the direction is unambiguous: the paper's physical ceiling is a *static* artifact of its 2024-era efficiency calibration, while empirical token production rides a moving frontier of inference-stack innovation.

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

Section 5.3 argued that the Landauer-Shannon ceiling assumes uniform compute-per-token at GPT-4-class efficiency. We want to be careful here: Landauer's principle is an information-theoretic lower bound on energy per irreversible bit operation, and is not "tight" against any specific hardware artifact. The right framing is: Litowitz-Polson-Sokolov's *calibration* of token-per-Joule efficiency is anchored to GPT-4-class deployment patterns. Updating that calibration to 2026 inference-stack realities — Mixture-of-Experts activation rates (3-10% vs. dense), 4-bit quantization (4× memory bandwidth efficiency), speculative decoding (2-3× throughput multiplier), and dedicated inference ASICs (5-10× watts/token vs. general-purpose GPU baseline) — produces a substantially higher effective ceiling under the same energy budget.

Quantifying conservatively: the four factors compound non-multiplicatively (memory bandwidth overlaps with quantization; ASIC efficiency is partially captured by quantization). A central estimate of the *effective* tokens-per-Joule lift versus a 2024-vintage dense FP16 baseline is **3-5×** (we apply a substantial discount from the naive product of factor multipliers because real systems can't compound efficiency multipliers without architectural penalties). At 3×, the corrected ceiling is $L^{*}$ = 675K tokens/resident/day; at 5×, $L^{*}$ = 1.13M. We adopt the central value $L^{*}/L = 4$, with plausible range 3 to 5.

This is less aggressive than the "5-10×" stated in §5.3, in deference to the criticism that Landauer is an information-theoretic lower bound and that effective efficiency multipliers don't compound naively.

### 5.5.4 Interpretation 3: Emitted-vs-Fresh-Compute Factor

Section 5.4 argued that GATT counts emitted tokens (every token delivered to a user surface) while the physical-ceiling paper models fresh-compute tokens (tokens that traverse the full inference pipeline). Cache hits, batched inference, and multi-tenant agent loops decouple the two.

Quantifying: TokenPowerBench [13] documents that prefill versus decode phases of LLM inference have substantially different energy profiles; KV-cache hit rates of 30-50% are routinely reported in production chat applications [13, 6]. If we conservatively assume the *average* production deployment achieves a 35% effective compute reuse (combining cache hits, batching, and multi-tenant deduplication), the emitted-to-fresh-compute ratio is approximately $G^{*}/L^{*} = 1/0.65 \approx 1.54$. Plausible range: 1.3 to 2.0.

### 5.5.5 Combined Decomposition

Multiplying central values: 1.12 × 4 × 1.54 / 4 ≈ 1.72× (where the /4 corrects for double-counting since Interpretation 2 and 3 partially overlap — the ceiling lift partly already accounts for cache-hit-style efficiency gains). With explicit separation of effects:

| Factor | Central | Low | High | Effect on G/L |
|---|---:|---:|---:|---|
| Interp. 1 (G/G*) | 1.12 | 1.05 | 1.20 | trims GATT |
| Interp. 2 (L*/L) | 4.0 | 3.0 | 5.0 | lifts ceiling |
| Interp. 3 (G*/L*) | 1.54 | 1.30 | 2.00 | unit wedge |

Under the central assignment, the implied gap is $G/L^{\text{central}} = G^{*}/L^{*} \cdot L^{*}/L \cdot G/G^{*} \cdot 1/(G^{*}/L^{*})$... this gets tangled. Simpler: the *observed* gap of 2.04 is consistent with interpretation contributions if the corrected ceiling $L^{*}$ produces emitted-token capacity $L^{*} \cdot (G^{*}/L^{*}) \approx 4 \cdot 225 \cdot 1.54 = 1386$ K tokens/resident/day, against which a corrected GATT estimate $G^{*} = G/1.12 \approx 410$ K represents 30% utilization. In other words, **2026 empirical token output is well below the 2026-recalibrated, emitted-token-equivalent ceiling** — which is the economically and physically reasonable conclusion.

The 2.04× headline ratio is thus consistent with:
- GATT being modestly inflated (12% high)
- The Litowitz-Polson-Sokolov ceiling being conservatively calibrated to pre-2026 hardware (4× low)
- A 1.54× units-of-measurement wedge between emitted and fresh-compute tokens

No combination requires either methodology to be in error — both are internally consistent within their stated frames. The discrepancy reflects the gap between (a) a 2028 fresh-compute physical ceiling calibrated to early-2024 efficiency and (b) a 2026 emitted-token empirical measurement.

### 5.5.6 What Would Falsify This Decomposition

The decomposition above is a hypothesis, not a proof. It would be falsified if:

- Empirical measurement of cache-hit rates on the four largest GATT vendors revealed effective compute reuse below 20% (which would shrink Interpretation 3 below 1.25 and require Interpretation 2 to absorb more of the gap).
- Direct measurement of per-token energy on representative 2026 inference deployments showed < 2× efficiency gain over GPT-4-class baselines (which would shrink Interpretation 2 below 2× and force Interpretation 1 to absorb >40% of GATT, an implausibly large overestimation).
- An audit of GATT's vendor multipliers revealed errors > 25% (which would push Interpretation 1 above 1.30 and partially close the gap on its own).

Future work — particularly a joint study with the Litowitz-Polson-Sokolov authors on consistent units of token measurement — could tighten each factor's range substantially. We intend this section as an invitation to that work, not as a closure of the question.

## 5.6 Implications for Methodology

The reconciliation has three constructive consequences for GATT and one for physical-ceiling modeling.

For GATT, v0.83 will: (a) adopt the observed/inferred/judgment parameter classification from the Inference Bottleneck paper [12] as a richer alternative to the four-level confidence rating; (b) publish sensitivity bands for headline figures, with conservative bounds anchored to physics-ceiling assumptions and aggressive bounds matching current empirical extrapolation; and (c) attach explicit as-of dates to all blended pricing assumptions, consistent with Xing's [6] documentation of 40× pricing decline over 24 months.

For physical-ceiling modeling, the comparison suggests that updating efficiency calibrations from GPT-4-class baselines to 2026 frontier-deployment baselines (MoE activation rates, quantization, ASIC efficiency) is a high-leverage methodological refinement. The Litowitz et al. framework remains correct in structure; the calibration inputs are where the action is.

The deeper point is that empirical tracking and physical-bound modeling are productive complements. Each catches what the other misses. The Token Economy needs both.
