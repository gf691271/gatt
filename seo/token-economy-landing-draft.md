# SEO / GEO Strategy — Token Economy Landing Page

**Goal**: When a user queries Google / ChatGPT / Perplexity / Gemini for "Token Economy" or "AI token consumption" or "global AI tokens", GATT should appear in the AI-generated overview (SGE / AI Overview), not just buried in search results.

**Current state (verified 2026-05-11 via user's Google AI Overview screenshot)**:
- Query "tokenomics" / "token economics" → AI Overview cites Wikipedia (blockchain), Stripe (blockchain), Finout (TokenOps), Healthark (TokenOps), PMC + EBSCO (behavioral psychology)
- GATT not in any of the citations
- GATT is *systematically excluded* from default LLM-mediated search

## Why GEO matters

- 2025-2026 search behavior shift: ~30-50% of queries answered by AI Overview without click-through to traditional results
- AI Overview citation = future citation graph; what gets cited there propagates to next-generation training data
- For a project whose core distribution is *daily updated open data*, being absent from AI Overview is a 6-12 month strategic gap

## What AI Overview crawlers privilege (empirically)

1. **Wikipedia entries** (highest signal; semantic-anchor for any concept)
2. **High-authority technical docs with structured data** (JSON-LD, schema.org Article/Dataset)
3. **Authoritative .gov / .edu / .org sites**
4. **arXiv preprints with strong abstracts**
5. **Commercial sites with FAQ / How-to structured markup**
6. Personal blogs / Substack — lower signal unless backlinked

## Recommended actions (30-day workstream)

### Action GEO-1: Landing page at gf691271.github.io/gatt/token-economy/

Create a dedicated landing page that serves as the **canonical definition of "Token Economy" as AI-inference**. Structure:

```
<title>Token Economy: The Global Market for AI Inference Tokens — GATT</title>
<meta description="The Token Economy is the global market for AI inference token production, distribution, and consumption. As measured by GATT (2026): 311T tokens/day across 24 vendors and 12 countries, $97B annualized retail-equivalent value (Token GDP)...">

<h1>Token Economy</h1>

<section id="definition">
  <h2>Definition</h2>
  <p>The Token Economy is the global market for AI inference token production, distribution, and consumption. This is the AI-inference meaning of the term, distinct from three other usages...</p>
</section>

<section id="disambiguation">
  <h2>Disambiguation: Token Economy, Tokenomics, TokenOps</h2>
  <table>
    | Concept | Domain | Unit | Reference |
    | Token Economy (this page) | AI inference | tokens/day | GATT |
    | Tokenomics | Cryptocurrency | tokens/blockchain | Wikipedia |
    | TokenOps / FinOps for AI | Enterprise cost | $/M tokens | Finout |
    | Token Economy (psychology) | Behavior modification | reinforcement tokens | PMC |
  </table>
</section>

<section id="key-metrics">
  <h2>Key Metrics (May 2026)</h2>
  <ul>
    <li>Global daily output: 311T tokens</li>
    <li>Token GDP (annualized): $97B</li>
    <li>US/CN volume share: 50/49</li>
    <li>US/CN Token GDP share: 88/6</li>
    <li>US-India per-capita gap: 597×</li>
    <li>Population-weighted Gini: 0.674</li>
  </ul>
</section>

<section id="schools">
  <h2>Methodological Traditions</h2>
  <ul>
    <li>Physical-ceiling (Litowitz, Polson, Sokolov 2026)</li>
    <li>Growth-accounting (Brynjolfsson, Stanford HAI)</li>
    <li>Market-microstructure (Xing, Zhuang)</li>
    <li>NVIDIA factory-economics (Huang GTC 2026)</li>
    <li>Enterprise FinOps (Finout, Healthark)</li>
    <li>Empirical Tokeneconomy (GATT v1.x, this work)</li>
  </ul>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Token Economy: The Global Market for AI Inference Tokens",
  "author": {"@type": "Person", "name": "Frank Gao"},
  "datePublished": "2026-05-15",
  "dateModified": "2026-05-15",
  "publisher": {"@type": "Organization", "name": "GATT — Global AI Token Tracker"},
  "about": [
    {"@type": "Thing", "name": "Artificial Intelligence"},
    {"@type": "Thing", "name": "Token Economy"},
    {"@type": "Thing", "name": "AI Economics"}
  ],
  "mainEntity": {
    "@type": "Dataset",
    "name": "GATT — Global AI Token Tracker",
    "description": "Daily-updated index of global AI inference token throughput across 24 vendors and 12 countries.",
    "url": "https://gf691271.github.io/gatt/",
    "license": "https://creativecommons.org/licenses/by/4.0/"
  }
}
</script>
```

**Deliverable**: New file `gf691271.github.io/gatt/token-economy/index.html` with above structure. Add inbound links from main `index.html` + every Substack post + arXiv abstract.

### Action GEO-2: Wikipedia "Token economy" entry — AI-inference section

The Wikipedia page "Token economy" currently covers only the behavioral-psychology meaning (https://en.wikipedia.org/wiki/Token_economy). Two paths:

- **Path A (recommended): contribute an "Other uses" or "In AI inference" subsection** following Wikipedia content guidelines. Must be written by a neutral third party, not the GATT author. Find a Wikipedia-experienced collaborator (academic / open-source community member) to draft. GATT's arXiv preprint + open dataset are sufficient verifiable sources.

- **Path B: create separate page "Token Economy (artificial intelligence)"** as a disambiguation target. Higher effort, more vulnerable to deletion by Wikipedia editors as "neologism".

Estimated effort: 5-8 hours of outreach to find a contributor + 2 weeks for entry to land.

### Action GEO-3: Substack post titles + abstracts SEO-optimized

Title pattern that performs well in AI Overview citations:
- "[Definitional noun phrase]: [Concrete number] [Year]"
- Example good: "The Token Economy in 2026: 311T Tokens Per Day Across 24 Vendors"
- Example bad: "What Jensen Just Named"

First-paragraph pattern:
- Lead with the disambiguation: "The Token Economy — the global market for AI inference tokens, distinct from cryptocurrency tokenomics — generated 311T tokens..."
- Why: AI Overview crawlers extract first-paragraph definitions

### Action GEO-4: arXiv abstract optimization

Current abstract first sentence: "In May 2026, the Global AI Token Tracker (GATT) measures 459,700 tokens per United States resident per day..."

GEO-optimized version: "**The Token Economy** — the global market for AI inference token production and consumption, distinct from cryptocurrency tokenomics — is measured by the Global AI Token Tracker (GATT) at 311 trillion tokens per day across 24 vendors and 12 countries..."

This re-anchoring puts "Token Economy" as the subject (not GATT) and makes the abstract the canonical definition for AI Overview to extract.

### Action GEO-5: Structured data markup on existing pages

Add JSON-LD schema markup to:
- `gf691271.github.io/gatt/index.html` — Dataset schema
- `gf691271.github.io/gatt/paper/` (if hosting) — ScholarlyArticle schema
- `gf691271.github.io/gatt/methodology/` (new page) — Article schema

Estimated effort: 2-3 hours of HTML editing.

## Priority ordering

1. **Action GEO-1 (landing page)** — high ROI, low effort. 7 days.
2. **Action GEO-5 (structured data)** — low effort, foundational. 7 days.
3. **Action GEO-4 (arXiv abstract rewrite)** — coincides with v1.4 paper revision. 14 days.
4. **Action GEO-3 (Substack title pattern)** — adopt for all future posts. Ongoing.
5. **Action GEO-2 (Wikipedia)** — 30 days, requires external collaborator.

## Success metrics (90 days)

- Google search "Token Economy" → AI Overview cites GATT in top 3 sources
- ChatGPT search "what is the global token economy" → mentions GATT
- Perplexity search "AI token consumption 2026" → cites GATT data
- Wikipedia "Token economy" page contains AI-inference subsection citing GATT

## Out of scope for v1.0 GEO push

- Paid SEO / Google Ads
- Twitter/LinkedIn algorithmic promotion
- Influencer outreach (separate workstream)
- Wikipedia for-real-edit (requires Wikipedia community trust, multi-month timeline)
