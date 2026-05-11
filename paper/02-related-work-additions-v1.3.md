# Proposed paper additions for v1.3 → v1.4 revision

**Status**: Draft. NOT yet merged into main paper. Awaits final review before integration into `paper/01-introduction.md` and `paper/02-related-work.md`.

**Triggered by**: (a) GTC 2026 Jensen keynote 公开命名 "token economics" 作为 NVIDIA 核心叙事；(b) Google AI Overview / GEO 调研发现 TokenOps + 区块链 + 行为心理学三方共占 "tokenomics" 词条；(c) Opus 第一性原理 verdict 建议 dialogue partner 扩展。

---

## §1.2 NEW — Disambiguation: Token Economy vs Tokenomics vs Token Economy (Psychology)

Three distinct concepts use "token" in adjacent vocabulary, and confusion among them substantially limits this paper's discoverability and citation pathways. We disambiguate explicitly:

**"Token Economy" (this paper)** refers to the global market for AI inference token production, distribution, and consumption — the empirical phenomenon GATT measures. Throughput is measured in trillions of tokens per day across 24 vendors and 12 countries; economic value is measured in retail-equivalent USD (Token GDP). This is a *macro-empirical* construct.

**"Tokenomics" / "Token Economics" (blockchain)** [Wikipedia] refers to the supply dynamics, distribution mechanics, and incentive structures of cryptocurrency tokens within distributed ledger networks. The term is decade-old in the cryptocurrency literature and substantially predates the LLM-token usage. When a general reader queries "tokenomics" via Google AI Overview, blockchain content dominates the response by default.

**"TokenOps" / "FinOps for AI" (enterprise cost management)** [Finout 2024, Healthark 2025, Inventive HQ 2025, arXiv:2507.03254] refers to operational disciplines for tracking and optimizing LLM token consumption at the firm level — prompt structure efficiency, request batching, cost attribution. This is a *micro-operational* construct, applied at single-firm scale, with commercial SaaS offerings (Finout, BMC Helix, etc.). TokenOps and the present paper are complementary: TokenOps optimizes within-firm token consumption; this paper measures and aggregates across-firm token consumption at the global level.

**"Token Economy" (behavioral psychology)** [PMC 2025, EBSCO research starter] refers to a behavior-modification intervention from 1960s clinical psychology — physical tokens earned for target behaviors, exchanged for backup reinforcers. This usage predates both AI and blockchain by decades but operates in a distinct disciplinary literature with no overlap to the present work.

The vocabulary collision is not merely terminological. It directly shapes the discoverability of token-economy research via large-language-model-mediated search ("Generative Engine Optimization"). We propose that the AI-inference meaning of *"Token Economy"* is the appropriate empirical-macroeconomic counterpart to *"Tokenomics"* (blockchain-supply-side) and to *"TokenOps"* (firm-level cost management), and we use the term consistently in this sense throughout.

---

## §2.7 NEW — Industry Framing: NVIDIA GTC 2026 Token Economics

In May 2026, NVIDIA's GTC keynote (Huang 2026) introduced a publicly articulated "Token Economics" framework as the company's core narrative for the Blackwell-to-Vera-Rubin architecture transition. The framework plots two axes: **tokens per watt** (Y, throughput per power input) and **tokens per second per user** (X, interaction speed, presented as a proxy for inference quality / "AI smartness"). Huang's central claim: in a power-constrained world, architectural efficiency on this two-axis surface determines annual revenue per gigawatt of installed inference capacity, with Rubin delivering 5× the 1GW-datacenter annual revenue of Blackwell ($30B → $150B) through 2-10× efficiency gains across user-tier service levels.

This industry framing is the **supply-side, capacity-imputed counterpart** to the present paper's *demand-side, consumption-measured* approach. The two constructs are best understood through the GDP-accounting analogy: NVIDIA's framework is the *production-side* aggregate (factory output × imputed pricing × utilization); GATT's Token GDP is the *expenditure-side* aggregate (realized vendor revenue from observed token consumption). In a closed token economy, the two should equal each other up to a statistical discrepancy; their measured difference is itself a research output (parallel to the production-vs-expenditure GDP discrepancy in national accounts, which is a recurring research topic in Chinese and US national income data).

Two methodological tensions in the NVIDIA framing are worth flagging. First, the X-axis "TPS/user as proxy for AI smartness" implicitly aggregates *output tokens* and *hidden reasoning tokens* (chain-of-thought traces from o1-class reasoning models). Modern reasoning models emit 50-200K reasoning tokens per user-visible answer; whether the framework counts these in Y-axis throughput, in X-axis TPS, in both, or in neither is not specified in the GTC presentation. This is the *reasoning-token asymmetry* — a structural ambiguity that affects both supply-side and demand-side accounting and that Section 5.5 of the present paper addresses through Token Velocity decomposition.

Second, the NVIDIA framework treats "1 token" as a homogeneous unit across vendors and models. Cross-vendor tokenizer fungibility (Section 3.2 and Appendix A) is a methodological prerequisite for any token-denominated aggregate; the GTC presentation does not surface it. We propose that demand-side empirical measurement (this paper) and supply-side capacity modeling (Huang 2026; Litowitz et al. 2026) are complementary frameworks that jointly constrain the global Token Economy more tightly than either alone.

---

## §2.8 NEW — Enterprise Token Cost Management: TokenOps and FinOps for AI

A parallel literature in enterprise operations — variously labeled "TokenOps" or "FinOps for AI" — addresses token consumption at the single-firm level. Representative work includes Finout's *Definitive Guide to FinOps for Tokens* (2024), Healthark Insights' *Token Economics: Measuring and Optimizing the Cost of Intelligence* (2025), Inventive HQ's *Optimize Prompts to Reduce Token Costs* (2025), and the academic survey arXiv:2507.03254. Commercial SaaS implementations — Finout's TokenOps platform, BMC Helix's AI cost-tracking modules, and similar offerings from CloudHealth, Apptio, and others — provide firm-level dashboards on the dimensions of cost, latency, and model-routing efficiency.

This literature is *micro-operational*: its unit of analysis is the firm, its objects are prompt structure / batch geometry / model selection, and its outputs are cost-per-output-quality optimization decisions. The present paper's unit of analysis is the global system, its objects are vendor-level volumes and pricing, and its outputs are macro-empirical aggregates (Token GDP, per-capita gaps, distributional Gini). The two frameworks are connected by an obvious accounting identity: the sum of all firm-level token expenditures across firms in a region equals (up to measurement error) the region's Token GDP at the macro level.

We see two specific complementarities. First, TokenOps frameworks provide validation of the *price-per-million-tokens* parameters that enter Token GDP calculations — their cost-management product literature documents realized blended pricing across model selections and vendor mixes. Second, the present paper's macro-aggregate datasets provide the *denominator* for any firm-level benchmarking question of the form "are we paying above or below the typical industry token rate?" — a question TokenOps SaaS products implicitly answer through opaque proprietary baselines but which an open dataset like GATT can answer transparently.

GATT and TokenOps are not competing methodologies. They occupy distinct scales (global-macro vs. firm-micro) and serve distinct audiences (researchers / policy analysts vs. enterprise FinOps teams). The present paper proposes a productive division of labor: TokenOps platforms operationalize within-firm cost control; the Token Economy literature (this paper, NVIDIA GTC 2026 framing, Photons=Tokens physical-ceiling work) provides the macro context within which firm-level decisions are made.

---

## Notes on integration

- §1.2 inserts after current §1.1 introductory paragraphs, before §1.2 (existing). Renumber existing §1.2-1.4 → 1.3-1.5.
- §2.7 and §2.8 append to existing §2 Related Work. Current §2.5 (David 1990 / Brynjolfsson J-curve framing) and §2.6 (GATT positioning) remain unchanged.
- §2 ordering rationale: A → B → C → Industry (Jensen) → Operations (TokenOps) → GATT (existing §2.6). This places GATT positioning AFTER all dialogue partners.

## References to add to `references.bib`

```bibtex
@misc{huang2026gtc,
  author = {Huang, Jensen},
  title = {{Token Economics: From Blackwell to Vera Rubin}},
  year = {2026},
  howpublished = {GTC 2026 Keynote},
  note = {Presented May 2026; \$1T total Blackwell + Vera Rubin order backlog through 2027}
}

@misc{finout2024tokenops,
  author = {{Finout}},
  title = {{Token Economics and TokenOps: The Definitive Guide to FinOps for Tokens}},
  year = {2024},
  url = {https://www.finout.io/blog/token-economics-and-tokenops-the-definitive-guide-to-finops-for-tokens}
}

@misc{healthark2025tokenecon,
  author = {{Healthark Insights}},
  title = {{Token Economics: Measuring and Optimizing the Cost of Intelligence}},
  year = {2025},
  url = {https://medium.com/@healthark.ai/token-economics-measuring-and-optimizing-the-cost-of-intelligence-ca1a47fe635c}
}

@misc{inventivehq2025promptopt,
  author = {{Inventive HQ}},
  title = {{Optimize Prompts to Reduce Token Costs}},
  year = {2025},
  url = {https://inventivehq.com/blog/optimize-prompts-reduce-token-costs}
}

@misc{tokenfinops2025survey,
  author = {Anonymous},
  title = {{A Survey of FinOps for LLM Token Cost Management}},
  year = {2025},
  eprint = {2507.03254},
  archivePrefix = {arXiv}
}
```

build_tex.py CITE_MAP needs extension: huang2026gtc → [28], finout2024tokenops → [29], healthark2025tokenecon → [30], inventivehq2025promptopt → [31], tokenfinops2025survey → [32].
