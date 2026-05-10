# Outreach Email Templates — GATT v1.0 / arXiv launch

**Use:** Once `arXiv:[NNNN.NNNNN]` is assigned, replace `[ARXIV_ID]` and `[ARXIV_URL]` placeholders globally and send per the day-0 / day-1-2 / day-3-7 schedule in `ARXIV_SUBMISSION.md`.

**Author:** Frank Gao · gf691271@gmail.com · https://gf691271.github.io/gatt/
**Paper:** *Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference*

---

## Tier 1 — Academic (Day 0, within 6 hours of arXiv live)

### T1.1 — Litowitz / Polson / Sokolov (joint email — paper's central dialogue partners)

**To:** alec.litowitz@magnetar.com (or institutional); polson@chicagobooth.edu; vsokolov@gmu.edu
**Subject:** Empirical companion to *Photons = Tokens* — joint reconciliation paper?

> Dear Alec, Nick, and Vadim,
>
> I just posted the empirical companion paper to your *Photons = Tokens* (arXiv:2603.06630) on arXiv: **[ARXIV_URL]**. It builds the daily 21-vendor index (Global AI Token Tracker, GATT) needed to test your physical-ceiling projection against measured 2026 reality.
>
> Headline: GATT measures **459,700 tokens per US resident per day** in May 2026, against your 2028 ceiling of 225,000 — a **2.04× discrepancy**. Section 5 proposes three reconciliation interpretations and Appendix C runs a 10K-draw Bayesian Monte Carlo over the inference-stack efficiency multipliers (MoE 1.05–1.20×, 4-bit quantization 2.0–4.0×, speculative decoding + ASIC blended 1.25–1.65×, ρ=0.4). Honest finding: even at the upper joint posterior, the decomposition is partial — a fourth factor (likely 30–50% theoretical-vs-empirical hardware utilization) is needed to close the gap. We do **not** add an ad-hoc /4 correction.
>
> The paper engages with your framework throughout — your three names are cited 11 times, and §5.5 reframes the gap not as a refutation but as a **joint calibration target**. If you're open to it, I'd love to discuss either (a) a co-authored reconciliation note at a future arXiv update, or (b) your reactions / corrections before broader distribution.
>
> Dataset: https://gf691271.github.io/gatt/ · Snapshots: github.com/gf691271/gatt/tree/main/data/snapshots
>
> Best,
> Frank Gao

---

### T1.2 — Erik Brynjolfsson (highest-leverage single endorser)

**To:** brynjolfsson@stanford.edu (cc: hai-info@stanford.edu)
**Subject:** A working instance of your December 2025 prediction — GATT, now on arXiv

> Dear Professor Brynjolfsson,
>
> In December 2025 you forecast that 2026 would see *"high-frequency AI economic dashboards tracking AI's economic impact in near real-time."* I built one: the **Global AI Token Tracker (GATT)** — 21 vendors, 12 countries, daily updated since February 2026. The methodology paper is now live on arXiv: **[ARXIV_URL]**.
>
> A few findings I think you'll find consequential:
> - Global daily output: **310 trillion tokens**; annualized "Token GDP" $95.8B
> - **China and the US are tied at 50% volume** — but the US captures **88% of Token GDP** (15× pricing asymmetry)
> - **US–India per-capita gap: 597×**, widened from 448× in five weeks
> - The paper documents a productive **2.04× tension** with the Litowitz/Polson/Sokolov 2028 physical ceiling, with three reconciliation interpretations + Bayesian sensitivity analysis
>
> Two specific asks:
> 1. **Endorsement for arXiv cs.CY** if my submission is held — would your name carry weight here?
> 2. **Cross-citation** in the next Stanford HAI / Digital Economy Lab brief — GATT is built explicitly to be the empirical input layer for productivity-J-curve work.
>
> Open dataset (CC BY 4.0): https://gf691271.github.io/gatt/
>
> Thank you for considering — happy to send the PDF, a one-page summary, or jump on a call.
>
> Best,
> Frank Gao

---

### T1.3 — Yicai Xing (TPI co-conceiver)

**To:** [via arXiv:2603.21690 author contact]
**Subject:** Your TPI proposal — GATT as a working prototype

> Dear Professor Xing,
>
> Your *AI Token Futures* paper (arXiv:2603.21690) called for a **Token Performance Index** as essential market infrastructure. I posted a working prototype to arXiv today: **[ARXIV_URL]**. The paper documents the methodology behind the **Global AI Token Tracker (GATT)** — 21 vendors, daily updated, open data.
>
> GATT measures 310T tokens/day globally, with vendor-level transparency, snapshot-based reproducibility, and a "Token GDP" weighted variant that addresses the regional-pricing-asymmetry problem TPI specifications need to solve. Section 6.5 explicitly positions GATT against your TPI specification.
>
> If a TPI standard is being developed, would you be open to GATT contributing the empirical reference layer? I'd value your reactions to §3 (methodology) and Appendix A (vendor-by-vendor confidence classification).
>
> Dataset: https://gf691271.github.io/gatt/
>
> Best,
> Frank Gao

---

### T1.4 — Jaime Sevilla (Epoch AI)

**To:** jaime@epochai.org
**Subject:** GATT × Epoch — token volume meets your inference-cost track

> Dear Jaime,
>
> Epoch's "inference cost halves every two months" panel and GATT's empirical token-volume index are complementary measurements of the same phenomenon. Today I posted GATT's methodology paper on arXiv: **[ARXIV_URL]**.
>
> GATT measures 310T tokens/day across 21 vendors, with **99.7% price decline + 3× spend increase** (the price-volume paradox documented in §4.4). When combined with your cost trajectory, the implied real-output growth is order-of-magnitude larger than headline numbers suggest.
>
> Two ideas:
> 1. **Cross-citation** in the next Epoch Brief — happy to provide a clean one-paragraph methodology summary
> 2. **Joint chart** combining Epoch cost decline × GATT volume growth — would give a single number for "real AI compute consumed"
>
> CC BY 4.0 dataset, snapshot history: https://gf691271.github.io/gatt/
>
> Best,
> Frank Gao

---

## Tier 1 — Practitioner (Day 1–2)

### T1.5 — Andrej Karpathy (X DM, single most leveraged)

**Channel:** X DM @karpathy (also @karpathy on Bluesky as backup)

> Hi Andrej — saw your tweets about token-throughput as a personal-productivity metric. I built the global-scale version: GATT, daily index of all 21 major vendors, just hit arXiv today: **[ARXIV_URL]** · live: https://gf691271.github.io/gatt/
>
> Highlight: **310T tokens/day globally, 459K/US-resident/day, US-India gap 597×**. Paper proposes "Token GDP" as a new economic metric and documents a 2.04× tension with Litowitz/Polson/Sokolov's physical ceiling — Appendix C is a Bayesian MC that's pretty fun.
>
> No ask other than "if it's interesting, take a look." Source + raw data fully open. Cheers.

---

### T1.6 — Anjney Midha (a16z; arXiv:2601.10088 co-author)

**To:** anjney@a16z.com (cc as appropriate)
**Subject:** GATT — extends your 100T Token Study methodology to all 21 vendors

> Dear Anjney,
>
> Your **100T Token Study** with OpenRouter was the most rigorous slice-level token-economy data point of 2026. I extended the methodology to all 21 major vendors globally — daily updated, fully open. The paper hit arXiv today: **[ARXIV_URL]**.
>
> Three findings that should land at a16z:
> - **310T tokens/day** (vs OpenRouter's slice; methodology contrasts in §2.4)
> - **Token GDP $95.8B/year**, with US–China 88/6 value-share split despite 50/50 volume
> - **2.04× tension** with the Litowitz/Polson/Sokolov physical ceiling — direct relevance to a16z's "AI as commodity" thesis
>
> If a16z's AI-infra content track is interested, I can supply ready-made charts, vendor-by-vendor breakdowns, or a customized one-pager. Endorsement for arXiv cs.CY would also be very welcome.
>
> Best,
> Frank Gao

---

### T1.7 — Martin Casado (a16z infrastructure)

**To:** martin@a16z.com
**Subject:** Token GDP — the empirical underpin to a16z's AI commodity thesis

> Dear Martin,
>
> a16z's recent infra writing positions AI as the next-generation commodity layer. GATT operationalizes that thesis with a daily Token GDP measurement: **$95.8B/year run-rate, 310T tokens/day across 21 vendors, 12 countries**. Methodology paper just hit arXiv: **[ARXIV_URL]**.
>
> Most a16z-relevant findings:
> - **Volcengine at 49.5% China public-cloud MaaS share** (IDC-confirmed) — concentration story
> - **15× US/China pricing asymmetry** with 50/50 volume parity — value-vs-volume divergence
> - **99.7% price decline / 3× spend increase** — clearest demand-elasticity data point I've seen
>
> Happy to brief the infra team or contribute to a16z published research. Open dataset, CC BY 4.0.
>
> Best,
> Frank Gao

---

### T1.8 — Dylan Patel (SemiAnalysis)

**To:** dylan@semianalysis.com
**Subject:** GATT × SemiAnalysis AI Cloud TCO — two views of the same economy

> Dear Dylan,
>
> SemiAnalysis's **AI Cloud TCO** is the canonical USD-side / capacity-side measurement. **GATT** is the token-side / output-side complement — daily index, 21 vendors, 12 countries. Methodology paper on arXiv as of today: **[ARXIV_URL]**.
>
> Most interesting if you write about it:
> - Direct GATT-to-TCO crosswalk in §6.4 — divides Token GDP by your $/H100-hour to derive implied utilization
> - **2.04× empirical-vs-physical-ceiling tension** with rigorous Bayesian sensitivity (Appendix C) — should be catnip for SemiAnalysis readers
> - **597× US–India per-capita gap** — distribution story your readers would value
>
> Possible Substack feature: *"Two Views of the Same Token Economy."* Happy to provide raw data, custom cuts, or a co-bylined piece.
>
> Best,
> Frank Gao

---

## Tier 2 — Media (Day 3–7)

### T2.1 — Karen Hao (The Atlantic / *Empire of AI* author)

**To:** karen.hao@theatlantic.com (or via Atlantic editorial)
**Subject:** A measurement layer for *Empire of AI* — GATT, 12-country daily index

> Dear Karen,
>
> *Empire of AI* documents the political economy of OpenAI and compute concentration. **GATT** measures the global *consequences*: who actually consumes AI tokens, where, and at what relative cost. Methodology paper just posted: **[ARXIV_URL]**.
>
> The Empire-of-AI relevant findings:
> - **US captures 88% of Token GDP** despite only 50% of volume — a power-economics story, not a usage story
> - **US–India per-capita gap: 597×, widened from 448× in five weeks** — the gap is *accelerating*
> - **Volcengine 49.5% of China MaaS** — the rise of a non-OpenAI empire your book opens space to discuss
>
> If The Atlantic is interested in covering, I can supply briefing materials, custom cuts, or contribute as a data source. The dataset is fully open (CC BY 4.0).
>
> Best,
> Frank Gao

---

### T2.2 — Kevin Roose & Casey Newton (Hard Fork)

**To:** kevin.roose@nytimes.com; casey@platformer.news
**Subject:** Hard Fork pitch — the price-volume paradox of AI tokens

> Dear Kevin and Casey,
>
> A Hard Fork-shaped finding from a paper I just put on arXiv: **AI token prices fell 99.7% in two years while total spending grew 3×.** Demand isn't elastic — it's hyper-elastic.
>
> Full paper here: **[ARXIV_URL]** — *Measuring the Token Economy*, an empirical 21-vendor daily index project (GATT). Other Hard Fork-friendly numbers:
> - **310 trillion tokens generated globally per day**
> - **United States: 459,000 tokens per resident per day**
> - **US–India per-capita gap: 597×**
> - **2.04× discrepancy** between empirical use and the most-cited physical ceiling — story angle: "AI is using more tokens than physics says it should"
>
> Happy to send a one-pager or jump on a 15-min call to make the segment work. All data CC BY 4.0.
>
> Best,
> Frank Gao

---

### T2.3 — Sarah Guo & Elad Gil (No Priors)

**To:** sarah@conviction.com (cc Elad's preferred channel)
**Subject:** No Priors pitch — Token Economy as the AI strategic-investment lens

> Dear Sarah and Elad,
>
> No Priors's investor-strategic lens fits cleanly with what I've been measuring at GATT. I just posted the methodology paper on arXiv: **[ARXIV_URL]**.
>
> Most VC-relevant findings:
> - **Token GDP $95.8B/year run-rate** — bigger than the headlines suggest
> - **Volcengine 49.5% China MaaS share** (IDC-confirmed) — concentration is faster than US analysts assume
> - **15× US/China pricing arbitrage** — open question: arbitrage or quality gap?
> - **Bayesian MC** in Appendix C: even the most conservative inference-efficiency assumptions point to a 4th factor (~30-50% theoretical-vs-actual hardware utilization) — investment thesis: who closes that gap wins
>
> If a No Priors guest spot, segment, or backgrounder makes sense, I'd love to make it happen.
>
> Best,
> Frank Gao

---

### T2.4 — Ben Thompson (Stratechery)

**Channel:** Stratechery contact form (best path)
**Subject:** GATT — Token GDP as a Stratechery-shaped framing

> Ben,
>
> Stratechery's analytical mode — strategic-economic framings of the platform layer — fits a project I just put on arXiv: **[ARXIV_URL]**. *Measuring the Token Economy*: a daily 21-vendor index (GATT) with a "Token GDP" $95.8B/year metric.
>
> Stratechery-shaped angles:
> - **Token GDP** as economic-value frame (vs raw volume) — surfaces a 88/6 US/China value split despite 50/50 volume parity
> - **Aggregator-vs-supplier reframed**: the platforms with pricing power capture Token GDP regardless of volume share
> - **The 2.04× tension** with Litowitz/Polson/Sokolov's physical ceiling — the kind of productive measurement-vs-theory gap Stratechery readers enjoy
>
> Happy to brief, supply raw data, or contribute a guest Daily Update.
>
> Best,
> Frank Gao

---

### T2.5 — Ezra Klein (NYT Opinion / EK Show)

**To:** ezra.klein@nytimes.com
**Subject:** AI inequality, measured: 597× US–India token gap

> Dear Ezra,
>
> Your AI commentary has consistently pulled at the inequality thread. I have a measurement that may be useful: **the per-capita AI token consumption gap between the US and India is 597×**, and it widened from 448× in just five weeks.
>
> Full paper on arXiv: **[ARXIV_URL]** — *Measuring the Token Economy*, daily 21-vendor index (GATT), open dataset.
>
> The inequality is not just a usage gap — it's compounding (Section 4.5 shows the rate of widening). If an Ezra Klein Show segment, NYT Opinion piece, or background briefing would be useful, happy to make any of them work.
>
> Best,
> Frank Gao

---

## Tier 2 — Policy / China (Week 2+)

### T2.6 — Wei Liang / CAICT

**To:** [via CAICT institutional contact]
**Subject:** GATT × CAICT — token-economy measurement triangulation

> Dear Vice President Liang,
>
> CAICT's reported 4.12 trillion tokens/week China figure and GATT's measured 154T tokens/day (China share) provide complementary measurement of the same underlying phenomenon. The methodology paper hit arXiv today: **[ARXIV_URL]**.
>
> The paper explicitly cites CAICT (§4.6) and acknowledges a v0.90 retraction where my prior interpretation of the 4.12T figure was incorrect. I'd value:
>
> 1. CAICT's reaction to GATT's 21-vendor methodology and the China-side numbers
> 2. Possible joint methodology note clarifying the relationship between the two measurement frames
> 3. Any contact with the CAICT team that produced the 4.12T figure
>
> Open dataset (CC BY 4.0): https://gf691271.github.io/gatt/
>
> Respectfully,
> Frank Gao

---

### T2.7 — CSIS Wadhwani Center (Token Bill authors)

**To:** [via CSIS author contact pages]
**Subject:** Operationalizing the Token Bill — GATT as data input

> Dear [Author Name],
>
> Your April 2026 analysis introduced the **"Token Bill"** framing for AI governance. GATT's methodology paper (just posted: **[ARXIV_URL]**) operationalizes that concept — daily 21-vendor / 12-country token index, with a "Token GDP" economic-value variant that gives policymakers a comparable cross-jurisdictional metric.
>
> Most CSIS-relevant findings:
> - **US/China 88/6 Token GDP split** despite 50/50 volume — sovereignty-vs-value framing
> - **Volcengine 49.5% China MaaS share** (IDC-confirmed) — concentration concerns
> - **Vendor-by-vendor confidence classification** in Appendix A — useful for policy due-diligence
>
> If GATT could be a data input layer for future CSIS analyses, happy to coordinate. Open dataset, CC BY 4.0.
>
> Best,
> Frank Gao

---

### T2.8 — CEIBS authors (China overtook US in token usage)

**To:** [via CEIBS author contact]
**Subject:** China-side commentary on GATT 50/50 volume parity finding

> Dear [Author Name],
>
> Your CEIBS piece *"How China overtook the US in AI token usage"* and GATT's measurements converge on the 50/50 volume-parity finding — but GATT's data also surfaces the **15× pricing asymmetry** that produces an 88/6 *value*-share split. This nuance seems important to a Chinese readership. Methodology paper now on arXiv: **[ARXIV_URL]**.
>
> If you're writing a China-side commentary, three GATT-derived data points may be useful:
> - **154T China tokens/day** (vs 156T US) — the volume tie
> - **Volcengine 49.5% MaaS share** — more concentrated than analyst consensus
> - **CAICT 4.12T/week reconciliation** — §4.6 of the paper
>
> Open dataset, CC BY 4.0: https://gf691271.github.io/gatt/. Happy to supply custom China-only cuts or co-author a methodology note.
>
> Best,
> Frank Gao

---

## Day-0 announcement copy

### Tweet / X post (270 chars)

> *Measuring the Token Economy* is live on arXiv: **[ARXIV_URL]**
>
> 21 vendors. 12 countries. Daily updated since Feb 2026.
>
> 310T tokens/day · $95.8B Token GDP/yr · US captures 88% of value at 50% of volume
>
> 2.04× tension with @vsokolov et al's physical ceiling — Bayesian MC in App. C
>
> https://gf691271.github.io/gatt/

### LinkedIn post (~150 words)

> Today I published *Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference* on arXiv ([ARXIV_URL]).
>
> The paper documents the methodology behind GATT (Global AI Token Tracker) — the first global, all-sources, daily index of AI inference token throughput, covering 21 vendors and 12 countries since February 2026.
>
> Three findings:
> 1. Global daily output is **310 trillion tokens**; "Token GDP" runs at **$95.8B/year**.
> 2. China and the US are tied at **50% of volume** — but the US captures **88% of Token GDP** because of a 15× pricing asymmetry.
> 3. The empirical 459.7K tokens/US-resident/day is **2.04× higher** than the leading 2028 physical ceiling. The paper proposes three reconciliation interpretations and runs a 10K-draw Bayesian Monte Carlo (Appendix C) showing the gap is real and identifies the missing factor.
>
> All data is open (CC BY 4.0): https://gf691271.github.io/gatt/

---

## Hacker News submission

**Title:** *Measuring the Token Economy: A 21-vendor Daily Index of AI Inference (arXiv)*
**URL:** [ARXIV_URL]
**First comment** (from author, posted immediately):

> Author here. Quick context: GATT has been daily-updated since February 2026, covering 21 vendors and 12 countries. The paper documents how I get the numbers, how I treat low-confidence vendors (see Appendix A — Gemini was downgraded from High to Medium between v0.91 and v1.0 after a peer review), and a 2.04× tension with the most-cited physical ceiling (Litowitz / Polson / Sokolov, arXiv:2603.06630).
>
> The tension is real: Bayesian MC in Appendix C with 10K draws and ρ=0.4 correlated priors shows even the optimistic posterior leaves a 30-50% gap. Honest answer: the §5.5 efficiency decomposition is partial. Happy to take HN's questions on methodology, gaps, or the Token GDP framing.

---

## Order of operations on Day 0

1. **0:00** — arXiv accepts; receive ARXIV_ID
2. **0:05** — Replace `[ARXIV_ID]` and `[ARXIV_URL]` placeholders globally in this file
3. **0:10** — Send T1.1 (Litowitz/Polson/Sokolov) — most important, do this first
4. **0:30** — Send T1.2 (Brynjolfsson)
5. **0:45** — Tweet announcement
6. **1:00** — LinkedIn post
7. **1:30** — Send T1.3 (Xing), T1.4 (Sevilla), T1.8 (Patel)
8. **2:00** — Submit to Hacker News
9. **Day 1** — T1.5 (Karpathy DM), T1.6 (Midha), T1.7 (Casado)
10. **Day 2-3** — T2.1 (Hao), T2.2 (Roose/Newton)
11. **Day 4-7** — T2.3 (Guo/Gil), T2.4 (Thompson), T2.5 (Klein)
12. **Week 2+** — T2.6 (CAICT), T2.7 (CSIS), T2.8 (CEIBS)

**Reply tracking:** maintain a simple log per email — sent date, reply received yes/no, follow-up needed yes/no. The `data/tci-latest.json` `outreach_targets` block can be updated with `last_contacted` and `response_status` fields after Day 7.
