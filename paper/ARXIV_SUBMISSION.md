# arXiv Submission Guide

**Manuscript:** *Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference*
**Author:** Frank Gao
**Date:** May 2026

---

## Pre-flight checklist (do before submitting)

- [ ] Re-run `python paper/build_tex.py` to regenerate `main.tex` from latest markdown
- [ ] Re-run `python paper/check_tex.py` — verify 0 unresolved citations, balanced braces, balanced math mode
- [ ] Open `main.tex` in any LaTeX editor (Overleaf preview is easiest) — render once to confirm pdflatex compiles cleanly
- [ ] Spot-check 5 sections render: abstract, intro, Section 5 (the 2× tension), Section 6 (discussion), references list
- [ ] Verify all `\href{...}{...}` URLs resolve (especially the GATT dataset URL: `https://gf691271.github.io/gatt/`)
- [ ] Verify dataset snapshot link is reproducible: `https://github.com/gf691271/gatt/blob/main/data/snapshots/2026-05-09.json`
- [ ] Final manual proof read of abstract + Section 1 (most-read parts)

## arXiv submission form fields

### Title
```
Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference
```

### Author
```
Frank Gao
```

### Abstract (paste verbatim — already 250 words from paper/abstract.md)
```
In May 2026, the Global AI Token Tracker (GATT) measures 459,700 tokens per United States resident per day -- 2.04x the 2028 physical ceiling of 225,000 tokens per person per day projected by Litowitz, Polson, and Sokolov (2026, arXiv:2603.06630) under a 326 TWh AI energy allocation. This paper presents the empirical methodology underlying that measurement and proposes three reconciliation interpretations: (i) GATT may overestimate top vendors via attribution multipliers, (ii) the paper's Landauer/Shannon ceiling is conservative because real 2026 inference uses Mixture-of-Experts architectures, 4-bit quantization, speculative decoding, and dedicated inference ASICs, yielding 5-10x more tokens per Joule than the physics baseline, and (iii) the two metrics measure different units -- GATT measures empirical all-surface output, while the physical-ceiling paper models theoretical capacity assuming fresh compute per token.

GATT is, to our knowledge, the first global, all-sources, daily-updated index of AI token throughput, covering 21 vendors across 12 countries. As of May 9, 2026, GATT measures global daily output at 310 trillion tokens, with China and the United States tied at 50% volume share but the United States capturing 88% of "Token GDP" -- a vendor-volume x blended-pricing metric -- due to a 15x pricing asymmetry between US and Chinese vendors. The US-India per-capita gap stands at 597x, having widened from 448x in five weeks. We document our methodology, contrast it with IDC China Public Cloud MaaS (which independently confirms our top vendor ranking at 49.5% Volcengine market share), and propose Token GDP as a regional-comparable economic-value metric for the emerging Token Economy. All data and code are released under CC BY 4.0 at gf691271.github.io/gatt/.
```

(Note: arXiv abstract field strips most LaTeX. The plain text above replaces × with x and uses ASCII dashes.)

### Categories

- **Primary:** `cs.CY` — Computers and Society
- **Cross-list:** `econ.GN` — General Economics

Justification: cs.CY for the policy / measurement-infrastructure dimension; econ.GN for the Token GDP / market-economic content. Avoid cs.LG (too narrow — this is not a model paper) and cs.AI (too generic).

### Comments field
```
8,000 words, 2 appendices (vendor table, Token GDP worked example with sensitivity bands), 37 references. Open dataset and revision history at https://github.com/gf691271/gatt; live dashboard at https://gf691271.github.io/gatt/. CC BY 4.0.
```

### License
**arXiv.org perpetual, non-exclusive license** + **CC BY 4.0** (matches GATT dataset license).

### Files to upload
- `main.tex` (manuscript)
- `references.bib` (bibliography)
- (Optional) `figures/` directory if any included — currently 0 figures (text-only, table-heavy paper)

### Source format
**LaTeX** (use the `Submit a LaTeX submission` option). arXiv compiles via TeX Live; should work cleanly given preamble uses standard packages.

---

## Endorser request (if needed)

arXiv requires endorsement for first-time authors in cs.* categories. Three endorsement paths:

### Path 1: Existing relationships
If you have a contact at an academic institution who has previously posted to cs.CY or econ.GN, ask them to endorse via the arXiv endorsement system. Send them this paper preprint + a 2-sentence note.

### Path 2: Cold email to paper's existing dialogue partners
The most natural endorsers are researchers GATT directly engages with:

**Best candidates** (in priority order):
1. **Erik Brynjolfsson** (Stanford HAI / Digital Economy Lab) — has posted to cs.CY and econ.GN; predicted GATT in his Dec 2025 forecast. Email: brynjolfsson@stanford.edu (or via Stanford HAI contact form).
2. **Anjney Midha** (a16z; co-author of arXiv:2601.10088) — has posted to arXiv recently in cs.* categories. Email: anjney@a16z.com.
3. **Vadim Sokolov** (GMU; co-author of arXiv:2603.06630, Photons = Tokens) — paper's central dialogue partner. Email: vsokolov@gmu.edu.

**Endorser request email template:**
```
Subject: Endorsement request — empirical token-economy paper engaging with arXiv:2603.06630

Dear [Name],

I'm writing to ask if you would consider endorsing my arXiv submission to cs.CY (with cross-list to econ.GN). My paper, *Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference*, presents an empirical methodology that directly engages with [Photons = Tokens / your AI economic dashboards prediction / etc.].

Key points:
- 21-vendor daily token-throughput index (open data, CC BY 4.0)
- Documents a productive 2.04x discrepancy between empirical GATT measurements and the Litowitz/Polson/Sokolov 2028 physical ceiling, proposing three reconciliation interpretations
- Proposes "Token GDP" as a regional-comparable economic-value metric

The full preprint is attached (PDF). Dataset: https://gf691271.github.io/gatt/

If you'd be willing to endorse (https://arxiv.org/auth/need-endorsement.php?archive=cs&subject_class=CY), please reply with your arXiv user ID and I will request endorsement formally through the system.

Thank you for considering.

Best regards,
Frank Gao
goghxiang@gmail.com
```

### Path 3: Submit to econ.GN first (lower endorsement bar)
econ.GN often has lower endorsement requirements than cs.CY. Consider primary submission to econ.GN with cs.CY cross-list if endorsement is delayed.

---

## Day-of submission timing

**Suggested:** Submit Tuesday-Thursday 14:00-16:00 ET. arXiv mailing list goes out daily 20:00 ET; weekday submissions get same-day attention.

**Avoid:** Friday late afternoon (paper sits over weekend), Monday early (catch-up backlog).

## Post-submission outreach (Day 0 to Day 7)

The 16 outreach targets in `data/tci-latest.json` `outreach_targets` block are designed for execution starting the moment the arXiv DOI is live.

### Day 0 (within 6 hours of arXiv preprint going live)
- Email tier-1 academic: Litowitz/Polson/Sokolov, Brynjolfsson, Xing, Sevilla
- Email tier-1 practitioner: Patel (SemiAnalysis)
- Tweet announcement with arXiv link + key 2× tension framing

### Day 1-2
- X DMs: Karpathy, Anjney Midha, Martin Casado
- Email: Karen Hao (The Atlantic)

### Day 3-7
- Pitch Hard Fork (Roose/Newton), No Priors (Guo/Gil)
- Pitch Stratechery (Ben Thompson)
- China-side: email Wei Liang (CAICT), CSIS authors, CEIBS authors

Each contact has a personalized hook documented in `data/tci-latest.json` outreach_targets block.

---

## Post-arXiv next steps

- Convert to journal format (target: *AI Magazine*, *Big Data & Society*, or SSRN)
- Build the first infographic (price-volume paradox)
- Write Substack/Medium long-form data story based on Section 5
- Register independent domain (tokeneconomy.org candidate)
- Begin Amazon book proposal — differentiated from Karen Hao *Empire of AI* by data-first global-index angle

## Files in this paper/ directory

```
paper/
├── ARXIV_SUBMISSION.md   ← this file
├── README.md             ← project overview
├── outline.md            ← full structure plan
├── build_tex.py          ← Markdown → LaTeX converter
├── check_tex.py          ← LaTeX sanity checker
├── main.tex              ← arXiv-ready manuscript (auto-generated)
├── references.bib        ← BibTeX (37 entries)
├── abstract.md           ← source: abstract
├── 01-introduction.md    ← source: Section 1
├── 02-related-work.md    ← source: Section 2
├── 03-methodology.md     ← source: Section 3
├── 04-findings.md        ← source: Section 4
├── 05-tension.md         ← source: Section 5 (the 2× discrepancy)
├── 06-discussion.md      ← source: Section 6
├── 07-conclusion.md      ← source: Section 7
├── appendix-a-vendors.md ← source: full vendor table
└── appendix-b-token-gdp-example.md  ← source: Token GDP worked example
```

To regenerate `main.tex` after editing any markdown:
```bash
python paper/build_tex.py
```

To verify LaTeX integrity before submission:
```bash
python paper/check_tex.py
```
