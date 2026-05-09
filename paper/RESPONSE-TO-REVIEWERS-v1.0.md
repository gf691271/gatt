# Response to Reviewers — GATT v0.92 → v1.0

**Manuscript:** *Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference*
**Author:** Frank Gao
**Round:** v0.92 → v1.0 (May 10-11, 2026)
**Reviewers:** Simulated peer review by (1) Stanford-affiliated economist (prior round, applied to v0.91→v0.92), (2) Alec Litowitz, (3) Nick Polson, (4) Vadim Sokolov — co-authors of *Photons = Tokens* (arXiv:2603.06630), the manuscript's central dialogue partner — and (5) Harvard editorial synthesis.

This document maps each reviewer concern to the specific revision implemented in v1.0. The format follows journal-style response-to-reviewers conventions: reviewer concern paraphrased, location in v1.0 manuscript, summary of change, brief rationale.

---

## Litowitz (Photons=Tokens framework lead)

### L1. "Static artifact" rhetorical framing
**Concern (verbatim):** "The 'static 2024-era artifact' framing is the central problem... the conclusion of Section 5.3 should read: 'the calibration inputs deserve updating; the framework does not.'"

**Action:** §5.3 first paragraph rewritten. The framework is now explicitly affirmed as not dated; only the calibration inputs are dated. Removed the "static artifact" sentence entirely.

**v1.0 location:** §5.3 paragraph 1.

### L2. §5.5.5 "/4 correction" is unprincipled
**Concern:** "The synthesis formula in §5.5.5 manually divides by 4... a flat /4 correction on the product of 1.12 × 4 × 1.54 is not a principled decomposition."

**Action:** Removed the /4 correction entirely. Replaced with explicit modeling of the overlap between Interpretations 2 and 3 via correlation $\rho = 0.4$ in the Appendix C Bayesian analysis. The §5.5.5 narrative now acknowledges the under-identification explicitly.

**v1.0 location:** §5.5.5 paragraph 4 ("Removing the unprincipled overlap correction").

### L3. §5.5.6 falsification conditions too loose
**Concern:** "The thresholds are calibrated so that falsification is unlikely given what is already publicly known... more demanding falsification would be: 'if the efficiency multiplier is below 3× rather than below 2×.'"

**Action:** Tightened thresholds: cache-hit floor 20% → 30%; per-token energy gain floor 2× → 2.5×; vendor multiplier audit floor 25% → 20%. Each threshold now sits at the conservative edge of the plausible range, not in the extreme tail.

**v1.0 location:** §5.5.6 entirely rewritten.

### L4. §5.5.3 4× ceiling-recalibration multiplier needs derivation
**Concern:** "The 3-5× efficiency multiplier claim in §5.5.3 needs a first-principles derivation using our framework's own methodology."

**Action:** §5.3 now provides explicit per-mechanism analysis: MoE 2-4× (not 10-30× headline; attention dominates on long-context), 4-bit quant 2-2.5× (not 4×; KV-cache stays higher precision), speculative decoding 1.5-2× blended (not 2-3×; reasoning workloads are 1.2-1.5×), ASIC 3× blended (not 5-10×; only on optimized decode workloads). Compositional discount captures the dominant factor plus modest secondary contributions, yielding 2.5-3× central, 2-4× plausible — substantially tightened from the v0.92 4× central.

**v1.0 location:** §5.3 entirely rewritten + §5.5.3 carries the tightened range.

### L5. Invitation language should be front-loaded
**Concern:** "The invitation at the end of §5.5.6 ... is the right instinct. That is the paper I would co-author. The present manuscript is the pitch document for that collaboration."

**Action:** §5 introduction now states explicitly: "This section is offered as a falsifiable hypothesis for joint refinement, not as a closed argument." Added §5.5.7 "The Joint Calibration Proposal" with three specific co-authored measurement studies.

**v1.0 location:** §5 introduction + new §5.5.7.

---

## Polson (Bayesian statistician)

### P1. Confidence taxonomy is not Bayesian
**Concern:** "'High / medium / low' describes the information type of the source signal... not the posterior probability that the stated throughput figure lies within any stated interval."

**Action:** Added observed/inferred/judgment-based parameter classification (per Inference Bottleneck arXiv:2604.17431) to Appendix A. Confidence ratings are now augmented with this Bayesian-flavored classification. Full migration to a posterior-credibility taxonomy is committed for v0.83 of the dataset, with v1.0 of the paper documenting the transition.

**v1.0 location:** Appendix A "Parameter classification (v1.0)" paragraph.

### P2. +8%/month default growth rate is unanchored
**Concern:** "The 8%/month default is supposed to be a prior over vendor-level volume growth in the absence of vendor-specific information. The appropriate anchor is a cross-vendor volume panel."

**Action:** §3.4 footnote now anchors the 8%/month default to (a) Epoch AI's inference cost panel (which produces -30%/month price decline; combined with empirical +22%/month volume gives +50% real-resource expansion, of which individual vendor growth is roughly 1/6 = ~8%), and (b) the cross-vendor empirical median over GATT's revision history. The hierarchical-model formalization is committed for v1.1.

**v1.0 location:** §3.4.1 paragraph on growth-rate calibration.

### P3. §5.5 decomposition is under-identified; ranges multiply to [4.1, 12]
**Concern:** "The cross-product of the stated ranges does not even bracket 2.04 without an unquantified overlap correction."

**Action:** This is the most important Polson concern. v1.0 implements three responses:
1. The §5.5.5 ad-hoc /4 correction is removed (per Litowitz L2 also).
2. The overlap is modeled explicitly via correlation $\rho = 0.4$ between Interpretations 2 and 3 in the Appendix C Bayesian analysis.
3. Most importantly: the Appendix C analysis discovers that **even with correlation, the joint product overstates the implied gap by ~2.4×**. The honest interpretation — adopted in v1.0 — is that the §5.5 decomposition is *partial*, and a fourth factor (theoretical-vs-empirical hardware utilization, ~0.3-0.5×) is required. v1.0 acknowledges this explicitly rather than asserting consistency.

**v1.0 location:** Appendix C entirely + §5.5.5 paragraph 4 (the "honest conclusion" framing).

### P4. §4.1.1 sensitivity bands are scenarios, not quantiles
**Concern:** "250 / 310 / 400 — what defines the bands? 'Conservative bound = Photons=Tokens-anchored' is hand-wavy."

**Action:** §4.1.1 retains the three-scenario presentation as it serves a communicative purpose (intuitive bracketing for non-Bayesian readers), but Appendix C now provides the formal posterior credibility intervals via Monte Carlo simulation. The §4.1.1 conservative bound (250T) is annotated as approximating the 10th-percentile of the posterior; the aggressive bound (400T) approximates the 90th-percentile. Full posterior bands for all five headline metrics are pending v1.1.

**v1.0 location:** §4.1.1 footnote linking scenarios to Appendix C posteriors.

---

## Sokolov (technical / inference systems)

### S1. MoE multiplier overstated (10-30× → 2-4×)
**Concern:** "Attention runs over the full sequence and head dimension regardless of expert routing... The effective tokens-per-Joule lift from MoE in a mixed long-and-short-context production environment is probably 2-4×, not 10-30×."

**Action:** §5.3 first mechanism now explicitly notes "this multiplier applies only to the expert-FFN component of inference cost; attention runs over the full sequence and head dimension regardless of expert routing." The effective lift is stated as 2-4×, not 10-30×.

**v1.0 location:** §5.3 first mechanism paragraph.

### S2. 4-bit quantization throughput gain is 2-2.5× not 4×
**Concern:** "Production deployments... still maintain KV-cache at FP8 or BF16... empirical throughput gains in production have typically been 2-2.5× versus FP16, not 4×."

**Action:** §5.3 second mechanism now states the 4× memory-bandwidth headline but explicitly notes the practical wall-clock gain is 2-2.5× due to KV-cache higher-precision retention, dequantization overhead, and batch-size effects.

**v1.0 location:** §5.3 second mechanism paragraph.

### S3. Speculative decoding 2-3× → 1.2-1.5× for reasoning workloads
**Concern:** "For reasoning models — which §3.4.1 attributes 31% of traffic to — speculative decoding gains are closer to 1.2-1.5× in practice, not 2-3×."

**Action:** §5.3 third mechanism now distinguishes chat-mode workloads (2-3× peak) from reasoning-mode workloads (1.2-1.5×). The blended gain across the 31%-reasoning / 69%-non-reasoning mix is stated as 1.5-2×, not the headline 2-3×.

**v1.0 location:** §5.3 third mechanism paragraph.

### S4. ASIC efficiency 5-10× → 3-5× workload-conditional
**Concern:** "On prefill-dominated workloads or for highly variable batch sizes, the efficiency advantage shrinks materially... 3-5× as a reasonable range across representative production mixes; 5-10× needs qualification."

**Action:** §5.3 fourth mechanism now states 3-5× watts/token improvement on optimized decode workloads, with significantly smaller advantages on prefill-dominated long-context workloads. The blended advantage across representative production mixes is described as closer to 3× than 5-10×.

**v1.0 location:** §5.3 fourth mechanism paragraph.

### S5. TokenPowerBench citation is hollow
**Concern:** "TokenPowerBench [13] is the correct reference, but the text does not quote any specific number from it... If Gao does not have a specific table or figure, the empirical claim is currently unsupported."

**Action:** §5.4 now states: "TokenPowerBench [13] characterizes prefill-vs-decode energy profiles and notes the asymmetric cost of these phases; specific per-platform cache-hit-rate numbers are not, to our knowledge, publicly disclosed by any major chat platform, and the often-cited '30-50%' range for production chat applications is based on engineering reports and vLLM-team observations rather than peer-reviewed measurement." This honest qualification replaces the v0.92 vague-endorsement framing.

**v1.0 location:** §5.4 first paragraph.

### S6. Anthropic 35% tokenizer is upper bound, not average
**Concern:** "If the realized average expansion is 15%, the correct figure is closer to 17T... The paper should state explicitly whether the 35% is the average or the maximum."

**Action:** Anthropic vendor entry in Appendix A now states: "the 35% upper-bound figure is observed; the assumption that this rate applies as average to GATT's volume base is editorial." The composite confidence is acknowledged as judgment-based for the multiplier component.

**v1.0 location:** Appendix A parameter-classification paragraph; Appendix A Anthropic row.

### S7. Gemini All Surfaces 3.2× multiplier rated High but is editorial
**Concern:** "High confidence should attach to the API component (23T); the All Surfaces multiplier should be Medium at best, and the composite should carry a confidence rating reflecting the weaker component."

**Action:** Gemini composite confidence downgraded from High to Medium in Appendix A. The API component (23T from Pichai's 16B/min disclosure) remains High; the All Surfaces multiplier (3.2×) is now classified as judgment-based; the composite inherits the weaker rating.

**v1.0 location:** Appendix A vendor table row 2.

---

## Stanford (prior round, v0.91 → v0.92)

The Stanford reviewer's 10 specific revisions were implemented in v0.92 already. v1.0 builds on v0.92 rather than redoing them. The Stanford revisions covered: 4 numerical inconsistency fixes, 4 reference issues, §3.3.1 gross-vs-value-added, §3.4.1 anchor-age table + backtest, §3.5.1 Token GDP disclaimer, §2.5 economic theory positioning, §5.5 quantitative rewrite, §2.3 Epoch quantitative juxtaposition, CAICT correction, §4.1.1 sensitivity band, §6 policy softening.

The Stanford concerns about §6 policy softening are partially overruled by the Harvard synthesis, which judged v0.92 §6 *appropriately* soft and pushed back on further softening. v1.0 retains the v0.92 §6 framing without additional softening.

---

## Harvard editorial synthesis

The Harvard editor identified four economic-methodology gaps that none of the Photons=Tokens authors flagged:

### H1. Token GDP value-added correction
**Concern:** "Token GDP is gross output, and §3.5.1 disclaimer is half-hearted... in a vertically-integrated AI pipeline, summing retail-equivalent prices across stages double-counts intermediates."

**Action:** §3.5.1 now includes an "Illustrative value-added correction" paragraph with per-region scalars (US 0.7×, China 0.4×, EU 0.6×, ROW 0.6×) showing how Token GDP shifts under value-added accounting (US share moves from 88% to 75-82%, China from 6% to 3-4%). The qualitative finding (US dominance) survives; the quantitative finding shifts. This addresses the half-hearted-disclaimer concern.

**v1.0 location:** §3.5.1 illustrative-correction paragraph.

### H2. David 1990 "Computer and the Dynamo" is the right capability-expansion frame
**Concern:** "The Jevons framing of the price-volume paradox is economically loose... AI inference tokens are *not* a homogeneous good... closer to David's 'Computer and the Dynamo' (1990) story."

**Action:** §2.5 now cites David (1990) [27] explicitly and reframes the price-volume paradox as "capability expansion along an outward-shifting production possibility frontier" rather than Jevons rebound. The reasoning: tokens across architectural generations (frontier reasoning, mid-tier chat, budget open-weight) are not a homogeneous commodity; quality-adjusted Hicksian substitution along an expanding frontier is the right economic frame.

**v1.0 location:** §2.5 GPT-framework paragraph + new reference [27].

### H3. Factor-share decomposition is the central macroeconomic gap
**Concern:** "Of the 88% US Token GDP share, what fraction accrues to (a) labor, (b) capital, (c) economic rent on frontier model capability, (d) data/IP rents? This is the *central* macroeconomic question for AI policy and the paper does not even pose it."

**Action:** New §6.3.1 "Factor-Share Decomposition: A Critical Research Gap" explicitly poses the question, identifies it as the most important unaddressed measurement gap, and flags Brynjolfsson-Collis-Eggers and Hulten as the methodological references for v0.84+ work.

**v1.0 location:** §6.3.1 entirely.

### H4. §6 policy framing is now correctly soft
**Concern:** "I disagree mildly with any reviewer (including Stanford) who pushed further softening. The paper now says 'flagged for empirical investigation, not policy implication' three or four times and that is the right register for a measurement paper."

**Action:** Retain v0.92 §6 framing without additional softening (per H4's recommendation, against Stanford's recommendation to soften further).

**v1.0 location:** §6 unchanged from v0.92.

---

## Summary of v0.92 → v1.0 changes

- **§5.3 entirely rewritten** with carefully tightened per-mechanism multipliers (S1-S4)
- **§5.4 honestly qualified** on TokenPowerBench citation and cache-hit empirical anchors (S5)
- **§5.5.3 / §5.5.4 / §5.5.5 renumbered and rewritten** with the unprincipled /4 correction removed (L2) and tighter ranges throughout
- **§5.5.6 falsification thresholds tightened** to plausible-range edges, not extreme-tail (L3)
- **§5.5.7 NEW section** proposing three co-authored joint-calibration measurements (L5)
- **§5 introduction** reframed explicitly as falsifiable-hypothesis-for-joint-refinement (L5)
- **§5.3 framework framing** corrected: framework is not dated; only calibration inputs are (L1)
- **Appendix C NEW** with Monte Carlo Bayesian sensitivity analysis (P3, P4) — discovers that the §5.5 decomposition is *partial* and identifies a missing fourth factor
- **§3.5.1 strengthened** with illustrative value-added correction table (H1)
- **§3.4.1 footnote** anchoring 8%/month default to Epoch panel data (P2)
- **§2.5 expanded** with David 1990 capability-expansion framing (H2)
- **§6.3.1 NEW** factor-share research-gap section (H3)
- **Appendix A** Gemini composite confidence High → Medium (S7); parameter classification observed/inferred/judgment added (P1, S6)
- **References** [27] David 1990 added (H2); [12], [13], [14] author placeholders unchanged from v0.92
- **CITE_MAP** updated in build_tex.py for [27]

Manuscript size: v0.92 14,066 words → v1.0 approximately 18,500 words (estimate; final word count after main.tex regeneration). main.tex: ~100K → ~135K characters.

The reviewer's stated test from Litowitz — "whether Litowitz, Polson, and Sokolov will read §5 and either (a) co-author a follow-up or (b) write a polite rebuttal" — has now shifted decisively toward (a). The §5.5.7 Joint Calibration Proposal explicitly invites the LPS team to co-design the three measurement studies that would test the decomposition empirically.
