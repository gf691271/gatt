# Measuring the Token Economy

### An Empirical Companion to Physical-Ceiling Models of Global AI Inference

**Frank Gao** · May 2026 · GATT v1.5.1 · CC BY 4.0
Live data: <https://gf691271.github.io/gatt/>
Source: <https://github.com/gf691271/gatt>

---

# Abstract

In May 2026, the Global AI Token Tracker (GATT) measures **459,700 tokens per United States resident per day** — 2.04× the 2028 physical ceiling of 225,000 tokens per person per day projected by Litowitz, Polson, and Sokolov (2026, arXiv:2603.06630) under a 326 TWh AI energy allocation. This paper presents the empirical methodology underlying that measurement and proposes three reconciliation interpretations: (i) GATT may overestimate top vendors via attribution multipliers, (ii) the paper's Landauer/Shannon ceiling is conservative because real 2026 inference uses Mixture-of-Experts architectures, 4-bit quantization, speculative decoding, and dedicated inference ASICs, yielding 5-10× more tokens per Joule than the physics baseline, and (iii) the two metrics measure different units — GATT measures empirical all-surface output, while the physical-ceiling paper models theoretical capacity assuming fresh compute per token.

GATT is, to our knowledge, the first global, all-sources, daily-updated index of AI token throughput, covering 24 vendors across 12 countries. As of May 11, 2026, GATT measures global daily output at 311 trillion tokens, with China and the United States essentially tied (50.2/49.5) on volume but the United States capturing 88% of "Token GDP" — a vendor-volume × blended-pricing metric — due to a 15× pricing asymmetry between US and Chinese vendors. The US-India per-capita gap stands at 597×, having widened from 394× one month earlier; the population-weighted Gini coefficient of token consumption across the 12 countries is **0.674**, already exceeding global income inequality (~0.62) and approaching wealth-distribution levels of concentration. We document our methodology, contrast it with IDC China Public Cloud MaaS (which independently confirms our top vendor ranking at 49.5% Volcengine market share), and propose Token GDP as a regional-comparable economic-value metric for the emerging Token Economy. All data and code are released under CC BY 4.0 at gf691271.github.io/gatt/.

---

# 1. Introduction

## 1.1 The 2× Discrepancy

In February 2026, Litowitz, Polson, and Sokolov constructed a thermodynamics-grounded supply-and-demand balance sheet for global AI token production [1]. Their headline projection: under the 326 TWh of US AI energy allocation projected for 2028, the *physical* ceiling for token production sits at roughly 6.5 × 10¹⁷ tokens per year — equivalently, **225,000 tokens per United States resident per day**. The figure is derived from Landauer's principle [2] and Shannon's channel capacity [3], applied to current GPU and accelerator infrastructure.

In May 2026 — eighteen months ahead of that 2028 projection — the empirical Global AI Token Tracker (GATT) measures US per-capita token throughput at **459,700 tokens per resident per day**, or 2.04× the paper's 2028 ceiling.

This paper takes the discrepancy seriously. It cannot be that an AI ecosystem in 2026 is exceeding a 2028 *physical* ceiling. Yet both numbers are derived carefully — one from peer-track-record physics, the other from twenty-four vendor-level disclosures aggregated daily. The most useful interpretation is not that one is wrong, but that they measure different quantities, or that one of the constituent assumptions is loose.

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

1. We **introduce GATT** — a daily empirical index of global AI inference token throughput across 24 vendors and 12 countries, with full revision history and confidence ratings. This work directly operationalizes Brynjolfsson's [17] December 2025 prediction that 2026 will see "the emergence of high-frequency AI economic dashboards that track, at the task and occupation level, where AI is boosting productivity, displacing workers, or creating new roles."
2. We **document an all-sources scope methodology** that distinguishes external enterprise API calls from internal first-party usage, and reconcile our scope with IDC's narrower external-MaaS-only methodology.
3. We **surface and reconcile the 2× discrepancy** with the physics-ceiling literature, proposing a synthesis that is informative for both empirical measurement and physical-bound modeling.
4. We **propose "Token GDP"** — a vendor-volume × regional-blended-pricing metric — as a regional-comparable economic-value indicator for the Token Economy. This addresses a gap noted by Xing [6], who argues for a "Token Performance Index" as essential infrastructure for an emerging token futures market, and complements the USD-side analysis of Patel [22] and SemiAnalysis.

## 1.5 Roadmap

Section 2 places GATT in the existing literature spanning commercial research, single-platform studies, physics-economics models, and empirical user studies. Section 3 details the methodology, including vendor coverage, confidence hierarchy, all-sources scope, the daily extrapolation engine, and the Token GDP formula. Section 4 reports empirical findings as of May 9, 2026. Section 5 returns to the 2× discrepancy and develops the reconciliation argument. Section 6 discusses policy and geo-economic implications. Section 7 concludes with limitations and an invitation to collaborate.

---

# 2. Related Work

GATT sits at the intersection of four research traditions: commercial research firms producing USD-priced infrastructure forecasts; recent academic and industry studies producing token-volume estimates from narrow slices of the market; physics-and-economics theoretical models of AI inference; and empirical user studies of platform usage patterns. None of these covers the full territory GATT occupies — global, all-sources, daily, per-vendor — but each contributes a piece, and GATT's methodology engages with all four.

## 2.1 Commercial Research (USD-priced)

The dominant commercial-research vocabulary for AI economics is dollars, not tokens. IDC's *Worldwide Artificial Intelligence Infrastructure Tracker* projects global AI infrastructure spending will reach $758 billion by 2029 [7], with the United States accounting for 76% of 2Q25 spending, the People's Republic of China 11.6%, Asia-Pacific-Japan 6.9%, and EMEA 4.7%. Cloud and shared environments command 84.1% of total spending. Gartner's *Worldwide AI Spending* forecast similarly aggregates AI software, services, and infrastructure: $1.5 trillion in 2025 [8], with revisions toward $2 trillion in 2026.

These figures are essential for capital-expenditure planning, vendor sales sizing, and macroeconomic comparisons. They are not, however, useful for measuring throughput. Two equal infrastructure-dollar investments can produce wildly different token volumes depending on hardware efficiency, model architecture, and inference optimization. Conversely, a dollar of GPT-5.5 inference at Anthropic's Opus 4.7 prices produces about 15 times fewer tokens than a dollar of Doubao inference. The USD-token translation is non-stationary: Xing [6] documents that GPT-4-equivalent output pricing fell from approximately $60 per million tokens in early 2023 to under $1.50 per million in early 2025 — a 40-fold reduction in 24 months. SemiAnalysis [22] reports an even sharper compression for GPT-3-equivalent inference (1200×) and documents that AI-cloud TCO modeling now spans multi-year cycles compressed into weeks. Any analysis pinned to dollar units must constantly re-anchor as pricing moves.

GATT does maintain a Token GDP metric (vendor volume × regional blended price), but this is presented alongside, not in place of, raw token volume.

## 2.2 Token-Volume Research

Token-volume measurement has three principal sources, each constrained.

**The China Academy of Information and Communications Technology (CAICT, 中国信通院)** independently corroborates token-volume measurement from a Chinese government research perspective. The CAICT *Artificial Intelligence Industry Development Research Report (2025)* [16], released January 2026, documents the maturation of China's large-model ecosystem; CAICT Vice President Wei Liang, quoted in the report context, frames the industry shift as "from parameter scaling to architecture optimization." For GATT, CAICT serves as a Chinese-government-research-perspective validation alongside IDC's May 2026 report and the National Data Administration's 140T-per-day national figure.

**OpenRouter Platform Weekly Aggregation** (separate from but conceptually related to the CAICT reporting context) provides an independently-published, neutral-third-party weekly token-volume aggregation that quantifies the China-US comparison. In the week of February 9-15, 2026, OpenRouter recorded Chinese mainstream large-model API throughput at **4.12 trillion tokens per week**, exceeding US mainstream models' 2.94 trillion in the same week — the first observed week of Chinese model leadership on the platform. The lead extended to 5.16T (Feb 16-22) and 7.36T (Mar 16-22), a three-consecutive-week China advantage. Chinese media (Yicai Global, CCID, Sina Finance, QbitAI) widely reported this trend through March 2026 [4]. The OpenRouter data is methodologically narrower than GATT's all-sources scope — it captures only API throughput on a specific aggregator platform — but its neutrality (a US-headquartered aggregator with no policy stake in either side) makes it a particularly clean cross-validation source for GATT's broader China-US volume parity finding.

Together, IDC's external-MaaS-only report, the National Data Administration's all-sources national figure, CAICT's qualitative ecosystem analysis, and OpenRouter's neutral platform aggregation form four concentric scopes that GATT triangulates across to produce its headline regional estimates.

**IDC China Public Cloud Large Model Services**, released May 7, 2026 [4], reports that China's external enterprise MaaS market consumed 114 trillion tokens in 2024, growing 16-fold to 1,944 trillion in 2025, with a forecast of approximately 40,000 trillion tokens for 2026. Volcengine led the market at 49.5% share for full-year 2025 (up from 46.4% in 2024 and 49.2% for the first half of 2025). Alibaba Bailian held second position at 27% (H1 2025); Baidu Qianfan held third at 17%. The IDC report is the highest-quality external token-volume measurement available, but it has two scope restrictions: it covers only China, and it counts only external enterprise public-cloud calls. Internal first-party usage — for example, ByteDance's own consumption of Doubao through Douyin AI Search, the Doubao consumer app, and the Jimeng image-generation product — is explicitly excluded from IDC's scope.

This exclusion produces a striking gap. IDC's 2025 China average works out to 5.32 trillion tokens per day across all external MaaS, of which Volcengine's 49.5% share equals approximately 2.64 trillion tokens per day. The Volcengine official disclosure of 120 trillion tokens per day at the Wuhan AI Innovation Expo (April 1, 2026) is roughly 45 times higher. The reconciliation is unambiguous: more than 95% of Volcengine's measured throughput is internal first-party usage outside IDC's scope. GATT's "all-sources" methodology (Section 3.3) is designed precisely to cover this gap.

**Aubakirova et al. (2026) State of AI: An Empirical 100 Trillion Token Study** [5], conducted by Andreessen Horowitz with OpenRouter, analyzes 100 trillion cumulative tokens of LLM interactions on the OpenRouter platform. The study documents that open-source models, particularly reasoning-forward variants such as DeepSeek R1 and Kimi K2, are gaining share due to cost efficiency. Creative and coding workloads dominate token volume. As of December 2025, OpenRouter processed more than 1 trillion tokens per day, growing approximately 4× year-over-year (from 5 trillion per week in April 2025 to 20 trillion per week in April 2026). The study is rigorous within its scope but its scope is one aggregator. GATT estimates total OpenRouter throughput at approximately 3 trillion tokens per day in May 2026 — about 1% of global throughput.

**Vendor disclosures** form the third pillar. OpenAI announced on March 31, 2026 that its APIs process more than 15 billion tokens per minute [9]. Sundar Pichai, in Google's Q1 2026 earnings call delivered at Cloud Next 2026, disclosed that Gemini processes more than 16 billion tokens per minute via direct API [10] — up from 10 billion in Q4 2025. Volcengine's 120 trillion tokens per day disclosure at the Wuhan event has already been discussed. Microsoft's Q3 FY2026 earnings (April 29, 2026) reported AI business ARR of $37 billion, up 123% year-over-year. These vendor disclosures are the highest-confidence inputs to GATT but appear sporadically and at heterogeneous granularities (per-minute API throughput, per-day total, per-quarter ARR). GATT translates these into a uniform daily-token unit.

## 2.3 Physics & Economics of Inference

A small but growing literature treats AI inference as an object of formal physics or economics modeling.

The most directly relevant is **Litowitz, Polson, and Sokolov (2026)** [1], which constructs a MacKay-style supply-and-demand balance sheet for global token production. The authors apply Landauer's principle [2] and Shannon's channel capacity [3] to current and projected GPU and accelerator infrastructure. Their headline result — that the projected 2028 US AI energy allocation of 326 TWh could support roughly 6.5 × 10¹⁷ tokens per year, or 225,000 tokens per person per day — is the principal benchmark this paper engages with (Section 5). Their framing, that token production has thermodynamic costs and that the question of "which tokens are worth producing" matters more than capacity expansion, is broadly compatible with GATT's emphasis on Token GDP rather than raw volume.

**Xing (2026)** [6] extends this argument into commodity-market design, proposing that AI tokens have evolved into a commodity asset class with fungibility, standardized measurement, large-scale trading, non-storability, and supply rigidity — sharing critical features with electricity, carbon emission allowances, and bandwidth. The paper proposes derivative contract designs for AI token futures and estimates that such instruments could reduce enterprise compute cost volatility by 62-78% via Monte Carlo simulation. The optimal launch window is identified as 2027-2028. Xing notes the absence of a "Token Performance Index (TPI)" as critical infrastructure missing for the proposed market; GATT functions as a working prototype of such an index.

**Zhuang et al. (2025)** [11] develop the first formal "LLM Inference Production Frontier," establishing three economic principles: diminishing marginal cost, diminishing returns to scale, and an optimal cost-effectiveness zone. The framework supports pricing-side normalization of token throughput and could provide theoretical grounding for GATT's Token GDP methodology in future versions.

**The Inference Bottleneck paper (2026, arXiv:2604.17431)** [12] develops a formal economic model of vertical foreclosure in AI markets with explicit calibration methodology. The paper distinguishes observed, inferred, and judgment-based parameters, and provides sensitivity analysis establishing which conclusions are robust to parameter perturbations. GATT's current confidence taxonomy (high/medium/low) is less granular than this template; we adopt the observed/inferred/judgment classification as the v0.83 development target.

**TokenPowerBench (Anonymous 2025, arXiv:2512.03024)** [13] introduces energy-centric metrics — Joules per token, Joules per response, instantaneous power draw — aligned with the prefill and decode phases of transformer inference. Its findings on the variability of energy-per-token across architectures support Section 5's argument that the physical-ceiling computation is sensitive to assumptions about inference-stack efficiency.

**Epoch AI** [18], the technological-forecasting research organization led by Jaime Sevilla, complements the physics-and-economics literature with a longitudinal data series on inference cost trajectories. Epoch AI documents that inference cost at a fixed performance level halves every two months — equivalent to a two-orders-of-magnitude decline per year — across the 2024-2026 window. The formal write-up [36] documents that this rate is *not uniform*: the price-decline rate varies from 9× per year to 900× per year depending on the benchmark, with GPT-4-quality inference falling at approximately 40× per year. This non-uniformity matters for GATT's Section 3.5 Token GDP construction: a single price-decline assumption averaged across task classes will misstate the real-resource growth rate for any specific workload, and the §2.3 implied +50%/month resource-growth figure is best read as a global mean that masks substantial cross-workload variance. This rate is consistent with both Xing's [6] 40× compression observation and SemiAnalysis's [22] 1200× claim for older model tiers. For GATT, Epoch's findings reinforce the Section 3.5 caveat that Token GDP figures must carry explicit as-of dates: pricing assumptions decay quickly enough that any Token GDP statement six months old is materially mis-anchored.

The quantitative juxtaposition between Epoch AI and GATT is informative. If Epoch's cost curve halves every 2 months — equivalent to roughly -30% per month price decline for fixed capability — and GATT measures +22% per month volume growth, the implied real-resource expansion (the rate at which actual compute consumption is growing, net of price effects) is approximately +50% per month — equivalent to a doubling every 2 months at the resource-input level. This rate is consistent with hyperscaler capital expenditure trajectories: top-five US hyperscalers (Meta, Alphabet, Microsoft, Amazon, Oracle) committed approximately $602B in 2026 AI infrastructure capex, a +36% year-over-year increase against 2025's $443B [21]. The GATT volume growth and the Epoch cost decline thus jointly imply that the field is in a regime where both *price compression* and *volume expansion* are occurring rapidly, with the expansion winning on the margin — the price-volume paradox formalized in this paper's Section 4.

## 2.4 Empirical Comparison Studies

A separate literature surveys actual user behavior across platforms. The most relevant is the **Cross-Platform User Survey (2026, arXiv:2603.25220)** [14], which collected responses from 388 active AI chat users across seven major platforms (ChatGPT, Claude, Gemini, DeepSeek, Grok, Mistral, Llama). Three findings inform GATT's methodology: first, the top three platforms (Claude, ChatGPT, DeepSeek) receive statistically indistinguishable satisfaction ratings, validating GATT's choice not to focus on a single "leader"; second, more than 80% of users use two or more platforms, with negligible switching costs, supporting a multi-vendor measurement approach; third, each platform attracts users for different reasons (interface, answer quality, content policy, word-of-mouth), implying that specialization rather than generalist dominance sustains competition.

## 2.5 Economic Theory: GPT Frameworks and Productivity Measurement

GATT's Token GDP construct connects to a longstanding economics literature on the measurement of new technologies. Three frameworks are particularly relevant.

**General-purpose technology (GPT) framework.** Bresnahan and Trajtenberg (1995) [26] formalized the analysis of technologies that "have the potential to be used in many sectors and have many opportunities for technological complementarity," explicitly framing electricity and the internal combustion engine as historical analogues. David (1990) [27] developed the canonical historical case study — "The Dynamo and the Computer" — documenting the long lag between electrification and measurable productivity gains as the U.S. economy reorganized factory layouts, business processes, and worker training around the new technology. Brynjolfsson, Rock, and Syverson (2021) [23] extended the framework with the *productivity J-curve*: GPTs initially appear to depress measured productivity (because intangible complementary investments are misclassified as costs rather than capital formation), then produce a sharp acceleration once those investments mature. AI inference fits the GPT pattern almost paradigmatically: token consumption is occurring across virtually every sector, with the heavy concentration in coding, search, and creative use cases that GATT documents. The price-volume paradox surfaced in this paper — 99.7% unit-price decline coexisting with 3× total enterprise spending — is more naturally framed as **capability expansion along an outward-shifting production possibility frontier** (David's "computer-dynamo" template) than as a Jevons rebound effect on a homogeneous good. Token consumption across architectural generations (frontier reasoning models, mid-tier chat, budget open-weight) is not a homogeneous commodity; quality-adjusted Hicksian substitution along an expanding frontier is the appropriate economic frame, and the David analogy provides the historical precedent.

**Task-based growth framework.** Acemoglu and Restrepo (2018) [24] developed a model of growth in which technologies can either *automate* existing tasks (substituting capital for labor) or *enable new tasks* that did not previously exist. Their framework distinguishes the displacement effect from the reinstatement effect, with the latter driving long-run growth. Token consumption maps onto this framework cleanly: agentic and reasoning workloads (Section 4 of GATT v0.87's `reasoning_split` block: 31% of global volume in May 2026, the principal growth vector) primarily *enable new tasks* (multi-step automation, code generation at scale, long-horizon agent loops) rather than automating routine knowledge work. The GATT data, viewed through the Acemoglu-Restrepo lens, suggests that the AI economic moment is currently dominated by reinstatement (new-task creation) rather than pure displacement — supporting the productivity-J-curve hypothesis that meaningful productivity gains are coming.

**Value-added vs. gross-output measurement.** Hulten (1978) [25] codified the methodological treatment of intermediate inputs in growth accounting, distinguishing value-added (the standard headline GDP construct) from gross output (which includes intermediate transactions). As Section 3.3.1 details, GATT's all-sources volume is closer to the gross construct, with consequences for cross-regional comparison. The Hulten framework also clarifies the appropriate aggregation for Token GDP: under standard national-accounts practice, summing transacted retail prices across vertical-pipeline tokens overstates true economic value-added.

These three frameworks are not separate concerns — they jointly constrain the interpretation of GATT's headline numbers. The price-volume paradox (Bresnahan-Trajtenberg / Brynjolfsson-Rock-Syverson territory), the workload mix (Acemoglu-Restrepo territory), and the volume-vs-Token-GDP asymmetry (Hulten territory) together form the economic interpretation of the dataset that this paper has so far pursued only descriptively. Future work — particularly a co-authored extension with macroeconomists — could formalize the GATT data as a panel for empirical testing of GPT-era productivity claims.

## 2.6 Industry Framing: NVIDIA GTC 2026 Token Economics

In May 2026, NVIDIA's GTC keynote [28] introduced a publicly articulated "Token Economics" framework as the company's core narrative for the Blackwell-to-Vera-Rubin architecture transition. The framework plots two axes: **tokens per watt** (Y, throughput per power input) and **tokens per second per user** (X, interaction speed, presented as a proxy for inference quality). Huang's central claim: in a power-constrained world, architectural efficiency on this two-axis surface determines annual revenue per gigawatt of installed inference capacity, with Rubin delivering 5× the 1 GW datacenter annual revenue of Blackwell ($30B → $150B) through 2-10× efficiency gains across user-tier service levels. Total Blackwell + Vera Rubin order backlog through 2027 is reported at approximately $1 trillion, double the prior-year $500 billion projection.

This industry framing is the **supply-side, capacity-imputed counterpart** to the present paper's *demand-side, consumption-measured* approach. The two constructs are best understood through the GDP-accounting analogy: NVIDIA's framework is the *production-side* aggregate (factory output × imputed pricing × utilization assumptions); GATT's Token GDP (Section 3.5) is the *expenditure-side* aggregate (realized vendor revenue from observed token consumption). In a closed token economy, the two should equal each other up to a statistical discrepancy; their measured difference is itself a research output, paralleling the production-vs-expenditure GDP discrepancy that has been a long-standing topic of national-accounts research [25].

Two methodological tensions in the NVIDIA framing warrant explicit note. First, the X-axis "tokens per second per user as proxy for inference quality" implicitly aggregates *output tokens* and *hidden reasoning tokens* (chain-of-thought traces from o1-class reasoning models). Modern reasoning models emit 50-200K reasoning tokens per user-visible answer; whether the GTC framework counts these in Y-axis throughput, in X-axis TPS/user, in both, or in neither is not specified in the public presentation. This *reasoning-token asymmetry* affects both supply-side and demand-side accounting and is the focus of the Section 5.5.8 Token Velocity decomposition. Second, the NVIDIA framework treats "1 token" as a homogeneous unit across vendors and models — an assumption that cross-vendor tokenizer-fungibility analysis (Section 3.2 and Appendix A) directly contradicts.

We propose that demand-side empirical measurement (this paper) and supply-side capacity modeling [1, 28] are complementary frameworks that jointly constrain the global Token Economy more tightly than either alone. The reconciliation work — quantifying and explaining the supply-side vs demand-side Token GDP discrepancy — is a publishable research question that the present paper opens for subsequent work.

## 2.7 Enterprise Token Cost Management: TokenOps and FinOps for AI

A parallel literature in enterprise operations — variously labeled "TokenOps" or "FinOps for AI" — addresses token consumption at the single-firm level. Representative work includes Finout's *Definitive Guide to FinOps for Tokens* [29], Healthark Insights' *Token Economics: Measuring and Optimizing the Cost of Intelligence* [30], Inventive HQ's *Optimize Prompts to Reduce Token Costs* [31], and the academic survey [32]. Commercial SaaS implementations — Finout's TokenOps platform, BMC Helix's AI cost-tracking modules, and similar offerings from CloudHealth and Apptio — provide firm-level dashboards on the dimensions of cost, latency, and model-routing efficiency.

This literature is *micro-operational*: its unit of analysis is the firm, its objects are prompt structure / batch geometry / model selection, and its outputs are cost-per-output-quality optimization decisions. The present paper's unit of analysis is the global system, its objects are vendor-level volumes and pricing, and its outputs are macro-empirical aggregates (Token GDP, per-capita gaps, distributional Gini). The two frameworks are connected by an obvious accounting identity: the sum of firm-level token expenditures across firms in a region equals — up to measurement error — the region's Token GDP at the macro level.

Two specific complementarities follow. First, TokenOps frameworks provide validation of the *price-per-million-tokens* parameters that enter Token GDP calculations: their cost-management product literature documents realized blended pricing across model selections and vendor mixes, which a macro paper cannot directly observe. Second, the present paper's macro-aggregate datasets provide the *denominator* for any firm-level benchmarking question of the form "are we paying above or below the typical industry token rate?" — a question TokenOps SaaS products implicitly answer through opaque proprietary baselines but which an open dataset like GATT can answer transparently.

GATT and TokenOps are not competing methodologies. They occupy distinct scales (global-macro vs. firm-micro) and serve distinct audiences (researchers / policy analysts vs. enterprise FinOps teams). The present paper proposes a productive division of labor: TokenOps platforms operationalize within-firm cost control; the Token Economy literature (this paper, NVIDIA GTC 2026 framing [28], Photons = Tokens physical-ceiling work [1]) provides the macro context within which firm-level decisions are made.

## 2.8 Sovereign Resource Framing: The Salt-and-Iron Analog

An eighth framing — historically the oldest of the eight, and currently the least articulated in academic or governmental literature — treats tokens as a *sovereign strategic resource* subject to potential state monopoly, mandatory fiscal extraction, or strategic reserve accumulation. The canonical precedent is Huan Kuan's *Discourses on Salt and Iron* (盐铁论, ca. 81 BCE) [33], the transcript of a Han-dynasty court debate over the policy — architected by Emperor Wu's finance minister Sang Hongyang (桑弘羊) — of nationalizing salt and iron production under state-owned monopolies. Sang Hongyang's structural argument was that salt and iron, as *universal inputs to economic activity with concentrated production geography and inelastic short-run demand*, were too fiscally and strategically consequential to remain entirely in private hands. The argumentative structure carries forward to AI inference tokens with notable directness:

| Structural feature | Han salt and iron (1st c. BCE) | AI inference tokens (2026) |
|---|---|---|
| Universal economic input | Salt as biological requirement; iron as tool / weapon input | Tokens as throughput unit for AI-enabled work across all sectors |
| Concentrated production geography | Coastal salt fields; specific iron-ore mountains | Frontier-model datacenter clusters in a small set of jurisdictions |
| Inelastic short-run demand | No substitute for biological / agricultural use | Workflows increasingly designed *around* AI inference |
| Fiscal extraction potential | Excise + state-monopoly margin captured as revenue | Token excise or state-operator margin (proposed; not implemented) |
| Cross-border arbitrage | Smuggling and jurisdictional price-differential trade | "Token Bill" cross-border flows documented by CSIS [21] |
| Strategic-reserve logic | State granaries; salt stockpiles in border garrisons | Sovereign compute / model-weight reserves (analog to SPR) |

The framing is, as of 2026-05-14, *absent* from formal Western policy literature we have located, and present only in fragmentary form in Chinese-government research outputs — CAICT [16] frames token throughput as a national-capability indicator without formally invoking a strategic-resource construct. It has, however, begun to surface in informed public discourse. The security researcher Yu Yang (TK), in a widely-read 2026-05-14 social-media post [34], observed that no government has yet conceptualized AI tokens as a strategic resource class, and conjectured that the Chinese government, if it did so, might establish state-owned token-infrastructure operators analogous to Sinopec (中石化) and PetroChina (中石油), and that a contemporary equivalent of the *Discourses on Salt and Iron* — a "Token Discourse" — could emerge from such a policy. We cite this not as policy doctrine but as evidence that the framing has begun to enter informed public discussion ahead of formal academic or governmental literature.

The sovereign-resource framing intersects GATT's empirical findings at three measurable points. First, the *concentration metric*: GATT's Appendix A shows that 87% of global token volume passes through the top four vendors, each headquartered in either the United States or China. This is the level of supply concentration that historically triggers state-monopoly debates — comparable to oil in the 1970s (the OPEC moment), telecommunications in the 1980s (Bell breakup), and search advertising in the 2010s (antitrust era). Second, the *fiscal-extraction base*: GATT's $97.0B/yr Token GDP is small relative to national tax bases today, but the §2.3-implied real-resource growth rate (the price-decline-adjusted residual after netting Epoch AI's [18] inference cost halving) projects the base to $0.5T–$1T/yr within the GATT v1.5 forecast window, at which point fiscal authorities will have a quantitatively material extraction target (worked illustration in §6.4). Third, the *geopolitical-asymmetry vector*: the 88/6 Token GDP split between the United States and China (§4.3), juxtaposed with 50/50 volume parity (§4.2), is the empirical signature of a strategically-asymmetric resource — production capacity present in both jurisdictions but value capture concentrated in one. In prior commodity cycles, this asymmetry pattern has been a leading indicator of state-monopoly or state-anchor-operator responses [35].

The sovereign-resource framing does not displace any of §2.1–§2.7. It complements them at a different level of analysis: GPT theory (§2.5) tells us tokens are a general-purpose input; the NVIDIA industry framing (§2.6) tells us they are a supply-side capacity product; TokenOps (§2.7) tells us they are a firm-level cost object. The sovereign-resource framing tells us that — conditional on §2.3 growth rates continuing — they will become a *state-level fiscal and strategic* object within the present decade. GATT's open dataset is intended to provide the empirical input to that policy debate before it is mediated through commercial-research opacity; §6.4 develops the policy-trajectory implications.

**Adjacent literature: capability sovereignty versus fiscal sovereignty.** Between the initial drafting of this section (2026-05-14) and the v1.5.1 revision (2026-05-15), a parallel literature on *sovereign AI* consolidated rapidly. MIT Technology Review's 2026-05-14 sovereignty piece [37] cites an EnterpriseDB survey of 2,050 senior executives in which 70% reported needing a sovereign data-and-AI platform, and quotes NVIDIA CEO Jensen Huang's appeal that each nation should "build your own AI, take advantage of your fundamental natural resource — your language and culture." Gartner's January 2026 forecast [38] projects 35% of countries locked into region-specific AI platforms by 2027 and 75% of European and Middle-Eastern enterprises geopatriating workloads by 2030. The World Economic Forum's April 2026 commentary [39] critiques the construct as "the myth of AI sovereignty"; Lawfare's analysis [40] frames the US position as a "sovereignty gap" in AI statecraft. By January 2026, the number of sovereign-AI projects had reached approximately 130 across more than 50 countries. This literature is *orthogonal* to the sovereign-resource framing developed in this section, not redundant with it, and the distinction is load-bearing for the §6.4 trajectory taxonomy. The sovereign-AI literature is principally about **capability sovereignty**: who controls model training, who hosts the weights, where the data is stored, which jurisdiction's chips power inference, and how a nation builds indigenous AI capability. GATT's salt-and-iron framing is principally about **fiscal sovereignty**: who extracts margin from token throughput, who operates the state-anchor token-infrastructure operator (Sang Hongyang's role), and who holds the sovereign token reserve. The two layers can co-occur or co-vary in any combination — a state can pursue capability sovereignty under laissez-faire fiscal posture (Trajectory A + capability buildout, the present US case), under utility-style regulation (Trajectory B + capability buildout, the present Chinese case per [41]), or under salt-and-iron monopoly (the hypothetical Trajectory C + capability buildout). Section 6.4 therefore treats capability sovereignty as a *fourth trajectory* (Trajectory D) that combines with Trajectories A, B, or C rather than competing with them, and credits the §2.8 framing with addressing the fiscal-sovereignty layer the sovereign-AI literature does not.

## 2.9 Where GATT Fits

Each of the four traditions covers part of the measurement problem. None covers the full territory:

| Approach | Geographic coverage | Vendor coverage | Update frequency | Unit |
|---|---|---|---|---|
| IDC / Gartner USD reports | Global / regional | Aggregate | Quarterly–annual | USD |
| IDC China MaaS report | China only | All major China vendors | Annual / semi-annual | Tokens (external only) |
| a16z / OpenRouter 100T study | Global | OpenRouter only | Periodic | Tokens (cumulative) |
| Vendor disclosures | Vendor-specific | One at a time | Irregular | Heterogeneous |
| Physics-ceiling models | Global | None | Static | Theoretical capacity |
| User surveys | Global | All major platforms | Periodic | Satisfaction scores |
| **GATT** | **Global** | **24 vendors, 12 countries** | **Daily** | **Tokens per day, all-sources** |

GATT does not replace any of these. It complements them: the empirical companion to physics-ceiling modeling (Litowitz et al.), the global counterpart to IDC's China-only token report, the all-vendor extension of OpenRouter's single-platform study, and the daily-frequency partner to the quarterly USD trackers. Section 5 develops the most consequential of these complementary relationships — with the Litowitz/Polson/Sokolov physical ceiling — in detail.

---

# 3. Methodology

GATT measures global AI inference token throughput as the sum of vendor-level estimates, with each estimate anchored to a dated source signal and updated via a transparent extrapolation rule. This section details how vendors are selected, how confidence is assigned, how the "all-sources" scope is operationalized, how daily values are computed between source updates, and how Token GDP and per-capita figures are derived. All design choices prioritize auditability over precision: every published figure can be traced to a specific source, a specific date, and a specific computational rule.

## 3.1 Vendor Coverage

GATT v0.82 (May 9, 2026) tracks 21 vendors selected by three criteria: (a) demonstrated daily token throughput exceeding 0.05 trillion (50 billion); (b) availability of at least one credible volume signal — official disclosure, ARR-and-pricing back-calculation, or platform aggregator data; and (c) representation across vendor types, including frontier closed models, open-weight foundation models, cloud-hosted aggregators, and consumer-facing chat assistants. The current list spans Chinese vendors (Doubao, Qwen, DeepSeek, Hy3/Hunyuan, Kimi, ERNIE, Spark, MiniMax, GLM, Xiaomi MiMo), United States vendors (Gemini, OpenAI, Anthropic, Microsoft Azure, OpenRouter, Grok, Groq, Meta Llama API, Amazon Bedrock, Perplexity), and one European vendor (Mistral).

Vendors are ordered by `daily_tokens_T` (total daily token throughput in trillions). The top ten in v0.82 are: Doubao (129T), Gemini (73T), OpenAI (45T), Anthropic (22T), DeepSeek (9.2T), Microsoft (10T), Qwen (6.2T), OpenRouter (3.0T), Hy3 (2.7T), and Kimi (2.5T). Several vendors known to operate at non-trivial scale are excluded — including most enterprise-only inference platforms and academic infrastructure — pending publishable signals.

Two structural caveats apply to vendor coverage. First, OpenRouter is an *aggregator*: tokens routed through it are also counted under their underlying vendor (Kimi, Anthropic, DeepSeek, etc.). The OpenRouter row is reported alongside an explicit `scope_note` flagging this overlap, and the global total nets the overlap out. Second, the boundary between "vendor" and "model" is occasionally blurry — for example, Xiaomi's MiMo-V2-Pro initially appeared anonymously on OpenRouter as "Hunter Alpha" before being reattributed [15]. GATT enters new vendors as soon as a credible signal emerges, with confidence rated accordingly.

## 3.2 Confidence Hierarchy

Each vendor entry carries a confidence rating drawn from four levels:

- **High** — direct vendor disclosure within the past 90 days (e.g., OpenAI's 15 billion tokens per minute API throughput; Pichai's 16 billion tokens per minute via direct API at Cloud Next 2026; Volcengine's 120 trillion tokens per day at the Wuhan AI Innovation Expo).
- **Medium-high** — a strong indirect signal (e.g., quarterly earnings disclosing AI-business ARR plus paid-seat counts) corroborated by at least one independent data point.
- **Medium** — multiple converging indirect signals (ARR plus pricing plus user count) without a direct throughput number.
- **Low** — single proxy signal, often months old.

The current distribution of confidence across the 24 vendors (post-v1.3 expansion) is: 3 High, 2 Medium-High, 8 Medium, 11 Low. This skew reflects the disclosure asymmetry between US and Chinese vendors: US vendors typically disclose ARR but not throughput; Chinese vendors increasingly disclose throughput but rarely ARR. Both kinds of signal are usable, but at different confidence levels.

This taxonomy is a working approximation. The Inference Bottleneck paper (arXiv:2604.17431) provides a more rigorous template — distinguishing observed, inferred, and judgment-based parameters, with explicit sensitivity analysis showing which conclusions are robust to perturbations [12]. GATT v0.83 will adopt this structure, augmenting (not replacing) the four-level confidence field.

## 3.3 All-Sources Scope (vs. IDC's External-MaaS-Only)

The scope decision is consequential and worth detailing. GATT counts a token if it is generated by an AI inference call attributed to a tracked vendor, regardless of whether the call originates externally (an enterprise API customer) or internally (the vendor's own consumer product, agent loop, or internal pipeline). For example, a token generated by ByteDance's Doubao foundation model is counted whether it is served to:

1. An external Volcengine MaaS customer via API;
2. A Douyin user receiving an AI-generated search overview;
3. A Doubao consumer-app user;
4. A Jimeng image-generation pipeline that calls Doubao for prompt expansion;
5. An internal Volcengine workflow (data labeling, code review, agent orchestration).

IDC's *China Public Cloud Large Model Services* report [4] explicitly excludes categories (2)–(5), stating that statistics cover "large model public cloud service call volume provided by major cloud vendors to external customers, excluding self-service business calls."

The two scopes can be reconciled with arithmetic. IDC's 2025 China total of 1,944 trillion tokens for the full year averages to approximately 5.32 trillion tokens per day. Volcengine's IDC market share of 49.5% for full-year 2025 yields approximately 2.64 trillion tokens per day in external MaaS volume. Volcengine's officially disclosed 120 trillion tokens per day, dated April 1, 2026, is a factor of 45 larger. No plausible growth path between January and April closes this gap; the only interpretation is that more than 95% of Volcengine's measured throughput is internal first-party usage that lies outside IDC's scope.

GATT therefore reports Doubao (Volcengine's flagship model) at 129 trillion tokens per day for May 11, 2026, with a `scope_note` field explicitly marking this as all-sources. The IDC validation block in `data/tci-latest.json` documents that GATT and IDC agree on Volcengine's #1 position in China while disagreeing on the absolute volume, with the scope difference fully accounting for the gap.

For non-Chinese vendors, the all-sources scope is generally less consequential because the largest internal first-party deployments are smaller relative to external API. Gemini's "All Surfaces" estimate (Search AI Overviews + Gemini App + Workspace + Cloud API) uses a 3.2× multiplier on the disclosed direct-API number; this is an attribution choice rather than a scope expansion, and Section 5 discusses its potential overestimation.

### 3.3.1 Gross vs. Value-Added: A Necessary Caveat

The all-sources scope choice raises a question that national accounts have grappled with since Hulten (1978) and the SNA 2008 framework: should the headline aggregate measure *gross output* (every transaction, including intermediate inputs) or *value-added* (final consumption only, with intermediate goods netted out)? GATT's all-sources methodology is closer to gross output: tokens consumed by Douyin's recommendation system as an intermediate input to a user-facing video feed are summed alongside Claude tokens consumed as final-consumption end-user assistance. This is a genuine measurement choice with consequences.

Three observations frame the choice:

First, the analogous decision in national accounts is well understood. Headline GDP is value-added (~$25 trillion US 2026); gross output (intermediate plus final) is approximately 1.7× larger. Both are published; both are useful for different questions. GATT publishes the gross construct because the value-added construct would require netting agent-loop tokens from final-output tokens, which no vendor discloses with the granularity needed.

Second, the volume parity finding (China-US 50/50) is partially an artifact of vertical integration vs. modular architecture. ByteDance vertically integrates Doubao into Douyin, the Doubao consumer app, and Jimeng — all of which generate intermediate-input token consumption that GATT counts. The US ecosystem is more modular: OpenAI sells API tokens; Anthropic sells API tokens; the customer's downstream pipeline tokens are consumed at the customer's account, not OpenAI's. A strict value-added comparison would likely show a wider US lead in final-consumption tokens than the gross 50/50 implies. Future GATT versions (v0.84+) will explore netting out one well-documented internal pipeline (e.g., Doubao prompt expansion calls inside the Jimeng image-generation pipeline) as a methodological probe.

Third, this caveat does not invalidate the gross construct — it constrains its interpretation. The 50/50 volume parity is an accurate measurement of *gross* token consumption attributable to each region's vendor base. Readers comparing GATT to a value-added counterpart would expect the US share to rise. We therefore frame the headline finding as "gross token volume parity, with the US over-represented in final-consumption value capture" rather than as parity simpliciter.

## 3.4 Extrapolation Engine

Vendor disclosures are sporadic. A typical pattern is a single high-confidence signal — for example, a quarterly earnings call — followed by 60-90 days of silence. To produce a daily index, GATT extrapolates between disclosures.

The extrapolation rule is straightforward. For each vendor `v` with the most recent source value `s_v` dated `d_v` and assigned monthly growth rate `g_v`, the value on day `t` is:

$$ v(t) = s_v \cdot (1 + g_v)^{(t - d_v)/30} $$

The monthly growth rate `g_v` is set by editorial judgment based on observed multi-period trajectories, capped at 30% per month for new high-momentum vendors (e.g., Kimi K2.6 post-launch) and floored at -5% per month for declining vendors (e.g., Grok in May 2026). The rate is reviewed weekly and updated when new signals arrive. Vendors with no recent disclosure default to 8% per month, reflecting a 2025-2026 baseline median across the index.

The extrapolation engine runs in the browser when readers load the dashboard, recomputing each vendor's `live` value from the latest snapshot file. Snapshot files (`data/snapshots/YYYY-MM-DD.json`) freeze each day's state for reproducibility; this paper draws all empirical figures from the May 9, 2026 snapshot. The headline number visible on the dashboard is therefore best understood as *anchor-extrapolated*, not freshly measured: it represents the most recent direct disclosure for each vendor projected forward at the editorial growth rate.

### 3.4.1 Anchor Age and Backtest

The honest framing of GATT's "daily" headline requires reporting the underlying anchor age. Table 1 summarizes the volume-weighted anchor age and growth rate for the top 10 vendors (which collectively cover approximately 97% of global volume) as of May 11, 2026:

| Vendor | Daily T | Anchor date | Anchor age (days) | g_v (%/mo) | Volume × age |
|---|---:|:---:|---:|---:|---:|
| Doubao | 129 | 2026-04-07 | 32 | 8 | 4128 |
| Gemini | 73 | 2026-04-09 | 30 | 10 | 2190 |
| OpenAI | 45 | 2026-05-05 | 4 | 15 | 180 |
| Anthropic | 22 | 2026-04-16 | 23 | 18 | 506 |
| Microsoft | 10 | 2026-04-29 | 10 | 10 | 100 |
| DeepSeek | 9.2 | 2026-04-24 | 15 | 10 | 138 |
| Qwen | 6.2 | 2026-04-02 | 37 | 8 | 229 |
| OpenRouter | 3.0 | 2026-04-30 | 9 | 10 | 27 |
| Hy3 | 2.7 | 2026-04-23 | 16 | 12 | 43 |
| Kimi | 2.5 | 2026-04-20 | 19 | 30 | 47 |

The volume-weighted mean anchor age for the top 10 is approximately **24 days**. The most stale top-tier anchor is Qwen (37 days), pending the Alibaba Q1 2026 earnings disclosure expected in May. The freshest is OpenAI (4 days) following the May 5 GPT-5.5 Instant launch.

We ran a five-day backtest comparing the v0.79 snapshot (May 4, 2026) extrapolated forward five days using the engine to the v0.82 anchored values (May 9). For the four vendors that received fresh anchors in this window (Gemini, Anthropic, Microsoft, OpenAI), the engine's pure-extrapolation prediction differed from the anchored update by a volume-weighted **+15.3%** (engine under-predicted, primarily because the Gemini Cloud Next 2026 disclosure of 16B tokens/min via API was a step-change rather than smooth growth). For the six top-10 vendors that did not receive fresh anchors (Doubao, DeepSeek, Qwen, OpenRouter, Hy3, Kimi), the engine prediction was within ±2% of the manually-adjusted v0.82 values, validating the engine's accuracy in the absence of step-changes. The implication: the extrapolation engine is reliable between disclosures but cannot anticipate large vendor announcements; readers should treat the headline as accurate to within ~10% during quiet news weeks and within ~25% during active disclosure windows.

The default 8%/month growth rate is calibrated to the Epoch AI inference-cost panel (Sevilla et al., reference [18]): Epoch reports cost-per-fixed-capability halving every two months, equivalent to a ~30%/month price decline. If volume grows at 22%/month (the 2026 GATT-implied rate), the implied real-resource expansion is approximately +50%/month — consistent with hyperscaler capex trajectories ($602B in 2026, +36% YoY) but at the upper end. Vendor-specific growth rates deviate from the 8%/month default when vendor-specific signals (Anthropic's MAU surge, Grok's user decline) override the field default.

## 3.5 Token GDP

Token GDP is GATT's normalization for cross-vendor and cross-region economic comparison. It is defined as:

$$ \text{Token GDP} = \sum_v v(t) \cdot p_{r(v)} $$

where `r(v)` is the region of vendor `v` and `p_{r(v)}` is the regional blended price per million tokens. Current pricing assumptions (May 2026) are:

- United States: $1.50 per million tokens
- Europe: $1.20 per million tokens
- China: $0.10 per million tokens
- Rest of World: $0.90 per million tokens

These are vendor-volume-weighted blends across input and output token rates and across the model lineup typical for each region. They are intentionally point-in-time. Xing [6] documents that GPT-4-equivalent pricing fell from approximately $60 per million tokens in early 2023 to under $1.50 per million in early 2025 — a 40-fold compression in 24 months. Epoch AI [18] reports a complementary finding from a longitudinal inference-cost panel: cost at fixed performance level halves every two months across the 2024-2026 window. SemiAnalysis [22] independently reports a 1200× compression for GPT-3-class inference cost over a similar window. The three measurements agree in direction and magnitude. Any analysis quoting Token GDP must accompany the figure with an as-of date and a note that the implicit pricing assumptions may have shifted by the time of citation.

For May 11, 2026, GATT computes daily Token GDP at $265.8 million, or $97.0 billion annualized. The regional breakdown is striking: the United States contributes $234 million per day (88% of the total) on 156 trillion tokens (post-v1.3 Apple Intelligence cloud-routed addition of 2T); China contributes $15.4 million per day (6%) on 154 trillion tokens. The pricing gap is approximately 15× and is the principal driver of the regional Token GDP asymmetry — not a volume difference.

### 3.5.1 What "Token GDP" Is and Is Not

The label "Token GDP" carries economic baggage that requires explicit framing. National accounts GDP, since Hulten (1978) and codified in SNA 2008, measures *value-added* — gross output net of intermediate inputs — and uses *transacted* prices. GATT's Token GDP construct departs from this standard in two ways.

First, as Section 3.3.1 details, GATT's all-sources volume basis is closer to gross output than to value-added. Doubao tokens consumed by Douyin's recommendation system as an intermediate input are summed alongside Claude tokens consumed as final-consumption end-user assistance.

Second, GATT applies retail menu prices ($1.50/M for US blended, $0.10/M for CN blended) to all volume — including the substantial fraction (>95% for Volcengine per the Section 3.3 arithmetic) that is *not* transacted at retail. The internal Doubao calls inside ByteDance's pipelines are not actually billed; assigning them a counterfactual retail price ("what would this cost on the API menu") is a comparability device, not an observed price.

The Token GDP construct is therefore best understood as a **counterfactual retail-equivalent valuation of gross token output**, not a national-accounts-style value-added measure. Readers comparing Token GDP to USD-priced AI infrastructure spending (e.g., IDC's $758B 2029 forecast [7]) should note that the constructs are not directly comparable: IDC measures money actually flowing; Token GDP measures the retail-equivalent value of all token consumption regardless of whether transacted. Future versions will explore (a) a value-added variant that nets out tracked internal-pipeline calls, and (b) a transaction-based variant that prices internal calls at internal-cost rather than retail. Both are substantial methodological extensions and are flagged for v1.0.

We retain the "Token GDP" label because the construct is parallel to GDP in spirit — an aggregate economic-value measure across a defined production base — but commit in this paper to using "Token GDP (retail-equivalent gross)" or "TGE" in the manuscript whenever the gross-vs-value-added distinction matters, and to encouraging downstream researchers to compute alternative variants from the open dataset.

**Illustrative value-added correction.** A first-order estimate of how Token GDP would shift under value-added accounting is informative. Volcengine's all-sources Doubao volume includes substantial intermediate-input usage: Douyin AI Search recommendation calls, Doubao consumer chat, Jimeng image-generation prompt expansion, internal Volcengine pipeline workflows. Even if intermediate-input tokens represent half of all Chinese vendor volume (a conservative estimate, given the IDC arithmetic implies >95% of Volcengine throughput is internal first-party), netting them out would reduce China's value-added token volume by roughly 50%. US vendors are more modular — token sales between OpenAI/Anthropic and downstream API customers are arms-length transactions and would survive value-added netting more intact — though some intermediate-input volume exists (Microsoft Copilot's internal Azure usage, for instance). Applying a conservative 0.4-0.6× value-added scalar to gross Token GDP yields the following illustrative correction:

| Region | Gross Token GDP (% of $97.0B/yr) | Value-added scalar (illustrative) | VA Token GDP share |
|---|:---:|:---:|:---:|
| United States | 88% | ~0.7× | ~75-82% |
| China | 6% | ~0.4× | ~3-4% |
| Europe | 4% | ~0.6× | ~2-3% |
| Rest of World | 2% | ~0.6× | ~1-2% |

The qualitative finding — US Token GDP dominance — survives the value-added correction; the quantitative magnitude shifts modestly (88% → 75-82% US share). The China value-added share contracts further (6% → 3-4%) reflecting the heavily vertical-integrated structure of Chinese AI deployment. Readers citing GATT's headline 88/6 split for policy debates should note that under value-added accounting the gap widens, not narrows. The 0.4× and 0.7× scalars used here are illustrative; a rigorous decomposition awaits vendor cost-disclosure data we do not yet have.

**The Zhuang et al. (2025) Inference Production Frontier [11]** is the most natural theoretical refinement: blended prices should ideally reflect observed production-cost curves and demand elasticities rather than retail menu prices. GATT v0.83+ will incorporate this where vendor cost data permits, alongside the value-added decomposition above.

## 3.6 Per-Capita Calculation

Per-capita figures use the standard formula:

$$ \text{tokens per person per day} = \frac{\text{country tokens}}{\text{country population}} $$

Country tokens are computed by attributing each vendor's daily volume to its primary country of operation. For vendors with substantial cross-border deployment (notably Microsoft and Anthropic, with significant European customer bases), GATT applies a simplifying assumption that aggregate vendor volume rolls up to the vendor's headquarters country. This is a known limitation; v0.83+ will explore vendor-region splits where data permits.

Twelve countries are currently tracked: United States, China, United Kingdom, France, Germany, Japan, South Korea, Canada, India, Brazil, Saudi Arabia, and Indonesia. Other geographies are aggregated into "Rest of World." Population figures are sourced from World Bank 2024 estimates.

The headline per-capita statistic — 459,700 tokens per United States resident per day in May 2026 — is the figure that the Litowitz et al. paper's 2028 ceiling of 225,000 tokens per resident is most directly comparable with. Section 5 develops the comparison.

## 3.7 Revision Discipline

GATT publishes a `revision_history` array for every vendor entry, listing prior values, dates, and reasons for change. The dashboard exposes a "correction log" view that surfaces changes across the index. This discipline is intended to make the dataset auditable: any reader who disagrees with a value can read the source signals and the chain of revisions back to the most recent direct disclosure.

The dataset is released under CC BY 4.0 and versioned via Git. Each version (v0.82 at the time of writing) is reproducible by checking out the corresponding tag. `data/snapshots/YYYY-MM-DD.json` files freeze the index state on each daily release and are immutable. The full Git history is preserved on GitHub with no force-pushes to main.

This auditability is the methodology's strongest claim. It does not eliminate measurement error — the index will continue to revise as better signals arrive — but it ensures that error is detectable, attributable, and correctable. As one of the productive results of the Section 5 reconciliation with the Litowitz et al. physical ceiling, GATT v0.83 commits to publishing sensitivity bands alongside point estimates, addressing the most common request from external readers thus far.

---

# 4. Empirical Findings

This section reports headline findings from the GATT v1.4 dataset as of May 11, 2026. All figures are reproducible from `data/tci-latest.json` (immutable v1.0 baseline at `data/snapshots/2026-05-09.json`; v1.3 vendor expansion and v1.4 methodology integration in current). Where a figure depends on extrapolation between disclosures, the source date and growth-rate assumption are documented in the corresponding vendor entry's `revision_history`.

## 4.1 Global Volume

Global daily AI inference output stands at **311 trillion tokens per day** as of May 11, 2026. The headline figure aggregates 24 tracked vendors across 12 countries (21 vendors at v1.0 publication state plus Apple Intelligence cloud-routed, Cohere, and Sarvam AI added in v1.3), with a small "Rest of World" residual covering geographies not yet broken out individually. Growth has run at approximately 22% per month over the preceding eight weeks — a doubling time of roughly 3.5 months. Extrapolating this rate forward through year-end 2026 yields a projection band of **1.1 to 1.5 quadrillion tokens per day** by December 2026, with the conservative end of the band assuming growth deceleration to 18% per month and the aggressive end assuming sustained 22% per month.

The 311T figure is itself the result of substantial recent revisions. GATT v0.79 (May 4, 2026) reported 264T per day; v0.80 (also May 9) raised this to 305T after seven vendor anchor upgrades reflecting Pichai's 16-billion-tokens-per-minute Q1 disclosure, Anthropic's Opus 4.7 launch and 44% MAU surge, Microsoft's Q3 FY26 $37B AI ARR earnings release, Kimi K2.6's launch and ARR doubling, DeepSeek V4 Pro/Flash's launch, and minor adjustments to Qwen and Hunyuan. v0.81 added 5 trillion tokens per day from third-party revisions (OpenRouter platform data, Perplexity user metrics, and the new Xiaomi MiMo entry). The week-over-week swing from 264T to 310T (+17%) reflects measurement-update density rather than a single underlying growth event; vendor activity in the April 1 to May 9 window was unusually rich in publishable signals.

### 4.1.1 Sensitivity Band on the Headline

The 311T point estimate carries methodological uncertainty that warrants explicit bracketing. Following the parameter classification template from Inference Bottleneck [12] (observed / inferred / judgment-based), GATT publishes three scenarios for the headline global figure:

| Scenario | Global daily tokens (T) | Methodology |
|---|---:|---|
| Conservative | 250 | Photons=Tokens-anchored: trim Gemini All-Surfaces multiplier 3.2× → 2.5×; trim Doubao all-sources by 5% (cache adjustment); apply 15% reduction across vendors with low-confidence ratings |
| **Best estimate** | **311** | **GATT v1.4 published values; vendor-volume-weighted, all-sources, May 11, 2026 anchored** |
| Aggressive | 400 | 22%/mo growth assumption holds through end-Q2 2026; assumes 1-2 additional Pichai-class US disclosures by mid-June |

The conservative bound (250T) maintains all five qualitative GATT findings — China-US volume near-parity (53/47 in conservative), US Token GDP dominance ≥85%, per-capita gap ≥450× US/India, growth trajectory positive, and the 2× tension with the Photons=Tokens 2028 ceiling persists (350K conservative US per-capita > 225K ceiling). The qualitative robustness of GATT's headline claims to conservative recalibration is, in our judgment, the strongest argument for citing GATT figures despite the unavoidable measurement uncertainty in the underlying vendor data.

## 4.2 Volume Parity Between China and the United States

For the first time since GATT began publishing in February 2026, the China and United States token-volume shares are essentially tied. As of May 11 (post-v1.3 expansion that added Apple Intelligence 2T to the US side): **United States 50.2% of global volume (156 trillion tokens per day)**, **China 49.5% (154 trillion tokens per day)**, with Europe at ~0.24% (0.74 trillion, dominated by Mistral and Cohere) and the Rest of World residual at the remainder. At v1.0 publication state (May 9, 2026, pre-Apple) the two were exactly tied at 154T each; the v1.3 expansion places the US marginally ahead.

The convergence is recent. On April 6, 2026, GATT v0.75 measured China at 58% and the United States at 35%. The 5-week shift to 50/50 reflects new United States hard-data disclosures rather than slowed Chinese growth: Pichai's 16-billion-tokens-per-minute API disclosure (a 60% quarter-over-quarter increase from Q4 2025's 10 billion) raised Gemini's All Surfaces estimate from 57T to 73T; Microsoft's Q3 FY26 disclosure of $37 billion AI business ARR (+123% year-over-year) and 20 million paid Copilot seats raised Microsoft's estimate from 8.1T to 10T; OpenAI's GPT-5.5 launch (April 23) and GPT-5.5 Instant rollout (May 5) raised OpenAI's estimate from 40T to 45T; Anthropic's Opus 4.7 launch (April 16, with a new tokenizer producing up to 35% more tokens per equivalent input) plus 44% Claude monthly-active-user growth raised Anthropic from 15T to 22T. China's leaders held steady on extrapolation through the same window, with no comparably large new disclosures.

The volume parity is the headline geo-economic finding of the v0.82 release. It does not, however, imply economic parity — see Section 4.3.

## 4.3 Token GDP Asymmetry

Daily Token GDP — vendor volume × regional blended price (Section 3.5) — totals **$265.8 million per day** ($97.0 billion annualized) post-v1.3 expansion. The regional split is the inverse of volume:

- **United States: $234 million per day, 88% of global Token GDP, on 50.2% of volume.**
- **China: $15.4 million per day, 6% of global Token GDP, on 49.5% of volume.**
- Europe: $10.8 million per day, 4% of Token GDP, on 0.24% of volume.
- Rest of World: $5.6 million per day, 2% of Token GDP, on 2.0% of volume (post-v1.3 Cohere + Sarvam additions).

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

### 4.4.1 Distributional Summary: Gini and Lorenz

The 597× United States-India ratio is a single-pair statistic. To summarize the full distribution, we compute the **population-weighted Gini coefficient** and the implied Lorenz curve across the twelve countries broken out in the dataset (which collectively cover approximately 51% of global population; the unrepresented residual is mostly low-per-capita and would push the global Gini higher rather than lower). The reproducibility script is `paper/scripts/token_gini.py`.

The result:

| Measure | Value |
|---|---:|
| Population-weighted Gini coefficient (12 countries) | **0.674** |
| Top 10% of population's share of token consumption | 50.2% |
| Top 1% of population's share | 6.0% |
| Bottom 50% of population's share | **1.4%** |

For comparison: cross-country income Gini (PPP-adjusted, 2024 World Bank) is approximately 0.62; pre-tax US wealth Gini is approximately 0.85. **Token consumption inequality has already exceeded global income inequality and approaches wealth-distribution levels of concentration.** This is consistent with Crawford [19]'s framing of AI infrastructure as a planetary-scale system whose access concentrates among a small number of populations and regions; the Gini number is the empirical scalar form of that concern.

The Lorenz curve (formal computation in the script) shows a particularly sharp inflection at the China-US transition: the bottom 92% of the represented population (everyone outside the United States) collectively accounts for 52% of token volume, while the top 8% (the United States) accounts for the remaining 48%. This is the structural consequence of the 50/50 China-US volume parity finding combined with China's 4.2× larger population.

**A caveat on interpretation.** The Gini above captures *vendor-attributed* per-capita consumption; it does not measure individual-level consumption within countries (which would require a wholly different data source, since GATT cannot observe per-user activity). Within-country distribution may also be highly unequal: a small fraction of US users likely accounts for a disproportionate share of US token volume. The 0.674 figure therefore *under*-states the true individual-level Gini, possibly substantially. We flag a within-country decomposition as future work but emphasize that even the conservative cross-country measurement establishes that token consumption is more unequally distributed than income at the global scale — already, in 2026, before the technology is broadly diffused.

## 4.5 Top Vendor Findings

The top four vendors account for **87% of global volume**:

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

---

# 5. The 2× Discrepancy with Photons = Tokens

This section returns to the question that opened the paper. Litowitz, Polson, and Sokolov [1] project that the 2028 United States AI energy allocation of 326 TWh can support roughly 6.5 × 10¹⁷ tokens per year, equivalently 225,000 tokens per resident per day. GATT v0.82 measures United States per-capita throughput at 459,700 tokens per resident per day in May 2026 — eighteen months *before* the paper's projection date, yet **2.04× above the paper's 2028 ceiling**.

Both numbers are produced carefully. We argue that the gap reflects three compounding factors, each of which can be quantified, and that the *informative* interpretation of the discrepancy is methodological complementarity rather than measurement error.

**This section is offered as a falsifiable hypothesis for joint refinement, not as a closed argument.** GATT v1.0 has been substantially revised in response to peer review from the Litowitz-Polson-Sokolov co-author team itself; we acknowledge the resulting decomposition is under-identified (three latent factors against one observable) and report a Bayesian sensitivity analysis (Appendix C) rather than a unique solution. Section 5.5.7 below proposes specific empirical measurement work — a co-authored energy-per-token benchmarking study on representative 2026 inference deployments — as the natural next step for jointly tightening the parameter ranges. The *companion paper* framing of this manuscript is real: this section is the pitch document for that collaboration.

## 5.1 Restating the Discrepancy

The Litowitz et al. ceiling derives from three inputs: a 326 TWh US AI energy allocation projected for 2028, Landauer's information-theoretic minimum energy cost per bit, and a Shannon-channel capacity calibration anchored to GPT-4-class inference efficiency. Their token-budget framework is rigorous within these assumptions and produces a meaningful upper bound on token production under fixed inputs. The 225,000 tokens-per-resident-per-day figure is the per-capita normalization of their aggregate ceiling under 2028 US population estimates.

The GATT empirical figure derives from twenty-four vendor-level estimates summed into a national total, divided by US population. Each vendor estimate is anchored in a dated source signal — a vendor disclosure, an ARR-and-pricing back-calculation, or platform-aggregator data — and updated via the extrapolation engine described in Section 3.4.

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

**Pre-registered numerical prediction (falsifiable test of the §5.5 decomposition).** The Appendix C Bayesian sensitivity analysis identifies a fourth factor — the theoretical-vs-empirical hardware-utilization scalar $\eta$ — whose value is not yet measured but which closes the §5.5 decomposition residual. We commit, in advance of any measurement, to a specific prediction:

> When 2027 vendor disclosures or third-party benchmarking studies report aggregate hardware-utilization figures for representative production inference deployments (H100/H200 clusters serving Anthropic, OpenAI, Google, ByteDance, DeepSeek workloads), **the volume-weighted average will fall in the range $\eta \in [0.30, 0.50]$**, with central expectation $\eta \approx 0.40$.

The falsification rule:

- **Confirmation** ($\eta \in [0.30, 0.50]$): the §5.5 decomposition + Appendix C fourth factor are jointly consistent with observed deployment efficiency. Joint posterior of the four-factor model achieves the observed 2.04× ratio at central values.
- **Falsification at the upper end** ($\eta > 0.70$): production hardware is running close to theoretical peak. The §5.5 decomposition's per-factor central values overstate efficiency gains; either Interpretation 2 is too aggressive (tokens-per-Joule lift ≪ 3×) or Interpretation 3 is too aggressive (cache-hit dominance smaller than 1.4×). Section 5 must be re-derived.
- **Falsification at the lower end** ($\eta < 0.20$): production hardware is running so far below theoretical peak that capacity is essentially software-throttled, not hardware-bounded. The Litowitz-Polson-Sokolov physical ceiling has unstated assumptions about scheduler efficiency that are doing more work than acknowledged; the framework needs an explicit utilization parameter, not an implicit assumption of full deployment.

This is **not** a forecast that "such a study will happen by 2027." It is a conditional prediction: *if* such a study is published, *then* the central tendency should fall in the stated range. The prediction is registered here, in v1.0, against future evidence. We invite Epoch AI [18], the Inference Bottleneck working group [12], or the SemiAnalysis team [22] to take the measurement, and we commit to publishing a v1.x revision either confirming or retracting this prediction within six months of the measurement's release.

This level of pre-registration moves the §5.5 decomposition from "a plausible reconciliation hypothesis" (its v0.92 status) to "a hypothesis with a specific empirical falsification target" (its v1.0 status). Polson's Bayesian-statistics critique was that consistency-checking is not identification; pre-registered prediction with falsification thresholds is the appropriate step beyond consistency-checking, short of full identification.

### 5.5.8 Token Velocity as a Unifying Macro Frame

The §5.5 decomposition treats $G$, $L$, $G^{*}$, and $L^{*}$ as point quantities and reasons about their ratios. A complementary framing — closer to monetary macroeconomics than to physics-ceiling accounting — is to treat the same quantities as a quantity-equation system parallel to Fisher's $M \cdot V = P \cdot Q$.

Define:

- **Token money supply** $M \equiv L_{\text{eff}}$, the *effective* fresh-compute capacity, where $L_{\text{eff}}$ is the Litowitz-Polson-Sokolov 2028 ceiling adjusted for two factors: the Section 5.3 efficiency recalibration ($L^{*}/L = 3.0$ central) and the Appendix C "fourth factor" — a hardware-utilization scalar capturing the gap between theoretical peak and observed-in-production deployment ($\eta \approx 0.3-0.5$). Concretely, $L_{\text{eff}} = L \cdot (L^{*}/L) \cdot \eta$, with central values $L_{\text{eff}} = 225 \times 3.0 \times 0.4 = 270$K tokens/resident/day of *deliverable* fresh-compute capacity.
- **Token velocity** $V \equiv G^{*}/L^{*}$, the emitted-vs-fresh-compute multiplier of Interpretation 3. Currently estimated at $V \approx 1.4$ with plausible range $[1.25, 1.65]$, dominated by KV-cache reuse and batched attention. Velocity in this sense is a measurement of *how many emitted tokens each unit of fresh compute supports* — exactly analogous to monetary velocity, which measures how many transactions each unit of money supports.
- **Token price level** $P$, the regional blended price per million tokens (US \$1.50, China \$0.10, Europe \$1.20, ROW \$0.90 per the Section 3.5 schedule).
- **Token GDP volume** $Q \equiv G^{*}$, the overestimation-corrected emitted-token output.

The quantity equation:

$$
M \cdot V = Q
$$

(with units of tokens per resident per day, and Token GDP recoverable as $P \cdot Q$).

Three substantive implications follow.

**First, the §5.5 decomposition collapses to a velocity statement.** The 2.04× tension between $G$ and $L$ is, in this frame, the joint product of an under-estimated capacity ($M$ is roughly $L_{\text{eff}}$, not $L$) and a velocity multiplier ($V \approx 1.4$). Section 5.5.5's "$G^{*}/L^{*}$" factor *is* token velocity; calling it that surfaces its similarity to a well-understood macro variable rather than treating it as an idiosyncratic ratio.

**Second, the Appendix C fourth factor lives on the $M$ side, not the velocity side.** The honest finding from the Bayesian sensitivity analysis is that the §5.5 decomposition's per-factor central values overstate the implied gap by ~2.3× under any plausible correlation structure. This residual is most parsimoniously explained as a hardware-utilization scalar $\eta$ that reduces the effective money supply, not as additional velocity. The distinction matters because the policy implications differ: a low-$\eta$ economy (production hardware running at 30-50% of theoretical peak) responds to different interventions than a low-velocity economy (low cache reuse, sparse batching). The first invites infrastructure investment; the second invites software-stack optimization.

**Third, velocity is a measurable, predictively useful quantity.** Token velocity has direct empirical proxies — KV-cache hit rates, attention-batching factors, prefix-sharing across sessions — that production inference operators measure routinely but rarely publish. A coordinated cross-vendor study reporting $V$ in the same way Epoch AI [18] reports inference cost would convert "is the gap real?" into "is velocity rising or falling, and at what rate?" Cross-checking against Epoch's panel: if cost-per-fixed-capability halves every two months [18] but $V$ holds constant, then physical-capacity expansion accounts for the entire gain; if $V$ rises in parallel, software efficiency is contributing too. Each of those two findings would have distinct implications for hyperscaler capex elasticity.

The macro-quantity-equation framing is offered as conceptual scaffolding, not as a complete theory. The most direct contributions of this subsection are: (a) renaming "Interpretation 3" as **token velocity** and aligning it with a familiar macro variable; (b) locating the Appendix C fourth factor on the *capacity* side rather than as a velocity correction; and (c) suggesting that velocity itself, $V$, is the most useful single forward-looking variable for tracking the Token Economy — more so than headline volume, more so even than Token GDP at fixed prices.

## 5.6 Implications for Methodology

The reconciliation has three constructive consequences for GATT and one for physical-ceiling modeling.

For GATT, v0.83 will: (a) adopt the observed/inferred/judgment parameter classification from the Inference Bottleneck paper [12] as a richer alternative to the four-level confidence rating; (b) publish sensitivity bands for headline figures, with conservative bounds anchored to physics-ceiling assumptions and aggressive bounds matching current empirical extrapolation; and (c) attach explicit as-of dates to all blended pricing assumptions, consistent with Xing's [6] documentation of 40× pricing decline over 24 months.

For physical-ceiling modeling, the comparison suggests that updating efficiency calibrations from GPT-4-class baselines to 2026 frontier-deployment baselines (MoE activation rates, quantization, ASIC efficiency) is a high-leverage methodological refinement. The Litowitz et al. framework remains correct in structure; the calibration inputs are where the action is.

The deeper point is that empirical tracking and physical-bound modeling are productive complements. Each catches what the other misses. The Token Economy needs both.

---

# 6. Discussion

## 6.1 Policy Implications Worth Investigating

The Section 4 finding that China and the United States are tied at 50% / 50% on token volume but split 6% / 88% on Token GDP raises questions for AI governance research that this paper does not resolve, but flags as worth investigating empirically. Two stand out.

First, **volume parity should not be conflated with AI parity**. Headlines about Chinese AI catching up frequently cite token volume; this paper documents that gross volume parity has arrived in May 2026. But Token GDP share — at current retail-equivalent pricing — remains heavily US-tilted. Whether the underlying 15× pricing gap reflects durable model-capability differences or transient market structure is an open question. The pricing gap has held at roughly 15× across the May 2025 to May 2026 window per the GATT dataset's price-history block, but a single year is insufficient to establish durability. A longitudinal pricing-gap analysis covering 2024-2027 would be the appropriate empirical test before drawing policy conclusions; we flag this as future work rather than asserting a policy implication.

Second, **per-capita metrics may belong in AI development indices**, akin to how GDP per capita supplements aggregate GDP in macroeconomic comparison. The 597× United States–India gap is the central distributional finding of the dataset, but its policy interpretation depends on counterfactuals: what fraction of the gap reflects access-constrained latent demand versus productively-applied AI versus passive AI consumption (chat-style entertainment)? GATT does not yet decompose volume by use category; doing so (per the v0.84 roadmap) is a precondition for moving from descriptive observation to actionable policy framing.

Xing's [6] proposed token futures market is conditional on the existence of a credible Token Performance Index — exactly the kind of artifact that GATT prototypes. If such a market launches in 2027-2028 as Xing projects, the empirical index underlying contract pricing will need to handle vendor disclosure asymmetry, scope normalization (all-sources vs. external), and pricing volatility (40× compression in 24 months per Xing; 1200× for older tiers per SemiAnalysis [22]). GATT's revision discipline and open methodology are designed to scale into that role.

The "Token Bill" framing has already entered policy discourse. CSIS's April 2026 analysis [21] uses the term to describe the phenomenon of American enterprises discreetly running Chinese AI inference for cost reasons, suggesting that the regional Token GDP asymmetry has practical consequences for cross-border AI economic flows. GATT's open dataset is intended to inform this debate with transparent measurement rather than commercial-research opacity.

## 6.2 Geo-Economic Implications

Three observations bear on the geo-economics of AI.

First, **China's 50% volume share is dominated by internal first-party usage**, per the Section 3.3 IDC arithmetic showing more than 95% of Volcengine's measured throughput is internal (Douyin AI Search, the Doubao consumer app, the Jimeng image-generation pipeline) rather than external MaaS. This is a structural fact about Chinese AI deployment that may have export-control implications: restrictions on inference chips that target enterprise MaaS deployment have limited reach into vertically-integrated internal supply chains. We flag this as a hypothesis that policy researchers can test empirically — comparing US export-control efficacy against vertically-integrated vs. modular vendor deployments.

Second, **the efficiency-margin question deserves empirical testing**. Section 5 proposed (without claiming to prove) a 3-5× lift in effective tokens-per-Joule between 2024-vintage dense-FP16 baselines and 2026 MoE/quantization/ASIC deployments. If this range is correct, hardware restrictions that delay efficiency-frontier adoption by even one generation could substantially reshape the global token landscape. Conversely, if the efficiency lift is smaller — say 2× — export-control efficacy would be more durable. The Section 5.5 decomposition is offered as a hypothesis whose factor ranges can be empirically tightened by future work; we do not assert specific export-control conclusions in advance of that work.

Third, **the 597× United States–India per-capita gap is a structural inequality outside the China–US frame**. India ranks 11th globally on per-capita token throughput (770 tokens per resident per day) despite ranking 9th in absolute volume (1.10 trillion per day). Population scale dilutes the metric, but the underlying access disparity is real: most AI-driven productivity gains are accruing to a small per-capita-rich set of countries, with India and Indonesia representing population-weighted majorities of the global Rest-of-World residual. Crawford [19] frames AI infrastructure as a planetary-scale system whose externalities and access patterns concentrate among a small number of populations and regions; the GATT per-capita findings are an empirical corollary of that thesis. Hao [20] documents the political economy by which a small number of frontier AI companies amassed disproportionate compute access; the volume-vs-GDP asymmetry GATT measures is the downstream economic signature of that concentration.

## 6.3 Limitations

GATT carries four limitations worth surfacing.

**Vendor disclosure asymmetry.** Chinese vendors increasingly disclose token volume (Volcengine 120T per day; IDC China MaaS report) but rarely ARR. United States vendors disclose ARR (OpenAI $25B; Anthropic $25B+; Microsoft AI ARR $37B) but disclose throughput sporadically (Pichai's 16B per minute; OpenAI's 15B per minute). GATT translates between units but the translations carry assumption error. Confidence ratings of "low" or "medium" for ten of twenty-one tracked vendors reflect this asymmetry.

**Aggregator overlap.** OpenRouter at 3 trillion tokens per day is reported alongside the underlying vendors whose tokens it routes (Kimi, Anthropic, DeepSeek, Tencent Hy3, Xiaomi MiMo). The global total nets out the overlap, but the per-vendor sum exceeds the global total. This is documented in `scope_note` fields but remains a source of reader confusion.

**Pricing volatility.** Xing [6] documents 40× compression in GPT-4-equivalent pricing over 24 months. Token GDP figures pinned to point-in-time blended prices may shift substantially within months. We attach as-of dates to all Token GDP statements in the dataset; readers citing the figure must propagate the caveat.

**Confidence still concentrated in the top tier.** The four highest-confidence vendor estimates (Doubao, Gemini, OpenAI, Anthropic) cover 88% of global volume. The remaining seventeen vendors are individually small but collectively material; their typically lower confidence ratings concentrate measurement error in the long tail rather than the headline.

## 6.3.1 Factor-Share Decomposition: A Critical Research Gap

GATT's headline 88% US Token GDP share is a gross-output number, and the gross-vs-value-added distinction (§3.5.1) is one critical caveat. A second, equally consequential gap that this paper does not yet address is the *factor-share decomposition* of that 88%: what fraction accrues to (a) labor (model researchers, infrastructure engineers, deployment operations), (b) capital (compute infrastructure, datacenter capex, hardware depreciation), (c) economic rent on frontier model capability (the price premium charged because capability gaps remain), and (d) data and intellectual-property rents (training-data licensing, model-architecture patents)?

This is the central macroeconomic question for AI policy. A US Token GDP share dominated by frontier-capability rent has different policy implications than one dominated by capital rent or labor compensation. Industrial-policy debates currently proceed without this decomposition, treating the headline regional share as if its composition were neutral. It is not.

GATT v0.84 or v1.0 will explore factor-share decomposition where vendor cost-disclosure data permits, drawing on Brynjolfsson, Collis, and Eggers' (2019) framework for AI's intangible-capital component and Hulten's (1978) standard growth-accounting formulation. We flag this here as the most important unaddressed measurement gap, not as a closure. Policy researchers — Furman, Acemoglu, Autor, and the Hulten-tradition growth-accounting community — should treat the current 88/6 figure as the *starting point* for a factor-share investigation, not the conclusion of one.

## 6.4 Sovereign / Strategic-Resource Policy Trajectories

The §2.8 sovereign-resource framing implies three policy trajectories that are mechanically available to any sufficiently large jurisdiction. The GATT empirical signature is sufficient to discriminate between them.

**Trajectory A: laissez-faire.** Token production and pricing remain entirely with private vendors. The state collects standard corporate income tax on vendor profits and consumption tax on token sales. This is the current United States position, *de facto*. GATT-observable signature: continued vendor disclosure asymmetry (vendors disclose what they wish), no per-token excise reporting, no government-published token-volume statistics distinct from commercial-research aggregates.

**Trajectory B: regulated utility.** Token production remains private but is regulated as a quasi-utility — disclosure mandates, pricing oversight, structural separation between model-provider and infrastructure layers. This is the natural extension of the Bell-breakup / FCC-utility tradition. GATT-observable signature: emergence of mandatory vendor token-volume disclosures (analogous to FCC tariff filings), regulatory pricing schedules for "essential token services," per-token excise reporting absent state monopoly.

**Trajectory C: state monopoly or state-anchor operator.** The Sang Hongyang precedent (§2.8). The state establishes one or more wholly-owned token-infrastructure operators — analogous to Sinopec (中石化), PetroChina (中石油), and CNOOC (中海油) in the Chinese petroleum sector — with first-claim access to compute capacity, model weights, and fiscal margin. Private vendors may continue in residual or specialized roles. GATT-observable signature: a single Chinese operator's market share rising past 50% with concurrent CAICT / National Data Administration formalization, explicit token-excise legislation, and possibly a Sovereign Token Reserve announcement.

The 2026-05-15 GATT dataset and adjacent policy literature are most consistent with **Trajectory A in the United States and a transitional position between Trajectory A and Trajectory B in China** — *not* between A and C as initially conjectured in v1.5. The May 12, 2026 *China Minutes* report [41] documents the operational instruments of the current Chinese transition explicitly: local-government "computing power vouchers" (算力券) reducing user costs, a Hangzhou computing-trading platform processing 200 million yuan in transactions, and revenue-sharing arrangements where platforms offer "credits, subsidies or revenue-sharing" based on contributed capacity. These are *utility-model* instruments — Bell-style regulated-quasi-utility policy posture — not state-monopoly instruments. Volcengine's 49.5% China MaaS share (§2.2, IDC-validated) remains at the structural threshold beyond which state-anchor operator status becomes a discussible option in the Chinese institutional environment, and the CAICT framing of token throughput as a national-capability indicator (§2.2) is the kind of intellectual scaffolding that, in prior Chinese sectoral reorganizations (telecommunications 1998, petroleum 1998, electricity 2002), preceded structural intervention by three to five years. But the empirical signature as of 2026-05-15 is Trajectory B, not Trajectory C, and the v1.5 falsifiable hypothesis sharpens accordingly: if Volcengine's share climbs past 60% with concurrent CAICT and National Data Administration formalization, the Trajectory-C hypothesis is supported and the current Trajectory-B posture has been superseded; if Volcengine's share plateaus while utility-model instruments (vouchers, computing-trading platforms, revenue-sharing pools) expand, Trajectory B is the durable equilibrium. The 36-month observation window beginning 2026-05-14 is sufficient to distinguish these outcomes; the 4-day update from v1.5's initial diagnosis is itself an instance of GATT's revision discipline applied to its own framing.

**Fiscal-extraction worked illustration.** Suppose a jurisdiction implements a token-excise tax at rate $\tau$ on $V$ tokens per year sold at blended price $p$. Annual gross revenue is $\tau \cdot p \cdot V$ (incidence and avoidance set aside). At May 2026 figures — global volume $V \approx 113.5 \times 10^{15}$ tokens/year (311T/day × 365) and blended price $p \approx \$0.86$ per million tokens (back-solved from $\$97.0\text{B} / 113.5 \times 10^{15}$) — a 5% excise generates approximately **$4.85 billion/year globally**, dominated by United States flows under the 15× pricing-asymmetry leverage. At the §2.3-projected real-resource growth rate (price-adjusted), the same 5% excise reaches **approximately $36 billion/year by mid-2027** and **exceeds $200 billion/year by mid-2028** in a flat-pricing scenario. These figures are illustrative — actual revenue depends on incidence, demand elasticity, and avoidance — but they establish the order of magnitude at which fiscal authorities will begin to consider the policy. For benchmark: U.S. federal alcohol excise raises approximately $10B/year; U.S. federal motor-fuels excise raises approximately $40B/year. The token excise reaches fuel-tax-comparable magnitudes within the GATT-projection window.

**Sovereign Token Reserve hypothesis.** The U.S. Strategic Petroleum Reserve (established 1975 in response to the OPEC embargo; current capacity 727 million barrels) is the prototype for a state-held commodity buffer against geopolitical supply shock. A Sovereign Token Reserve would differ in mechanical detail: tokens are not storable as a commodity, but *compute capacity* and *pre-loaded model weights* are storable. A coherent sovereign reserve in the AI-token sense would consist of (a) state-owned datacenter capacity at strategic geographic distribution, (b) state-curated weight repositories of frontier and near-frontier models, and (c) priority-access agreements with private vendors during national emergencies. We flag this as a research direction rather than a policy recommendation; whether such a reserve is welfare-improving requires the factor-share decomposition (§6.3.1) and counterfactual-demand modeling that GATT does not yet support.

**Trajectory D: indigenous capability sovereignty (orthogonal).** A fourth trajectory, orthogonal to A-B-C rather than competing with them, is the *capability-sovereignty* path: a state pursues indigenous AI capability (sovereign datacenters, domestic chip programs, national-language model corpora, locally-hosted weights) independently of the fiscal-extraction posture it adopts on token throughput. The empirical evidence for this trajectory is substantial as of May 2026: approximately 130 sovereign-AI projects across more than 50 countries by January 2026 [37], Gartner's projection that 35% of countries will be locked into region-specific AI platforms by 2027 and 75% of European and Middle-Eastern enterprises will geopatriate workloads by 2030 [38], the World Economic Forum's "myth of AI sovereignty" critique [39], and Lawfare's "sovereignty gap" analysis of US AI statecraft [40]. Trajectory D combines with any of A, B, or C: the present US case is A + D (laissez-faire fiscal posture coupled with substantial indigenous capability investment); the present Chinese case per [41] is B + D (utility-style regulation coupled with indigenous capability investment); a future Sang Hongyang state would be C + D. Trajectory D maps onto the existing sovereign-AI literature [37-40], which is principally about capability sovereignty; Trajectories A, B, and C extend that literature with the fiscal-sovereignty layer that the salt-and-iron analog supplies. The GATT dataset is silent on Trajectory D in isolation — it measures token throughput and Token GDP, not capability ownership — but provides the empirical base for Trajectory-D analysts to test capability-sovereignty claims against actual throughput shares: a country claiming capability sovereignty whose throughput is dominated by foreign-headquartered vendors has a claim-versus-reality gap that GATT directly measures.

The sovereign-resource framing is the principal policy-side gap in GATT v1.4. Sections 2.8 and 6.4 close it descriptively; the substantive policy debate — whether any of Trajectories A, B, or C is welfare-improving, and under what conditions — remains open for the policy-research community to take up with the GATT empirical base as input rather than blackbox commercial research.

## 6.5 Future Work

GATT v0.83 will adopt the Inference Bottleneck [12] template — observed/inferred/judgment parameter classification with explicit sensitivity analysis — and publish sensitivity bands for headline figures, with conservative bounds anchored to Litowitz/Polson/Sokolov [1] physics-ceiling assumptions and aggressive bounds matching current empirical extrapolation. v0.84 will explore per-domain decomposition (chat / coding / search / agent workflows) where vendor disclosures permit. v1.0 will incorporate the LLM Inference Production Frontier [11] as a theoretical grounding for Token GDP, replacing simple blended pricing with production-cost curves where vendor cost data permits.

Beyond the dataset, three research directions are open: deeper integration with the academic physical-ceiling literature (perhaps a joint paper with Litowitz et al. that bounds the ratio between emitted and fresh-compute tokens empirically); per-domain pricing elasticity studies; and a longitudinal token-economy panel covering 2024-2030 once enough years of consistent measurement accumulate.

---

# 7. Conclusion

This paper introduced GATT — to our knowledge, the first global, all-sources, daily-updated empirical index of AI inference token throughput. As of May 11, 2026, GATT measures global daily output at 311 trillion tokens across 24 vendors and 12 countries, with China and the United States essentially tied (49.5/50.2) on volume share, the United States capturing 88% of Token GDP at $97.0 billion annualized, and a 597× United States–India per-capita gap.

The central methodological contribution of the paper is the documented 2.04× discrepancy between GATT's empirical United States per-capita figure (459,700 tokens per resident per day in May 2026) and the physical 2028 ceiling of 225,000 projected by Litowitz, Polson, and Sokolov [1]. Three reconciliation interpretations — partial GATT overestimation, conservative physical-ceiling calibration relative to 2026 inference-stack efficiency, and a unit-of-measurement difference between emitted and fresh-compute tokens — jointly account for the gap without invoking measurement error in either methodology. Empirical tracking and physical-bound modeling are productive complements; the Token Economy needs both.

GATT is released under CC BY 4.0 with full data, methodology, and revision history at `gf691271.github.io/gatt/`. The dataset is intended as a public good and a working prototype of the kind of token-volume infrastructure that the emerging token-economy literature [1, 6, 11] presupposes but does not yet possess. Collaborations on methodology refinement, vendor coverage extension, and joint physical-empirical reconciliation studies are warmly welcomed. The Token Economy is too consequential to measure in private.

**Empirical Tokeneconomy as a Fourth Methodological Tradition.** Token-economy research, as of mid-2026, comprises three established traditions, each applying a pre-AI methodology to the token unit: *physical-ceiling modeling* (Litowitz, Polson, Sokolov [1] — information theory and Bayesian statistics applied to inference energy budgets); *growth-accounting and general-purpose-technology economics* (Brynjolfsson, Hulten, Bresnahan-Trajtenberg, David, Acemoglu-Restrepo — productivity research with token volume as one possible empirical proxy); and *market-microstructure / commodity-derivative design* (Xing [6], Zhuang et al. [11], Inference Bottleneck working group [12] — Token Performance Index and futures-market construction inheriting from electricity, carbon, and bandwidth-derivatives precedent). None of the three is methodologically token-native: each toolkit would adapt to FLOPs, GPU-hours, or other computational currencies with comparable validity, and each predates the AI-inference token by decades.

GATT v1.0 introduces a fourth tradition — **empirical tokeneconomy** — whose methodological constructs are bound to token-specific phenomena that have no direct counterpart in the source disciplines. **Token GDP** (vendor-volume × regional blended pricing, §3.5) measures retail-equivalent value capture and surfaces the volume-vs-value asymmetry that ratio-of-FLOPs cannot. **Token Velocity** (the emitted-vs-fresh-compute multiplier, §5.5.8) measures cache and batched-attention reuse, a phenomenon that is meaningless at the FLOP layer. **Token Gini** (§4.4.1) leverages tokens' rare property of being individually attributable to populations, producing a distributional concentration measure that no aggregate compute metric supports. The §5.5.7 pre-registered numerical prediction ($\eta \in [0.30, 0.50]$) and the daily-anchored open dataset together establish the tradition as falsifiable and reproducible — necessary conditions for a methodology rather than a measurement exercise. Future work in this tradition includes a Token Balance of Payments (cross-border bilateral flow matrices reframing the CSIS [21] "Token Bill" concept as a full ledger), Token Engel curves (composition shifts in token use as per-capita consumption rises), and a longitudinal Token Economy panel once five-plus years of consistent measurement accumulate. We invite engagement across all four traditions, and we explicitly invite the source disciplines to refine the empirical-tokeneconomy constructs by importing their respective rigor: Bayesian identification of $V$ from cache-hit data, growth-accounting decomposition of Token GDP into factor shares, and microstructure formalization of token velocity as a tradable basis for a Token Performance Index.

---

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

---

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

---

# Appendix C. Bayesian Sensitivity Analysis of the §5.5 Decomposition

This appendix converts the §5.5 quantitative decomposition into a formal Bayesian sensitivity analysis, addressing the methodological concern (raised by Polson in our pre-submission peer review and synthesized by the Harvard editorial review) that the §5.5 decomposition as stated reports point estimates and asserts consistency rather than computing a posterior over the joint factor space.

## C.1 Setup

The decomposition under analysis is:

$$
\frac{G}{L} = \underbrace{\frac{G}{G^{*}}}_{\text{Interp. 1}} \cdot \underbrace{\frac{L^{*}}{L}}_{\text{Interp. 2}} \cdot \underbrace{\frac{G^{*}}{L^{*}}}_{\text{Interp. 3}}
$$

with the §5.5 central estimates and ranges (after the v1.0 per-factor tightening):

| Factor | Central | Low | High |
|---|---:|---:|---:|
| Interp. 1: $G/G^{*}$ | 1.12 | 1.05 | 1.20 |
| Interp. 2: $L^{*}/L$ | 3.0 | 2.0 | 4.0 |
| Interp. 3: $G^{*}/L^{*}$ | 1.4 | 1.25 | 1.65 |

The observable is $G/L = 459.7 / 225 \approx 2.04$.

## C.2 Prior specification

We specify a triangular prior on each factor anchored at the central value with bounds at the stated low and high. Triangular priors are appropriate for this setting because (a) the central values reflect our best estimate, (b) the bounds are interpretable (not just "wide" or "narrow"), and (c) the triangular distribution does not assume the symmetry or unboundedness that a Normal prior would impose.

Formally:
- $G/G^{*} \sim \text{Triangular}(1.05, 1.12, 1.20)$
- $L^{*}/L \sim \text{Triangular}(2.0, 3.0, 4.0)$
- $G^{*}/L^{*} \sim \text{Triangular}(1.25, 1.4, 1.65)$

**Modeling overlap between Interpretations 2 and 3.** The §5.5.5 discussion notes that Interpretation 2 (ASIC efficiency factor) and Interpretation 3 (compute-reuse mechanism) partially overlap because both exploit workload-pattern predictability. We model this overlap by introducing positive correlation $\rho = 0.4$ between the standardized values of $L^{*}/L$ and $G^{*}/L^{*}$ in the joint distribution. This correlation has two interpretations: (a) hardware-software co-design (ASIC efficiency depends on the workload-pattern predictability that also drives cache hits), or (b) shared underlying technology (better speculative decoding algorithms simultaneously improve both the ceiling-recalibration multiplier and the compute-reuse fraction). The choice of $\rho = 0.4$ is editorial; sensitivity to $\rho \in [0.2, 0.6]$ is tested below.

## C.3 Monte Carlo procedure

We draw $N = 10{,}000$ samples from the joint prior:

```
for i in 1 to N:
    interp1[i] = sample from Triangular(1.05, 1.12, 1.20)
    
    # Correlated draws for Interp. 2 and 3
    z1, z2 = draw two iid standard normals
    z2_corr = rho * z1 + sqrt(1 - rho^2) * z2  # rho=0.4
    
    interp2[i] = inverse_triangular_cdf(Phi(z1), 2.0, 3.0, 4.0)
    interp3[i] = inverse_triangular_cdf(Phi(z2_corr), 1.25, 1.4, 1.65)
    
    # Combined effect, with overlap modeled via correlation
    # Note: the overlap between Interp. 2 and Interp. 3 is captured by
    # the correlation in the standardized space, NOT by the
    # /4 ad-hoc correction removed from the v1.0 paper.
    G_over_L[i] = interp1[i] * interp2[i] * interp3[i]
```

This procedure replaces the v0.92 §5.5.5 ad-hoc /4 overlap correction with an explicit correlation model in the prior.

## C.4 Posterior over $G/L$

Running 10,000 MC draws under $\rho = 0.4$:

| Statistic | Value |
|---|---:|
| Mean of posterior $G/L$ | 4.85 |
| Median of posterior $G/L$ | 4.72 |
| 10th percentile | 3.30 |
| 25th percentile | 3.95 |
| 50th percentile | 4.72 |
| 75th percentile | 5.55 |
| 90th percentile | 6.50 |
| Observed $G/L$ | 2.04 |

**Result.** The observed 2.04 lies *outside* the central 80% credibility interval of the posterior — specifically, well below the 10th percentile of 3.30. This is the signal that the decomposition as stated is **insufficiently constrained by overlap**. Even under a correlation of 0.4 between Interpretations 2 and 3, the joint product overstates the implied gap by approximately 2× — which is precisely the tension that the v0.92 ad-hoc /4 correction was attempting (incorrectly) to repair.

## C.5 Re-calibrating the overlap correlation

The honest interpretation of §C.4 is that the decomposition's three factors must overlap *more* than $\rho = 0.4$ implies, *or* the per-factor central values must be lower, *or* both. We test the sensitivity by varying $\rho$ and reporting the $\rho$ at which the posterior median of $G/L$ matches the observed 2.04:

| Correlation $\rho$ | Posterior median $G/L$ | Posterior 10-90% interval |
|---:|---:|---:|
| 0.0 (independent) | 4.71 | [3.42, 6.42] |
| 0.4 | 4.72 | [3.30, 6.50] |
| 0.7 | 4.69 | [3.04, 6.83] |
| 1.0 (perfectly correlated) | 4.65 | [2.95, 7.04] |

Even under perfect positive correlation between Interpretations 2 and 3, the posterior median remains around 4.65 — far above the observed 2.04. **Correlation alone cannot reconcile the decomposition with the observable; the per-factor central values must shrink.**

## C.6 Implication for §5.5

The Appendix C analysis demonstrates that the §5.5 decomposition, as stated with Sokolov-tightened factor ranges (1.05-1.20, 2.0-4.0, 1.25-1.65), is **inconsistent with the observed 2.04× discrepancy under any plausible correlation structure**. The decomposition as a whole overstates the implied gap by approximately 2.3× (4.72 / 2.04).

This is informative, not falsifying. There are three possible resolutions:

**Resolution 1: Per-factor central values are higher than stated.** If the actual Interp. 2 central is 1.5× rather than 3.0×, and Interp. 3 central is 1.2× rather than 1.4×, the product 1.12 × 1.5 × 1.2 = 2.02 matches the observable. This would require accepting that the inference-stack efficiency multiplier is much smaller than §5.3 argues, which contradicts our engineering analysis. We do not endorse this resolution.

**Resolution 2: A fourth factor is missing from the decomposition.** The §5.5 decomposition may be incomplete. A natural candidate: the *empirical-vs-theoretical-throughput* gap — actual hardware utilization is far below theoretical peak. If 2026 inference deployments run at 30-50% of theoretical peak (a plausible figure given memory-bandwidth bottlenecks, scheduler inefficiencies, and load variability), an additional 0.3-0.5× factor would close the gap. We will explore this in v1.1.

**Resolution 3: The correlation structure should be modeled differently.** Rather than positive correlation between Interp. 2 and 3, the factors may exhibit a *substitution* relationship: when one factor is high (e.g., aggressive ASIC deployment), the other is correspondingly low (e.g., less reliance on cache-hit reuse because the ASIC handles fresh-compute efficiently). Negative correlation would shrink the posterior central tendency. We test this:

| Correlation $\rho$ | Posterior median $G/L$ |
|---:|---:|
| -0.5 (substitution) | 4.74 |
| -0.8 (strong substitution) | 4.78 |

Negative correlation actually *raises* the central posterior slightly. Substitution does not resolve the gap either.

## C.7 Honest conclusion and pre-registered prediction

The §5.5 decomposition is inconsistent with the observed 2.04× discrepancy under the per-factor ranges stated. This means either the per-factor central values are systematically biased upward (Resolution 1, which we reject on engineering grounds), or the decomposition is missing a fourth factor (Resolution 2, which we identify as theoretical-vs-empirical-utilization gap and quantify below), or both.

We report this honestly in the v1.0 paper: §5.5 is a *partial* decomposition that captures three of the relevant mechanisms but probably not all of them. The 2.04× observation is consistent with the partial decomposition once a 0.3-0.5× theoretical-vs-empirical-utilization factor is included; it is inconsistent with the partial decomposition as standalone.

### C.7.1 Pre-registered numerical prediction

To convert this finding from a soft "v1.1 will explore" into a falsifiable scientific claim, we commit to a specific numerical prediction in advance of empirical measurement:

> **Prediction.** When third-party benchmarking studies or vendor disclosures report aggregate hardware-utilization figures for representative 2026-2027 production inference deployments (H100/H200/TPU 8th-gen clusters serving frontier-model workloads), the volume-weighted average will satisfy $\eta \in [0.30, 0.50]$, with central expectation $\eta \approx 0.40$.

The four-factor model — adding $\eta$ to the §5.5.5 decomposition — yields:

$$
\frac{G}{L} = \underbrace{\frac{G}{G^{*}}}_{\approx 1.12} \cdot \underbrace{\frac{L^{*}}{L}}_{\approx 3.0} \cdot \underbrace{\frac{G^{*}}{L^{*}}}_{\approx 1.4} \cdot \underbrace{\eta}_{\approx 0.4} \approx 1.88
$$

against the observed $G/L = 2.04$. The 8% remaining residual sits well within the joint credibility band. This is *not* curve-fitting — $\eta \approx 0.4$ is the value implied by published 2024-2025 H100 utilization studies (Patel SemiAnalysis [22]; Epoch AI [18]) for memory-bandwidth-bound inference workloads, applied here as a forward extrapolation rather than a free parameter.

**Falsification rule:**

- **Confirmation** ($\eta \in [0.30, 0.50]$): the four-factor model is consistent with both empirical observation and engineering priors. Joint posterior of $G/L$ centers near 1.88-2.20, encompassing 2.04.
- **Falsification at the upper end** ($\eta > 0.70$): production hardware runs close to theoretical peak. The §5.5 per-factor central values overstate efficiency gains. Either Interpretation 2 ($L^{*}/L = 3.0$) is too aggressive or Interpretation 3 ($G^{*}/L^{*} = 1.4$) is too aggressive. The decomposition must be re-derived with the per-factor centrals revised downward.
- **Falsification at the lower end** ($\eta < 0.20$): production hardware is so under-utilized that capacity is software-throttled, not hardware-bounded. The Litowitz-Polson-Sokolov physical ceiling has implicit assumptions about scheduler/utilization efficiency that need to be made explicit. The framework requires an additional utilization parameter rather than treating utilization as part of the calibration.

The prediction is registered here, in v1.0, before any measurement. The author commits to publishing a v1.x revision within six months of the first credible empirical $\eta$ measurement, either confirming or retracting the prediction.

### C.7.2 Significance for the §5.5 program

The v0.92 manuscript reported "consistent with the observable" without sensitivity analysis. The v1.0 manuscript reports the sensitivity analysis, identifies the missing fourth factor, and pre-registers a specific numerical prediction with explicit falsification thresholds. The progression — from consistency assertion to identified-gap analysis to pre-registered prediction — is the appropriate scientific path for a hypothesis that cannot yet be uniquely identified from a single observable.

**The §5.5 decomposition is necessary but not sufficient. The fourth factor's central value is now an empirical question with a stated answer; the next study to measure $\eta$ in production deployments will either confirm or refute this paper's central reconciliation hypothesis.**

## C.8 Reproducibility

The Monte Carlo simulation code is deposited at the GATT repository:
```
paper/scripts/bayesian_sensitivity.py
```

The script accepts custom factor ranges and correlation values via command-line arguments and reproduces the Tables in §C.4 and §C.5. Posterior draws are released as `paper/data/bayesian_posterior_draws.csv`.

---

## References

See `paper/references.bib` for 47 entries; 32 used in main.tex cite calls.
