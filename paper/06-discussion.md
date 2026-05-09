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

## 6.4 Future Work

GATT v0.83 will adopt the Inference Bottleneck [12] template — observed/inferred/judgment parameter classification with explicit sensitivity analysis — and publish sensitivity bands for headline figures, with conservative bounds anchored to Litowitz/Polson/Sokolov [1] physics-ceiling assumptions and aggressive bounds matching current empirical extrapolation. v0.84 will explore per-domain decomposition (chat / coding / search / agent workflows) where vendor disclosures permit. v1.0 will incorporate the LLM Inference Production Frontier [11] as a theoretical grounding for Token GDP, replacing simple blended pricing with production-cost curves where vendor cost data permits.

Beyond the dataset, three research directions are open: deeper integration with the academic physical-ceiling literature (perhaps a joint paper with Litowitz et al. that bounds the ratio between emitted and fresh-compute tokens empirically); per-domain pricing elasticity studies; and a longitudinal token-economy panel covering 2024-2030 once enough years of consistent measurement accumulate.
