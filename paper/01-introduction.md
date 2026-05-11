# 1. Introduction

## 1.1 The 2× Discrepancy

In February 2026, Litowitz, Polson, and Sokolov constructed a thermodynamics-grounded supply-and-demand balance sheet for global AI token production [1]. Their headline projection: under the 326 TWh of US AI energy allocation projected for 2028, the *physical* ceiling for token production sits at roughly 6.5 × 10¹⁷ tokens per year — equivalently, **225,000 tokens per United States resident per day**. The figure is derived from Landauer's principle [2] and Shannon's channel capacity [3], applied to current GPU and accelerator infrastructure.

In May 2026 — eighteen months ahead of that 2028 projection — the empirical Global AI Token Tracker (GATT) measures US per-capita token throughput at **459,700 tokens per resident per day**, or 2.04× the paper's 2028 ceiling.

This paper takes the discrepancy seriously. It cannot be that an AI ecosystem in 2026 is exceeding a 2028 *physical* ceiling. Yet both numbers are derived carefully — one from peer-track-record physics, the other from twenty-one vendor-level disclosures aggregated daily. The most useful interpretation is not that one is wrong, but that they measure different quantities, or that one of the constituent assumptions is loose.

We propose three reconciliations:

1. **GATT may overestimate top vendors.** The Gemini "All Surfaces" attribution multiplier (3.2× the API-disclosed throughput, to account for Search AI Overviews, the Gemini App, and Workspace) may double-count tokens emitted by interface layers that share underlying API infrastructure. The Doubao "all-sources" scope (132 trillion tokens per day, including ByteDance's internal first-party usage on Douyin AI Search, Doubao App, and Jimeng) may include cached or replicated agent-loop calls. A conservative correction trims GATT by 10-15%.

2. **The paper's physical ceiling is conservative.** Landauer/Shannon assumes uniform compute-per-token at GPT-4-level efficiency. Real 2026 inference operates well above this baseline. Mixture-of-Experts architectures activate as little as 3% of total parameters per token (DeepSeek V4 Pro: 49 billion active out of 1.6 trillion total). 4-bit quantization shrinks memory bandwidth requirements 4×. Speculative decoding multiplies effective throughput 2-3×. Dedicated inference ASICs — Groq LPUs, Google TPU 8th-gen, Tencent's chip stack, Xiaomi's MiMo deployment — operate at watts-per-token efficiencies far below general-purpose GPUs. Compounding these factors, effective tokens per Joule may sit 5-10× above the paper's baseline assumption.

3. **The two metrics measure different units.** GATT measures empirical all-surface output: every token generated and delivered to a user surface, regardless of whether the underlying computation reused a cached prefix, batched alongside other tenants, or replicated through multi-tenant agent loops. The Litowitz et al. paper models theoretical physical capacity assuming each token requires fresh compute. The two are related but not identical, much as "kilowatt-hours delivered to consumer outlets" differs from "kilowatt-hours of fuel input at the power plant." Both are valid; the 2× ratio reflects efficiency multipliers in the inference stack.

We argue that interpretations (2) and (3) jointly account for most of the gap, with (1) contributing a smaller share. Section 5 develops this argument in detail. The point of this paper is not to invalidate either methodology — both are valuable — but to propose that the *productive* interpretation of the discrepancy is methodological maturation rather than measurement error.

## 1.2 Disambiguation: Token Economy vs. Tokenomics vs. TokenOps

Four distinct concepts use overlapping "token" vocabulary, and confusion among them substantially limits the discoverability and citation pathways of token-economy research. We disambiguate explicitly.

**"Token Economy" (this paper)** refers to the global market for AI inference token production, distribution, and consumption — the empirical phenomenon GATT measures. Throughput is denominated in trillions of tokens per day across 24 vendors and 12 countries; economic value is measured in retail-equivalent USD (Token GDP). This is a *macro-empirical* construct.

**"Tokenomics" / "Token Economics" (blockchain)** refers to the supply dynamics, distribution mechanics, and incentive structures of cryptocurrency tokens within distributed ledger networks. The term predates the LLM-token usage by approximately a decade. When a general reader queries "tokenomics" via Google AI Overview, blockchain content dominates the response by default. We do not contest this vocabulary; GATT does not measure blockchain tokens.

**"TokenOps" / "FinOps for AI" (enterprise cost management)** [29, 30, 31] refers to operational disciplines for tracking and optimizing LLM token consumption at the firm level — prompt structure efficiency, request batching, cost attribution. Commercial SaaS offerings now operationalize this discipline (Finout, BMC Helix, Apptio). TokenOps and the present paper are complementary: TokenOps optimizes within-firm token consumption; this paper measures and aggregates across-firm token consumption at the global level. Section 2.7 develops this complementarity in detail.

**"Token Economy" (behavioral psychology)** refers to a 1960s clinical-psychology behavior-modification protocol — physical tokens earned for target behaviors, exchanged for backup reinforcers. This usage predates both AI and blockchain by decades but operates in a distinct disciplinary literature with no overlap to the present work.

The vocabulary collision is not merely terminological. It directly shapes the discoverability of token-economy research via large-language-model-mediated search (so-called Generative Engine Optimization). We propose that the AI-inference meaning of *"Token Economy"* is the appropriate empirical-macroeconomic counterpart to *"Tokenomics"* (blockchain) and to *"TokenOps"* (firm-level cost management), and use the term consistently in this sense throughout.

## 1.3 The Measurement Gap

GATT exists because no other public dataset measures global AI inference in token units. Existing approaches fall into four categories:

- **USD-priced infrastructure forecasts** (IDC Worldwide AI Infrastructure Tracker, Gartner Worldwide AI Spending) are useful for capital-expenditure planning but blind to volume. The unit is dollars, not tokens.
- **Single-jurisdiction token reports** (IDC China Public Cloud Large Model Services [4], May 2026) are restricted to one geography and to one slice (external enterprise MaaS). They cannot speak to global aggregates or to internal first-party usage.
- **Single-platform token studies** (a16z and OpenRouter's "100 Trillion Token Study" [5], January 2026) provide deep insight into one aggregator but cover only ~1% of global throughput.
- **Training-FLOPs trackers** (Epoch AI) measure model-training compute, not inference, and use a different unit.

GATT fills the gap as a global, all-sources, daily-updated, per-vendor index. It is also, deliberately, free and CC BY 4.0 — addressing what we observe as a citation barrier in the existing commercial-research landscape.

## 1.4 Contributions

This paper makes four contributions:

1. We **introduce GATT** — a daily empirical index of global AI inference token throughput across 21 vendors and 12 countries, with full revision history and confidence ratings. This work directly operationalizes Brynjolfsson's [17] December 2025 prediction that 2026 will see "the emergence of high-frequency AI economic dashboards that track, at the task and occupation level, where AI is boosting productivity, displacing workers, or creating new roles."
2. We **document an all-sources scope methodology** that distinguishes external enterprise API calls from internal first-party usage, and reconcile our scope with IDC's narrower external-MaaS-only methodology.
3. We **surface and reconcile the 2× discrepancy** with the physics-ceiling literature, proposing a synthesis that is informative for both empirical measurement and physical-bound modeling.
4. We **propose "Token GDP"** — a vendor-volume × regional-blended-pricing metric — as a regional-comparable economic-value indicator for the Token Economy. This addresses a gap noted by Xing [6], who argues for a "Token Performance Index" as essential infrastructure for an emerging token futures market, and complements the USD-side analysis of Patel [22] and SemiAnalysis.

## 1.5 Roadmap

Section 2 places GATT in the existing literature spanning commercial research, single-platform studies, physics-economics models, and empirical user studies. Section 3 details the methodology, including vendor coverage, confidence hierarchy, all-sources scope, the daily extrapolation engine, and the Token GDP formula. Section 4 reports empirical findings as of May 9, 2026. Section 5 returns to the 2× discrepancy and develops the reconciliation argument. Section 6 discusses policy and geo-economic implications. Section 7 concludes with limitations and an invitation to collaborate.
