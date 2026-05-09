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

## 5.5 Synthesis

We assign rough weights to the three interpretations:

- **Interpretation 1** (GATT overestimates): 10-15% downward correction. Removes ~30-70K of the 459.7K US per-capita figure.
- **Interpretation 2** (paper ceiling conservative): 5-10× upward correction to the ceiling. Lifts 225K to 1.1-2.25M.
- **Interpretation 3** (different units): 1.5-2× multiplicative wedge between emitted and fresh-compute tokens. Explains a substantial fraction of the gap on its own.

No single interpretation dominates. Interpretations 2 and 3 jointly explain most of the discrepancy without invoking measurement error in either methodology. Interpretation 1 contributes a smaller share. The 2× ratio is fully accounted for under combinations that leave both methodologies internally consistent.

## 5.6 Implications for Methodology

The reconciliation has three constructive consequences for GATT and one for physical-ceiling modeling.

For GATT, v0.83 will: (a) adopt the observed/inferred/judgment parameter classification from the Inference Bottleneck paper [12] as a richer alternative to the four-level confidence rating; (b) publish sensitivity bands for headline figures, with conservative bounds anchored to physics-ceiling assumptions and aggressive bounds matching current empirical extrapolation; and (c) attach explicit as-of dates to all blended pricing assumptions, consistent with Xing's [6] documentation of 40× pricing decline over 24 months.

For physical-ceiling modeling, the comparison suggests that updating efficiency calibrations from GPT-4-class baselines to 2026 frontier-deployment baselines (MoE activation rates, quantization, ASIC efficiency) is a high-leverage methodological refinement. The Litowitz et al. framework remains correct in structure; the calibration inputs are where the action is.

The deeper point is that empirical tracking and physical-bound modeling are productive complements. Each catches what the other misses. The Token Economy needs both.
