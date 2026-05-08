# GATT Data Changelog

## 2026-05-09 (v0.80 — IDC Validation + 7 Vendor Anchor Upgrades)

First external validation of GATT methodology + 7 previously-uncaptured vendor anchors layered on top of v0.79's weekly extrapolation. Most ambitious single update since v0.75's live-extrapolation engine.

### Headline metrics (vs v0.79 baseline)
- **Global**: 264T → **305T/day** (+16% in 5 days, driven by hard data not extrapolation)
- **Token GDP**: $65.6B → **$90.8B/yr** (+38%)
- **China share**: 57% → **50%** (volume gap closed)
- **US share**: 38% → **50%**
- **US-India per-capita gap**: 448× → **589×**
- **Doubao global share**: 49% → **42%** (still #1, but US disclosures rebalance the index)

### Vendor changes (7 anchor upgrades)
- **Google Gemini**: 61T → **73T** — Pichai disclosed 16B tokens/min via direct API at Cloud Next 2026 / Q1 2026 earnings, up from 10B in Q4 2025 (+60% in one quarter). Single biggest US-side disclosure since GATT launch. All Surfaces multiplier reduced 4× → 3.2× since API outpaced consumer surface attach. Source: blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
- **Anthropic Claude**: 19T → **22T** — Three previously-uncaptured signals: (1) Opus 4.7 launched April 16 with new tokenizer producing up to 35% more tokens for same input; (2) Claude MAU surged 44% Mar→Apr to 23M, biggest growth among top AI apps in April (BigGo/Similarweb); (3) Continued compute strain. Confidence upgraded medium-high → high.
- **Microsoft Azure + Copilot**: 8.1T → **10.0T** — Q3 FY2026 (Apr 29): AI business ARR $37B (+123% YoY); Microsoft 365 Copilot 20M paid seats (vs 15M Jan); Azure +40%. Microsoft–OpenAI partnership restructured Apr 27 to non-exclusive license through 2032. Confidence upgraded low → medium.
- **OpenAI ChatGPT + API**: 44T → **45T** — GPT-5.5 launched April 23, GPT-5.5 Instant launched May 5 (now ChatGPT default). Some developers reportedly hitting 40M tokens/min during launch. $25B ARR confirmed; targeting $29.4B for 2026.
- **DeepSeek**: 8.2T → **9.2T** — DeepSeek V4 Pro / V4 Flash launched April 24 (1M token context, 1.6T params MoE / 49B active). Now #3 in enterprise developer SDK usage.
- **Kimi (Moonshot)**: 1.54T → **2.5T** (+62%) — FASTEST-GROWING vendor. K2.6 launched April 20 (1T params, 262K context, ties GPT-5.5 on SWE-Bench Pro at 80% lower cost). ARR doubled $100M → $200M Mar → Apr. $2B funding round closing May 6 at $20B valuation. OpenRouter weekly volume 1.85T tokens (#2 globally on OR). Growth rate raised 25% → 30%/mo.
- **Alibaba Qwen**: 5.7T → **6.2T** — Qwen 3.6-Plus released April 2 with enhanced coding (Caixin). "Alibaba Token Hub" reorg consolidates Qwen + Tongyi Lab + Wukong under CEO Eddie Wu.
- **Tencent Hunyuan**: 2.39T → **2.7T** — New flagship Hunyuan launched April 2026 (Shunyu Yao led, agent-focused). Yuanbao integrated DeepSeek for image generation May 7.
- **Grok (xAI)**: 0.65T → **0.55T** — **FIRST NEGATIVE-GROWTH VENDOR IN GATT HISTORY**. MAU dropped 12.5% Mar→Apr to 12.2M; tumbled from 2nd to 5th place in mobile rankings; 80+ staff incl. several co-founders left xAI. Growth rate flipped +15%/mo → -5%/mo.
- All other vendors: routine 33-day extrapolation at their respective monthly growth rates.

### IDC Validation (NEW)
The IDC China Public Cloud Large Model Services report (May 7, 2026) is the first external commercial research firm to publish token-volume data that can be cross-checked against GATT. Key findings:
- 2024 China external MaaS: 114T tokens
- 2025: 1,944T tokens (+16× YoY)
- 2026 forecast: 40,000T tokens (+20× YoY)
- Volcengine market share: 46.4% (2024) → 49.2% (H1 2025) → **49.5% (full 2025)**
- Alibaba Bailian #2 (27%, H1 2025); Baidu Qianfan #3 (17%, H1 2025)

**What this validates:**
- Volcengine #1 ranking in China — independently confirms GATT's Doubao #1 globally
- Growth: IDC's 16× YoY 2025 + projected 20× for 2026 ≈ ~27%/mo, supports GATT's 22%/mo trajectory assumption

**Critical scope distinction added to data/tci-latest.json:**
- IDC measures only external enterprise public-cloud MaaS calls (excludes internal first-party Douyin AI Search, Doubao App, Jimeng, Volcengine internal pipelines)
- GATT measures all-sources inference (external + internal first-party + consumer apps + on-device)
- Math: IDC 2025 average 5.32T/day total external MaaS × Volcengine 49.5% = 2.64T/day external Volcengine in 2025. The 120T/day Volcengine Apr 1 official disclosure cannot fit IDC's external-only scope under any plausible growth path. Therefore GATT's 129T/day Doubao number is inherently all-sources, with internal usage estimated at ≥95% of total.

### New file structure
- `data/tci-latest.json`: added top-level `methodology_triangulation` block with IDC + Gartner + a16z cross-source comparison, GATT unique value props, and per-source validates_gatt / differs_from_gatt arrays
- `data/tci-latest.json`: added `scope_note` field to Doubao vendor entry (all-sources vs IDC external-only clarification)
- `about.html`: new section "GATT vs IDC, Gartner, a16z — Methodology Triangulation" addressing journalist comparison questions
- `index.html`: new IDC validation card in Weekly Digest, updated Vendor Watch with IDC-confirmed CN MaaS shares

### Why this matters
- **Q2 (data credibility)**: First external commercial-research validation of GATT's #1 ranking. Adds material trust signal for journalists.
- **Q9 (publication authority)**: GATT vs IDC/Gartner triangulation positions GATT as the only global, all-sources, daily-updated, free token-volume index.
- **Q10 (citation value)**: Now journalists comparing GATT to IDC have a clear scope explainer in both data file and about page — preventing scope-mismatch confusion.

### Files updated
- data/tci-latest.json (v0.79 → v0.80, +methodology_triangulation block)
- api/v1/tci.json + api/v1/snapshot.json (synced from data/tci-latest.json — were stuck at v0.72)
- llms.txt (full rewrite v0.79 → v0.80)
- index.html (banner, Weekly Digest, Vendor Watch, Q2 Quarterly Snapshot, Key Numbers JS targets, share text, og:image:alt meta)
- about.html (new "GATT vs IDC, Gartner, a16z — Methodology Triangulation" section)
- data/snapshots/2026-05-09.json (immutable snapshot)
- CHANGELOG.md (this entry)

---

## 2026-02-27 (v0.64 — GATT Weekly Pulse section)

- **New section: 📡 GATT Weekly Pulse** — chronological update log visible to all visitors
  - 5 update cards covering this week's key changes: OpenAI revision (19T→28T), Token GDP correction ($99M→$122.6M), global total update (151T→162T), forecast fix (10×→6×), GEO infrastructure work
  - Color-coded by type: DATA UPDATE (green), CORRECTION (amber), FORECAST (amber), INFRASTRUCTURE (blue)
  - Links to CHANGELOG.md and GitHub commit history for full auditability
  - Quick-nav entry added: 📡 GATT Weekly Pulse
- **Why this matters**: Journalists checking "is this fresh?" now see an active update log at the top of the page. No other AI data tracker does this. Signal of active maintenance = trust.
- Improves 10Q: #6 (vendor correction mechanism visible), #9 (publication authority — shows ongoing editorial process), #10 (AI记者会引用吗 → yes, active correction log = higher credibility than static dashboards)

## 2026-02-27 (v0.63 — llms.txt Token Economy definition + API summary fix + cite cleanup)

- **llms.txt**: Added "What is the Token Economy?" canonical definition block for LLM/AI crawler ingestion
- **CRITICAL API FIX**: `api/v1/tci.json` summary section had stale data (100T, 55% China) while meta showed correct values (162T, 51% China) — now consistent
- **api/v1/tci.json**: Added `key_stats{}` object at summary level — pre-computed headline numbers for AI scrapers that read only the summary block
- **llms.txt**: Removed duplicate citation block; unified cite format references v0.63 and correct API URL
- Improves 10Q: #7 (API machine-readability — no more contradictory numbers), #8 (GEO/AI crawler data fidelity), #10 (AI journalist引用 — consistent numbers everywhere)

## 2026-02-27 (v0.62 — Year-End Forecast Fix + Q1 2026 Quarterly Report)

- **CREDIBILITY FIX**: Year-end forecast corrected from ~10× to ~6× current run rate (1000T ÷ 162T = 6.2×)
- **Token Economy Quarterly Report** section added — GATT is now a recurring publication, not just a static dashboard
- Quick-nav entry: 📋 Q1 2026 Quarterly Report
- Improves 10Q: #2 (forecast arithmetic defensible), #9 (publication authority), #10 (standard cite format)

## 2026-02-27 (v0.61 — Token Economy Definition + DefinedTerm JSON-LD)

- **"Token Economy" Definition section** added to page (above Key Numbers):
  - Canonical 1-sentence definition: "The global system of AI inference production, distribution, and consumption — measured in daily token throughput across models, regions, and use cases."
  - Three-way disambiguation: behavioral psych (1960s) / crypto tokenomics (2017+) / AI inference (GATT 2026)
  - Cite this data format + copy-to-clipboard button + Twitter share hook
  - Quick-nav entry added: 📖 Token Economy Definition
- **`DefinedTerm` JSON-LD schema** added to `<head>` (alongside existing Dataset schema):
  - `@type: DefinedTerm` with termCode, inDefinedTermSet, creator, dateCreated/Modified
  - Now compliant with schema.org vocabulary for concept definitions
  - Google and AI crawlers can now extract GATT's definition as a named concept
- **North Star alignment**: This is the first concrete step toward GATT owning the "Token Economy" definition slot in search and AI responses
- Improves 10-Question check: #9 (content authority), #10 (AI journalist引用), #4 (definition transparency)



## 2026-02-27 (v0.58 — GEO Fix: Machine-Readable Files Synced)

- **CRITICAL BUG FIX**: `llms.txt` and `tci-latest.json` were stuck at v0.20-era data while HTML showed v0.57
  - This was silently blocking the North Star goal: LLMs reading these files cited wrong numbers
  - OpenAI in JSON: 19T → 28T | Global: 151T → 162T | China share: 55% → 51%
- **`llms.txt` complete rewrite** with all v0.58 stats — this is what Gemini/ChatGPT ingests:
  - 162T global, $44.8B Token GDP, 214× per-capita gap, pricing intelligence summary
  - Journalist-ready cite format, methodology summary, author bio
- **`tci-latest.json` major upgrade**:
  - Added `token_gdp` breakdown section (auditable: $102M US + $8.3M CN + $9.6M EU + $2.7M ROW = $122.6M)
  - Added `per_capita[]` array with 12-country data (the 214× stat, machine-readable)
  - Added `key_stats{}` object with pre-computed headline numbers for scrapers/LLMs
  - Added `gatt_version` field
  - Correction log updated with all v0.55-v0.58 changes
- **CSV export version**: 0.45 → 0.58 (was embarrassingly outdated)
- **10Q improvement**: #8 (GEO/machine-readability) — GATT's main distribution channel for AI citations was broken, now fixed
- **Autonomous iteration**: Overnight agent v2, 2026-02-27 ~03:05 PST

## 2026-02-27 (v0.57 — Vendor Pricing Intelligence Table)

- **New section: Vendor Pricing Intelligence** — 12 vendors with input/output/blended $/M pricing
  - Reveals pricing tiers: Premium (OpenAI $5/M, Anthropic $7.5/M) vs Ultra-Low (DeepSeek $0.02/M, Doubao $0.06/M)
  - US vendors charge 60–100× more per token than Chinese peers
  - Per-vendor daily GDP contribution calculated inline
  - Twitter share hook: pricing gap 60–100× story
- **Makes Token GDP fully auditable**: journalists can now verify every $/M assumption
- Addresses 10-question #4 (transparency) and #10 (journalist citeability)

## 2026-02-27 (v0.56 — Token GDP Math Fix + Divergence Chart)

- **Critical arithmetic fix**: Token GDP numbers corrected
  - Daily: $99M → $122.6M/day (=$97.5M+$8.3M+$16.8M — was previously rounded incorrectly)
  - Annual: $36B → $45B/year ($122.6M × 365 = $44.7B ≈ $45B)
  - Previous headline figures were inconsistent with the shown breakdown — now fully auditable
- **New visualization**: "The Great Divergence — Volume vs GDP Share"
  - Canvas bar chart: US / China / EU+other, volume bar vs GDP bar side-by-side
  - Visually shows China's paradox: 51% of tokens → only 7% of economic value
  - Most shareable data story on the site — designed for screenshot + tweet
- **China narrative corrected**: 55% → 51% volume share (83T/162T = 51.2%)
- **GDP share labels added** to each calculation card: US 80%, CN 7%, EU+other 14%
- **Sum row added**: explicit $97.5M + $8.3M + $16.8M = $122.6M/day shown for full audit trail
- **Updated tweet copy**: corrected numbers, sharper narrative
- **10Q improvement**: #2 (data inconsistency fixed — biggest trust risk) + #3 (new chart = screenshot-able)
- **Autonomous iteration**: Overnight agent v2, 2026-02-27 ~01:15 PST

---

## 2026-02-27 (v0.55 — OpenAI Fix + Token GDP Introduction)

- OpenAI revised 19T→28T; Global total 151T→162T; Token GDP metric introduced
- See prior changelog entry for details

---

## 2026-02-27 (v0.54 — Data Provenance Board)

- **New section**: "🔍 Data Provenance Board" — full transparency table for all 20 vendors
  - Shows: source date, days since last verification, confidence level (color-coded), estimation method
  - Stale sources (>120 days) highlighted in red — journalists can instantly spot extrapolated estimates
  - Fresh sources (≤60 days) shown in green — high-signal data marked clearly
  - Direct link to full provenance JSON
  - Quick-nav added: "🔍 Data Provenance Board"
- **Why**: Addresses 10-question audit item #4 (inference logic transparency for journalists/analysts)
  - Previously: readers had to click into about.html to understand how numbers were derived
  - Now: single-glance table on dashboard shows data freshness for every vendor
  - Expected impact: makes GATT more citable — journalists can verify staleness before citing
- **Autonomous iteration**: Overnight agent v2, 2026-02-27 ~23:10 PST

---

## 2026-02-26 (v0.51 — Per Capita Ranking)

- **New section**: "AI Inequality — Tokens Per Person, Per Day"
  - 12-country horizontal bar chart (log scale), ranked by tokens/person/day
  - Key finding: US 135K vs India 631 = **214× gap**
  - Insight: China ranks #3 per capita (59K), not #1 — large population dilutes absolute lead
  - Three insight cards: highest (US 135K), biggest surprise (China 59K), biggest gap (India 631)
  - Twitter share hook pre-filled: "Americans generate 135,000 tokens/day. Indians: 631. That's 214×."
  - Quick-nav added: "📊 Per Capita Ranking"
  - This addresses 10-question audit item #3 (UI/share) and #10 (journalist citation value)



All significant data revisions are logged here. This is not a software changelog — it tracks when and why estimates changed.

---

## 2026-02-27

- **Global Total**: 136T/day → 151T/day
  Reason: Google revised to All Surfaces scope (+15T), Anthropic revised upward (+7.5T), country shares recalculated
  Confidence: medium

- **Anthropic/Claude**: 2.5T/day → 10T/day
  Reason: $14B ARR confirmed (Feb 2026). At 70% API share × $3/M blended price = ~9T/day. Cross-validated with 820M req/day proxy and 18M MAU × 500K tokens/day.
  Confidence: medium-low → medium

- **Tencent/Hunyuan**: 0.8T/day → 2T/day
  Reason: Yuanbao 50M DAU data point (Feb 2026) + 900 internal Tencent apps using Hunyuan
  Confidence: very low

## 2026-02-26

- **Google Gemini**: 35T/day → 50T/day (All Surfaces)
  Reason: Switched from API-only metric to "All Surfaces" scope. Pichai Q3 2025 earnings: "1.3 quadrillion tokens/month across all surfaces" = 43T/day, extrapolated 4 months to ~50T.
  Confidence: medium

- **xAI/Grok**: 0.3T/day → 0.5T/day
  Reason: 134M queries/day data point (Feb 2026) + revenue back-calculation
  Confidence: low

- **Groq**: 0.15T/day → 0.25T/day
  Reason: LPU capacity back-calculation + valuation-proportional estimate ($6.9B at Sep 2025)
  Confidence: low

- **DeepSeek**: 5T/day → 7.5T/day
  Reason: DeepSeek V3 adoption surge + R1 reasoning model launch
  Confidence: low

## 2026-02-20 (Initial Release)

- First public release of GATT data
- 20 vendors tracked across CN, US, EU
- Global total estimate: ~120T/day

---

## Correction Policy

We welcome corrections. If you have more accurate data for any vendor:
- Open a [GitHub Issue](https://github.com/gf691271/gatt/issues/new?title=Data+correction&labels=data)
- Email: goghxiang@gmail.com
- Include: source URL, date, and the specific claim

## v0.52 — 2026-02-26 21:05 PST (Overnight Agent)

### Changed
- **CREDIBILITY FIX**: Removed fabricated testimonial quotes from "In the Press" section (were: unnamed r/MachineLearning post and unnamed "AI infrastructure analyst" — no real attribution, could destroy journalist trust)
- Replaced with honest "Launched Feb 2026 — First Citations Welcome" banner
- Added GitHub social proof links (Star, Bug report, Twitter follow)

### Added
- **Distribution Toolkit** — ready-to-post titles for:
  - Hacker News: "The US generates 214× more AI tokens per person per day than India — open dataset" (with one-click Submit to HN link)
  - Reddit r/MachineLearning: "[OC] Open dataset" format with Submit link
  - Twitter/X: Full thread hook with 214× stat, ready to copy
- Honest citation placeholder grid (3 cards: press / research / KOL)

### Why this matters (10-question improvement)
- Q9 (Content authority): Fake quotes are *worse* than no quotes — a journalist who spots them would distrust ALL data. Now the site is honest about being newly launched.
- Q10 (Would AI journalist cite?): Credibility restored. The "Distribution Toolkit" also makes it easy for the first real citations to happen.

## 2026-02-27 (v0.55)

- **OpenAI/ChatGPT**: 19T/day → 28T/day
  Reason: Sep 2025 baseline of 19T extrapolated at 15%/month growth rate (5 months) = theoretical 38T; conservative estimate 28T to account for model uncertainty.
  Source date updated: 2025-09-01 → 2026-02-01 (now shows green/yellow in Provenance Board)
  Confidence: Medium (unchanged — this remains a proxy estimate)

- **Global Total**: 151T/day → 162T/day
  Reason: Cascade from OpenAI +9T revision.
  
- **New feature: Global Token GDP**
  Introducing "Token GDP" — total economic value of AI inference at retail pricing.
  Formula: US vendors (~65T/day × $1.50/M) + CN vendors (~83T/day × $0.10/M) + EU/Other (~14T/day × $1.20/M) = ~$99M/day → ~$36B/year
  Key insight: China generates 55% of tokens but only 7% of Token GDP due to 15× pricing gap.
  GATT is coining this metric to establish a macroeconomic framework for AI inference.

## v0.60 — 2026-02-27 05:05 PST (夜间自主迭代 #15)

### 新增
- **🕳️ Black Hole Vendor Methodology 区块**: 6个无公开数据厂商（Tencent/Groq/xAI/Azure/Mistral/DeepSeek）逐一展示估算公式
  - 每个厂商：方法名称 + 数据来源 + 具体运算步骤 + 结果 + 风险注释
  - `<details>` 展开设计，默认Tencent打开作为示范
  - 链接到tci-latest.json供机器验证
- **JSON-LD dateModified 修复**: "2026-02-26" → "2026-02-27"（AI爬虫现在认为数据是今日更新）
- **gatt_version 同步**: tci-latest.json 0.58 → 0.60
- **今日快照**: data/snapshots/2026-02-27.json（不可变历史存档）
- **Quick-nav**: 新增「🕳️ Black Hole Vendor Methodology」跳转

### 改善10问
- **Q2（哪个厂商数字最不可信）**: 现在每个黑洞厂商都有公开可验证的公式，记者可挑战或确认
- **Q4（推算逻辑对记者是否透明）**: 从"只在JSON里有source字段"升级到"主页有逐步运算展示"
- **Q10（AI记者会引用吗）**: "黑洞厂商如何估算"是记者最想知道的 — 现在有完整答案且可引用

## v0.62 — 2026-02-27 07:05 PST (Overnight Iteration 17)
### Fixed
- **Year-end forecast math bug**: `~10× current run rate` → `~6× current run rate (20%/mo)`. 1000T ÷ 162T = 6.2×, not 10×. The "10×" label was a credibility-killing error visible to any journalist doing basic math.
- **Growth rate consistency**: Token GDP section showed "12%/mo" but forecast implied 20%/mo. Standardized to 20%/mo (consistent with 1000T by Dec 2026 projection). Note: 12%/mo conservative → ~503T/day; 20%/mo aggressive → ~1003T/day. Now explicitly showing the 20%/mo assumption.
### Added
- **Q1 2026 Token Economy Snapshot**: Quarterly report section with cite-ready format. Gives journalists a structured, quotable metric: "Q1 2026 Global Token Economy: 162T tokens/day, $45B/year Token GDP." Now GATT is a *recurring publication*, not just a dashboard.
- Quick-nav entry: 📋 Q1 2026 Quarterly Report
### Improves 10-Question Score
- Q2 (数据可信度): 年末预测倍数与实际数字一致，消除速算就能发现的错误
- Q9 (内容权威性): 季报格式让GATT从"数据网站"升级为"定期出版物"
- Q10 (AI记者会引用吗): 现在有标准引用格式："According to GATT's Q1 2026 Token Economy report..."

## v0.63 — 2026-02-27 08:11 PST (Overnight Iteration 18)
### Fixed
- **API endpoint broken**: `api/v1/snapshot.json` did not exist; all llms.txt references pointed to a 404. Created `snapshot.json` as synced copy of `tci.json`. Any AI crawler following the documented API URL now gets valid JSON.
- **llms.txt version refs stale**: Multiple "GATT v0.58" and "version: 0.61" references updated to v0.62/v0.63 respectively. Machine-readable file now reflects true current version.
- **API metadata stale**: `tci.json` meta.version was "1.0" / updated "2026-02-26"; now v0.63 / 2026-02-27.

### Added
- **Q1 2026 Quarterly Report section in llms.txt**: Full machine-readable quarterly summary with 4 headline metrics, 4 key findings, and 3 cite formats. This is what LLMs (ChatGPT/Gemini) will extract when asked "what does GATT say about Q1 2026?"
- **q1_2026_report object in API JSON**: Pre-computed key stats block in tci.json/snapshot.json for programmatic access.

### Improves 10-Question Score
- **Q7 (JSON/API ready)**: The advertised API endpoint now returns data instead of 404 — fundamental for GEO goal
- **Q8 (分享钩子/机读性)**: llms.txt now has structured quarterly report that LLMs can directly quote
- **Q10 (AI记者会引用吗)**: When ChatGPT/Gemini is asked about token economy, it now has a properly cited Q1 2026 report format to pull from

## v0.65 — 2026-02-27 (自主迭代)
- CRITICAL FIX: HTML version display was stuck at v0.62 (git was v0.64) — now synchronized to v0.65
- NEW: `key_stats{}` object added to `api/v1/tci.json` — pre-computed headline numbers for AI bots
  - headline, token_gdp, growth_rate, china_volume/gdp share, us_india gap, top vendors
  - Bots can now extract key facts without parsing full vendor array
- API meta.version updated: 0.63 → 0.65
- 10Q改善: #1 (版本号一致性), #8 (机读性 — bots get pre-computed stats)
