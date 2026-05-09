#!/usr/bin/env python3
"""
build_tex.py — Convert paper/*.md to a single arXiv-ready main.tex.

Usage: python paper/build_tex.py
Output: paper/main.tex (alongside references.bib)
"""

import re
from pathlib import Path

PAPER_DIR = Path(__file__).parent
OUT = PAPER_DIR / "main.tex"

# Section files in order
SECTIONS = [
    ("abstract", "abstract.md"),
    ("intro", "01-introduction.md"),
    ("related", "02-related-work.md"),
    ("method", "03-methodology.md"),
    ("findings", "04-findings.md"),
    ("tension", "05-tension.md"),
    ("discussion", "06-discussion.md"),
    ("conclusion", "07-conclusion.md"),
    ("appA", "appendix-a-vendors.md"),
    ("appB", "appendix-b-token-gdp-example.md"),
    ("appC", "appendix-c-bayesian-sensitivity.md"),
]

# Numeric citation [1] → BibTeX key mapping (per references.bib order)
CITE_MAP = {
    "1": "litowitz2026photons",
    "2": "landauer1961irreversibility",
    "3": "shannon1948mathematical",
    "4": "idc2026china",
    "5": "aubakirova2026state",
    "6": "xing2026token",
    "7": "idc2025infrastructure",
    "8": "gartner2025aispending",
    "9": "openai2026next",
    "10": "pichai2026cloudnext",
    "11": "zhuang2025beyond",
    "12": "inference2026bottleneck",
    "13": "tokenpowerbench2025",
    "14": "crossplatform2026survey",
    "15": "xiaomi2026mimo",
    "16": "caict2026ai",
    "17": "brynjolfsson2026dashboards",
    "18": "epoch2026inference",
    "19": "crawford2021atlas",
    "20": "hao2025empire",
    "21": "csis2026tokenbill",
    "22": "patel2026semianalysis",
    "23": "brynjolfsson2021productivity",
    "24": "acemoglu2018task",
    "25": "hulten1978growth",
    "26": "bresnahan1995general",
    "27": "david1990dynamo",
}

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}

% --- arXiv-friendly packages ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{textcomp}
\usepackage{amsmath, amssymb, amsfonts}
\usepackage{booktabs}
\usepackage{array}
\usepackage{longtable}
\usepackage[hidelinks,colorlinks=false]{hyperref}
\usepackage{geometry}
\geometry{margin=1in}
\usepackage{authblk}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage[round]{natbib}
\bibliographystyle{plainnat}

\title{Measuring the Token Economy: An Empirical Companion to Physical-Ceiling Models of Global AI Inference}
\author[1]{Frank Gao}
\affil[1]{Independent researcher \\ \texttt{goghxiang@gmail.com}}
\date{May 2026}

\begin{document}

\maketitle
"""

ABSTRACT_WRAPPER_OPEN = r"""\begin{abstract}
"""
ABSTRACT_WRAPPER_CLOSE = r"""
\end{abstract}

\textbf{Keywords:} Token Economy, AI inference, large language models, global measurement, ChatGPT, Gemini, Doubao, Anthropic, Token GDP, Photons-Tokens, physical ceiling, Jevons paradox.

"""

POSTAMBLE = r"""

\bibliography{references}

\end{document}
"""


def escape_latex(text: str) -> str:
    """Escape LaTeX special characters in body text. Order matters."""
    # Backslash first (must precede other escapes)
    text = text.replace("\\", r"\textbackslash{}")
    # Then ampersand, percent, dollar, hash, underscore, caret, tilde, braces
    text = text.replace("&", r"\&")
    text = text.replace("%", r"\%")
    text = text.replace("$", r"\$")
    text = text.replace("#", r"\#")
    text = text.replace("_", r"\_")
    text = text.replace("{", r"\{").replace("}", r"\}")
    text = text.replace("^", r"\textasciicircum{}")
    text = text.replace("~", r"\textasciitilde{}")
    # Restore textbackslash that got mangled
    text = text.replace(r"\textbackslash\{\}", r"\textbackslash{}")
    return text


def escape_body_specials(text: str) -> str:
    """Escape LaTeX-fatal special characters in body text. Conservative: only escape what definitely breaks compilation or mis-renders."""
    # % is a comment marker — must escape
    text = re.sub(r"(?<!\\)%", r"\%", text)
    # & breaks tabular outside table; conservative escape
    text = re.sub(r"(?<!\\)&", r"\&", text)
    # Currency $: $ followed by a digit/letter character (e.g., $758, $1.5B, $44B)
    # is currency, not math mode. Escape to \$ to render the dollar sign correctly.
    # Do NOT touch $$ (display math) or $x...$ where x starts with letter+space (math var).
    text = re.sub(r"(?<!\\)(?<!\$)\$(?=\d)", r"\\$", text)
    return text


def replace_unicode(text: str) -> str:
    """Replace problematic Unicode characters with LaTeX-safe equivalents.

    Strategy: pdflatex with utf8 inputenc handles most basic Unicode (×, –, —, ·).
    But superscript Unicode (¹, ², ⁷) and CJK characters need special handling.
    """
    # Unicode superscripts → LaTeX math-mode superscripts
    # Common: 6.5 × 10¹⁷ → 6.5 × $10^{17}$
    superscripts = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}
    # Match runs of superscripts and convert
    def sup_repl(m):
        digits = "".join(superscripts[c] for c in m.group(0))
        return "$^{" + digits + "}$"
    text = re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+", sup_repl, text)

    # Strip CJK characters (Chinese 中信国通院 etc.) — redundant since English equivalents always present
    # CJK Unified Ideographs: U+4E00 to U+9FFF
    text = re.sub(r"[一-鿿]+\s*", "", text)
    # Strip orphaned CJK punctuation that may remain
    text = re.sub(r"[（）]", "", text)
    # Clean up doubled spaces / spaces before punctuation
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    text = re.sub(r"  +", " ", text)

    return text


def convert_inline(text: str) -> str:
    """Convert inline markdown to LaTeX."""

    # PROTECT inline math $...$ from subsequent conversions (italic regex would mangle $G^{*}$)
    # Replace each $...$ segment with a placeholder, restore at the end.
    # IMPORTANT: only protect math-shaped content (starts with letter or backslash),
    # NOT currency ($758 = digit start = currency, must NOT be protected).
    math_segments = []
    def math_protect(m):
        math_segments.append(m.group(0))
        return f"\x00MATH{len(math_segments)-1}\x00"
    # Math content: $ followed by letter or backslash, ending with another $, single-line only
    text = re.sub(r"\$[a-zA-Z\\][^\$\n]{0,300}\$", math_protect, text)

    # Convert markdown links [text](url) → \href{url}{text}
    def link_repl(m):
        label = m.group(1)
        url = m.group(2)
        return r"\href{" + url + r"}{" + label + r"}"
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, text)

    # Convert numeric citations [1], [1, 2], [1, 4, 7] → \cite{key1, key2}
    def cite_repl(m):
        nums = [n.strip() for n in m.group(1).split(",")]
        keys = [CITE_MAP.get(n, f"REF{n}") for n in nums]
        return r"\cite{" + ", ".join(keys) + r"}"
    # Match [N] or [N, N, N] only when preceded by word char or whitespace,
    # NOT followed by ( — to avoid matching markdown link syntax
    text = re.sub(r"(?<![\(\w])\[(\d+(?:\s*,\s*\d+)*)\](?!\()", cite_repl, text)

    # Bold **text**
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    # Italic *text* (avoid double-asterisk already handled)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\\emph{\1}", text)

    # Inline code `text` — escape LaTeX-fatal chars inside
    def code_repl(m):
        content = m.group(1)
        content = content.replace("\\", r"\textbackslash{}")
        content = content.replace("_", r"\_")
        content = content.replace("{", r"\{").replace("}", r"\}")
        content = content.replace("^", r"\textasciicircum{}")
        content = content.replace("$", r"\$")
        content = content.replace("&", r"\&")
        content = content.replace("%", r"\%")
        content = content.replace("#", r"\#")
        return r"\texttt{" + content + "}"
    text = re.sub(r"`([^`]+)`", code_repl, text)

    # Em-dash → en/em dash
    text = text.replace(" — ", r" --- ")

    # Escape body specials AFTER all markdown conversions (so we don't mess with \cite{}, \href{}, etc.)
    # We need to escape only LITERAL % and & in non-LaTeX-command contexts
    text = escape_body_specials(text)

    # Replace problematic Unicode (superscripts, CJK) with LaTeX-safe forms
    text = replace_unicode(text)

    # RESTORE protected math segments
    for idx, seg in enumerate(math_segments):
        text = text.replace(f"\x00MATH{idx}\x00", seg)

    return text


def convert_table(lines):
    """Convert a markdown table block (list of lines) → LaTeX longtable."""
    # First line: headers; second line: separator; rest: rows
    rows = [l.strip() for l in lines if l.strip()]
    headers = [h.strip() for h in rows[0].strip("|").split("|")]
    n_cols = len(headers)
    spec = "l" * n_cols
    out = [r"\begin{center}",
           r"\begin{tabular}{" + spec + r"}",
           r"\toprule"]
    out.append(" & ".join(escape_latex(convert_inline(h)) for h in headers) + r" \\")
    out.append(r"\midrule")
    for row in rows[2:]:  # skip separator line
        cells = [c.strip() for c in row.strip("|").split("|")]
        # Pad if needed
        while len(cells) < n_cols:
            cells.append("")
        out.append(" & ".join(convert_inline(c) for c in cells[:n_cols]) + r" \\")
    out.append(r"\bottomrule")
    out.append(r"\end{tabular}")
    out.append(r"\end{center}")
    return out


def convert_block(md: str, is_abstract=False) -> str:
    """Convert a single markdown file's body to LaTeX."""
    lines = md.split("\n")
    out = []
    i = 0
    in_code_block = False  # track ``` fenced code blocks

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code fence detection — wrap fenced blocks in verbatim env
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                out.append(r"\begin{verbatim}")
            else:
                in_code_block = False
                out.append(r"\end{verbatim}")
            i += 1
            continue

        # While inside a code block, emit lines verbatim, no markdown processing
        if in_code_block:
            out.append(line)
            i += 1
            continue

        # Headings
        if stripped.startswith("# "):
            # Top-level heading — usually the section title; skip if abstract
            if is_abstract:
                i += 1
                continue
            heading = stripped[2:].strip()
            heading = re.sub(r"^\d+\.\s*", "", heading)  # strip "1. " prefix
            out.append(r"\section{" + convert_inline(heading) + "}")
            i += 1
            continue
        if stripped.startswith("## "):
            heading = stripped[3:].strip()
            heading = re.sub(r"^\d+\.\d+\s*", "", heading)  # strip "1.1 " prefix
            out.append(r"\subsection{" + convert_inline(heading) + "}")
            i += 1
            continue
        if stripped.startswith("### "):
            heading = stripped[4:].strip()
            out.append(r"\subsubsection{" + convert_inline(heading) + "}")
            i += 1
            continue

        # Tables
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|", lines[i + 1].strip()):
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            out.extend(convert_table(tbl))
            out.append("")
            continue

        # Display math (line that's exactly $$ ... $$)
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4:
            math = stripped[2:-2]
            out.append(r"\begin{equation*}")
            out.append(math)
            out.append(r"\end{equation*}")
            i += 1
            continue

        # Display math block
        if stripped == "$$":
            i += 1
            math_lines = []
            while i < len(lines) and lines[i].strip() != "$$":
                math_lines.append(lines[i])
                i += 1
            i += 1  # skip closing $$
            out.append(r"\begin{equation*}")
            out.extend(math_lines)
            out.append(r"\end{equation*}")
            continue

        # Bullet lists — consolidate
        if stripped.startswith("- ") or stripped.startswith("* "):
            out.append(r"\begin{itemize}")
            while i < len(lines):
                cur_stripped = lines[i].strip()
                if cur_stripped.startswith("- ") or cur_stripped.startswith("* "):
                    item = cur_stripped[2:]
                    out.append(r"  \item " + convert_inline(item))
                    i += 1
                elif lines[i].startswith("  ") and not cur_stripped == "" and not re.match(r"^\d+\.", cur_stripped):
                    # continuation
                    if out and out[-1].startswith(r"  \item"):
                        out[-1] = out[-1] + " " + convert_inline(cur_stripped)
                    i += 1
                elif cur_stripped == "":
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j < len(lines) and (lines[j].strip().startswith("- ") or lines[j].strip().startswith("* ")):
                        i = j
                    else:
                        break
                else:
                    break
            out.append(r"\end{itemize}")
            continue

        # Numbered lists — consolidate consecutive items separated only by blank lines
        if re.match(r"^\d+\.\s+", stripped):
            out.append(r"\begin{enumerate}")
            while i < len(lines):
                cur_stripped = lines[i].strip()
                if re.match(r"^\d+\.\s+", cur_stripped):
                    item = re.sub(r"^\d+\.\s+", "", cur_stripped)
                    out.append(r"  \item " + convert_inline(item))
                    i += 1
                elif lines[i].startswith("   ") and not cur_stripped.startswith("- "):
                    # continuation of previous item
                    if out and out[-1].startswith(r"  \item"):
                        out[-1] = out[-1] + " " + convert_inline(cur_stripped)
                    i += 1
                elif cur_stripped == "":
                    # blank — peek ahead: continue if another numbered item follows
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j < len(lines) and re.match(r"^\d+\.\s+", lines[j].strip()):
                        i = j  # skip blank lines, continue list
                    else:
                        break  # end of list
                else:
                    break
            out.append(r"\end{enumerate}")
            continue

        # Blank line
        if not stripped:
            out.append("")
            i += 1
            continue

        # Regular paragraph
        out.append(convert_inline(line))
        i += 1

    return "\n".join(out)


def main():
    parts = [PREAMBLE]

    # Process abstract specially — wrap in abstract environment
    abstract_path = PAPER_DIR / "abstract.md"
    abstract_md = abstract_path.read_text(encoding="utf-8")
    abstract_tex = convert_block(abstract_md, is_abstract=True)
    parts.append(ABSTRACT_WRAPPER_OPEN)
    parts.append(abstract_tex.strip())
    parts.append(ABSTRACT_WRAPPER_CLOSE)

    # Process all other sections
    for label, fn in SECTIONS[1:]:  # skip abstract (already done)
        path = PAPER_DIR / fn
        if not path.exists():
            continue
        md = path.read_text(encoding="utf-8")

        # Special handling for appendices
        if label == "appA":
            parts.append(r"\appendix")
            parts.append("")

        tex = convert_block(md)
        parts.append(tex)
        parts.append("")

    parts.append(POSTAMBLE)

    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"Total length: {len(OUT.read_text(encoding='utf-8'))} chars")


if __name__ == "__main__":
    main()
