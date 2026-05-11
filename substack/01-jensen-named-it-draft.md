# Jensen Just Named What We've Been Measuring

**Substack post #1 — draft**
**Target publication**: 2026-05-13 (within 48-72h of GTC 2026 keynote)
**Estimated length**: 1200-1500 words
**Status**: DRAFT — not yet published

---

## Title options

- **A. Jensen Just Named What We've Been Measuring** (current)
- B. Two Token GDPs: NVIDIA's Supply Side, GATT's Demand Side
- C. The $150B Question: Can NVIDIA's Token Economy Be Audited?
- D. A Reader's Guide to "Token Economics" After GTC 2026

Recommendation: B as title (SEO-strong, structurally clear), A as subtitle.

---

## Draft

In May 2026, NVIDIA CEO Jensen Huang opened GTC by announcing that orders for the Blackwell and Vera Rubin chip families had reached $1 trillion through 2027 — a doubling from last year's $500B projection. But the more interesting framing was on the slide that followed: a two-axis chart with **tokens per watt** on the vertical and **tokens per second per user** on the horizontal, with revenue contours mapping the surface. Huang called this *Token Economics*.

He was not the first to use the phrase. He may have been the first to put it on the GTC keynote stage.

I run the Global AI Token Tracker — GATT for short. It's a daily-updated index of how many AI inference tokens get produced and consumed worldwide. As of May 2026, the number is 311 trillion per day across 24 tracked vendors and 12 countries. We've been calling the phenomenon "the Token Economy" since February. That's why, watching the keynote, I wasn't surprised by Jensen's framing — I was surprised at how clearly it complemented ours.

This post is about that complementarity, and about what *we* see when we look at the same Token Economy that Jensen sees, from the opposite side of the meter.

---

### Two ways to measure the same economy

In national income accounting, GDP can be computed three ways: production side (sum of value added across producers), expenditure side (sum of final consumption + investment + net exports), and income side (sum of wages + profits + taxes). Standard practice: compute all three, publish the differences as "statistical discrepancy." The discrepancies are themselves research-worthy.

Jensen's framework is the **production side** of the Token Economy. It starts from installed capacity (gigawatts of Blackwell or Rubin), multiplies by throughput efficiency (tokens per watt), allocates the throughput across service tiers (50 TPS/user Free, ..., 400 TPS/user Premium at $45/M tokens), and arrives at imputed annual revenue per gigawatt. Rubin's 1GW Premium-heavy tier mix: $150B/year. Multiply by the gigawatt count that NVIDIA expects to ship: trillions in revenue.

GATT is the **expenditure side**. It starts from observed vendor-level throughput (Doubao 129T/day, Gemini 73T/day, OpenAI 45T/day, Anthropic 22T/day, ...) — each anchored to a disclosure date, each with a confidence rating — sums to 311T/day globally, multiplies by realized regional blended prices ($1.50/M US, $0.10/M China, $1.20/M Europe), and arrives at $97B/year in retail-equivalent value. We call this Token GDP.

The two numbers don't equal each other. They shouldn't, exactly, for the same reason that production-side and expenditure-side GDP never quite equal each other in national accounts:

- NVIDIA's framework is **forward-looking** (orders through 2027) and **capacity-imputed** (assumed utilization × tier-mix). GATT is **backward-looking** (May 9, 2026 anchored) and **consumption-realized**.
- NVIDIA's framework counts the value that Blackwell-Rubin capacity *could* produce at assumed prices. GATT counts the value that vendors *did* charge for tokens they *did* deliver.
- NVIDIA's framework excludes second-hand markets (cloud customers reselling capacity, agent platforms aggregating, OpenRouter routing). GATT includes them when vendor data shows them.

The difference between the two numbers — Jensen's imputed supply-side and GATT's measured demand-side — is what economists call a **statistical discrepancy**, and it's the most interesting number in this whole conversation. It will sometimes go positive (capacity ahead of consumption, indicating overbuild or pricing softness). It will sometimes go negative (consumption ahead of capacity, indicating shortage or price escalation). When the two diverge widely, it tells you the Token Economy is in disequilibrium — and which direction.

In May 2026, my back-of-envelope reconciliation: Jensen's 1 GW Rubin Premium-tier $150B/year × the gigawatts already shipped ≈ $400-700B annualized capacity. GATT's measured Token GDP ≈ $97B annualized actual revenue. The discrepancy is large — roughly 4-7× — and it tells you something obvious that the GTC keynote understated: **most of the world's installed AI capacity is not yet operating at Jensen's Premium-tier assumptions**. Free-tier and mid-tier traffic dominates. Realized prices are well below the $45/M Premium tier benchmark. Utilization is uneven.

This is not a contradiction of NVIDIA's framing. It is the demand-side counterpart that NVIDIA needs in order for the Premium-tier 5× revenue projection to be credible. Without an external demand-side benchmark, the $150B/GW projection is unaudited.

---

### The reasoning-token asymmetry both frameworks should worry about

There's one structural ambiguity that affects both Jensen's framework and GATT — the **reasoning-token asymmetry**.

Modern reasoning models (o3, DeepSeek R1, Claude extended thinking, Gemini reasoning mode) generate 50,000 to 200,000 hidden chain-of-thought tokens per user-visible answer. These tokens:

- Consume actual watts (so they appear in Jensen's Y-axis tokens-per-watt)
- Don't appear to the user (so they don't appear in Jensen's X-axis TPS/user, if measured at the output layer)
- Are billed in some pricing schemes (OpenAI's o-series API charges output rate for reasoning tokens) and not in others (ChatGPT Plus subscription is fixed-fee regardless of reasoning depth)

This means **the same physical inference produces different "Token Economy" footprints depending on how you count**. If you count reasoning tokens in supply-side Y-axis but exclude them from demand-side billing, you get Jensen's projected $150B/GW. If you count them on both sides, you get something different. If you count them on neither, different again.

GATT and NVIDIA are both vulnerable to this ambiguity. Neither has resolved it. Resolving it requires an industry-wide accounting standard for reasoning tokens — a standard that does not yet exist. This is one of several methodological problems on the field's path; it deserves named research attention.

---

### What GATT is not

To be clear about what I'm not claiming:

- I am not claiming GATT measures the *true* size of the global Token Economy. GATT measures observable cloud inference. On-device inference (Apple Intelligence, Galaxy AI, Copilot+ PCs) is excluded. Military and government deployment is excluded. Self-hosted open-source inference (Ollama, LM Studio) is excluded. Realistic 95% confidence interval on global daily volume: roughly 180T-550T tokens, of which 311T is GATT's mid-estimate.

- I am not claiming Jensen's projection is wrong. Capacity-imputed forward projections operate at a different temporal scale than realized-revenue backward measurements. They are not directly comparable; their *difference* is the analytically interesting object.

- I am not claiming NVIDIA's framing should be displaced by GATT's. The opposite: both framings are needed for the Token Economy to be credible as a research field. Production-side without consumption-side is unaudited. Consumption-side without production-side is uncalibrated. Token Economy as a discipline requires both.

---

### What this means for readers

If you are a:

- **Cloud infrastructure investor** — Jensen's tokens/watt framework gives you the upper-bound capacity revenue. GATT's Token GDP gives you the realized revenue. Their gap is the gap between the bull case and the current state, and tracking how the gap closes (or doesn't) over the next 24 months is the most important macro signal for AI infra valuations.

- **Policy researcher / regulator** — neither framework alone tells you the distributional consequences of the Token Economy. GATT's per-capita and Token Gini data (US-India 597×; population-weighted Gini 0.674) are demand-side distributional findings that the supply-side framework cannot generate.

- **AI company executive** — your firm's TokenOps cost discipline (Finout, BMC Helix, in-house tools) measures the *third* perspective: firm-level micro accounting. The macro Token GDP is the denominator your TokenOps benchmarks should reference but rarely do.

- **Academic economist** — three measurement frameworks now exist: physical-ceiling (Litowitz, Polson, Sokolov 2026), supply-side capacity economics (Huang 2026), and demand-side empirical economics (this work). Reconciliation work — *Token GDP statistical discrepancy* — is a publishable research question and currently unclaimed.

---

### What I'm doing about it

Three things over the next 30 days:

1. **Publishing v2.0 of the GATT paper** with explicit recognition of NVIDIA's framing as a dialogue partner, and with a new section explicitly comparing the supply-side and demand-side Token GDP estimates. Currently writing the §2.7 dialogue.

2. **Releasing a calibration dataset** — `tokenizer_ratio_matrix_v0.1` — that addresses a methodological problem both frameworks have been avoiding: the assumption that "1 token" means the same thing across vendors. It doesn't. This dataset shows how much it doesn't.

3. **Weekly Substack posts** on the realized-revenue side of the Token Economy. The supply side has Jensen; the demand side has me, for now. We'll see.

If you want the daily data: https://gf691271.github.io/gatt/. All data is CC BY 4.0. Comments and corrections welcome at the GitHub issues page.

---

**Footnotes / image budget**: insert here a side-by-side image of Jensen's two-axis chart (cited from public GTC slides) vs. GATT's vendor-share pie chart (from the dashboard). The visual juxtaposition is the post's most shareable moment.

---

## Post-publication checklist

- [ ] Cross-post link to Twitter / X with image (2026-05-13 launch)
- [ ] Cross-post to LinkedIn (one day delay, 2026-05-14)
- [ ] Send to Litowitz, Polson, Sokolov, Brynjolfsson, Sevilla, Patel, Karpathy via outreach templates
- [ ] Email Hard Fork (Roose/Newton), Stratechery (Thompson), Ben Thompson directly
- [ ] Submit to Hacker News (timing: Tuesday-Thursday 8 AM PT)
- [ ] Add post URL to GATT dashboard footer
