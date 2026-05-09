# 6. Discussion

## 6.1 Policy Implications

The Section 4 finding that China and the United States are tied at 50% / 50% on token volume but split 6% / 88% on Token GDP has direct implications for AI governance. Two are worth highlighting.

First, **volume parity is not AI parity**. Headlines about Chinese AI catching up frequently cite token volume; this paper documents that volume parity has indeed arrived. But economic value has not. The 15× pricing gap between United States and Chinese inference reflects model capability tier (frontier US vs. fast-follower Chinese), enterprise willingness to pay, and the absence of true price competition where capability gaps remain. Governance frameworks that conflate volume with value will misread the situation; a US Token GDP share of 88% is the more decision-relevant figure for export-control or industrial-policy debates.

Second, **per-capita rather than total-volume metrics are appropriate for inequality governance**. The 597× United States–India gap is the central distributional finding of the dataset and is more pertinent to international development conversations than aggregate national totals. A country with one-fifth the US population but matching aggregate token output would still be far behind on per-resident terms. We expect per-capita figures to play an increasing role in AI development indices, akin to how income per capita supplements GDP in macroeconomic comparison.

Xing's [6] proposed token futures market is conditional on the existence of a credible Token Performance Index — exactly the kind of artifact that GATT prototypes. If such a market launches in 2027-2028 as Xing projects, the empirical index underlying contract pricing will need to handle vendor disclosure asymmetry, scope normalization (all-sources vs. external), and pricing volatility (40× compression in 24 months per Xing). GATT's revision discipline and open methodology are designed to scale into that role.

## 6.2 Geo-Economic Implications

Three observations bear on the geo-economics of AI.

First, **China's 50% volume share is dominated by internal first-party usage**. Section 3.3 documents that more than 95% of Volcengine's measured throughput is internal — Douyin AI Search, the Doubao consumer app, the Jimeng image-generation pipeline — rather than external MaaS sold to enterprise customers. This shapes export-control implications: restrictions on inference chips that target enterprise MaaS deployment have limited reach into ByteDance's internal supply chain. The Chinese token economy is structurally vertical-integrated in ways the United States is not.

Second, **export controls operate on a thin efficiency margin**. The Section 5 reconciliation showed that effective inference efficiency in 2026 deployments runs 5-10× above the GPT-4-class baseline implicit in physical-ceiling models. Hardware restrictions that delay this efficiency frontier by even one generation can substantially reshape the global token landscape. Conversely, if Chinese vendors achieve ASIC parity (e.g., via Tencent's chip stack or Xiaomi's MiMo deployment hardware), the United States volume lead from inference-stack innovation could collapse.

Third, **the 597× United States–India per-capita gap is a structural inequality outside the China–US frame**. India ranks 11th globally on per-capita token throughput (770 tokens per resident per day) despite ranking 9th in absolute volume (1.10 trillion per day). Population scale dilutes the metric, but the underlying access disparity is real: most AI-driven productivity gains are accruing to a small per-capita-rich set of countries, with India and Indonesia representing population-weighted majorities of the global Rest-of-World residual.

## 6.3 Limitations

GATT carries four limitations worth surfacing.

**Vendor disclosure asymmetry.** Chinese vendors increasingly disclose token volume (Volcengine 120T per day; IDC China MaaS report) but rarely ARR. United States vendors disclose ARR (OpenAI $25B; Anthropic $25B+; Microsoft AI ARR $37B) but disclose throughput sporadically (Pichai's 16B per minute; OpenAI's 15B per minute). GATT translates between units but the translations carry assumption error. Confidence ratings of "low" or "medium" for ten of twenty-one tracked vendors reflect this asymmetry.

**Aggregator overlap.** OpenRouter at 3 trillion tokens per day is reported alongside the underlying vendors whose tokens it routes (Kimi, Anthropic, DeepSeek, Tencent Hy3, Xiaomi MiMo). The global total nets out the overlap, but the per-vendor sum exceeds the global total. This is documented in `scope_note` fields but remains a source of reader confusion.

**Pricing volatility.** Xing [6] documents 40× compression in GPT-4-equivalent pricing over 24 months. Token GDP figures pinned to point-in-time blended prices may shift substantially within months. We attach as-of dates to all Token GDP statements in the dataset; readers citing the figure must propagate the caveat.

**Confidence still concentrated in the top tier.** The four highest-confidence vendor estimates (Doubao, Gemini, OpenAI, Anthropic) cover 88% of global volume. The remaining seventeen vendors are individually small but collectively material; their typically lower confidence ratings concentrate measurement error in the long tail rather than the headline.

## 6.4 Future Work

GATT v0.83 will adopt the Inference Bottleneck [12] template — observed/inferred/judgment parameter classification with explicit sensitivity analysis — and publish sensitivity bands for headline figures, with conservative bounds anchored to Litowitz/Polson/Sokolov [1] physics-ceiling assumptions and aggressive bounds matching current empirical extrapolation. v0.84 will explore per-domain decomposition (chat / coding / search / agent workflows) where vendor disclosures permit. v1.0 will incorporate the LLM Inference Production Frontier [11] as a theoretical grounding for Token GDP, replacing simple blended pricing with production-cost curves where vendor cost data permits.

Beyond the dataset, three research directions are open: deeper integration with the academic physical-ceiling literature (perhaps a joint paper with Litowitz et al. that bounds the ratio between emitted and fresh-compute tokens empirically); per-domain pricing elasticity studies; and a longitudinal token-economy panel covering 2024-2030 once enough years of consistent measurement accumulate.
