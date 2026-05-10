"""
Population-weighted Gini coefficient and Lorenz curve for AI token consumption,
across the 12 countries broken out in the GATT v1.0 dataset.

Reproduces the §4.4.1 distributional summary in the paper.

Usage:
    python paper/scripts/token_gini.py
    python paper/scripts/token_gini.py --plot lorenz.png
"""

import argparse
import json
import sys
from pathlib import Path


def load_per_capita(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    return d["per_capita"]


def gini_population_weighted(per_capita):
    """Population-weighted Gini via trapezoid integration of the Lorenz curve.

    Each entry: {country, tokens_per_person_K, population_M, ...}
    """
    sorted_pc = sorted(per_capita, key=lambda x: x["tokens_per_person_K"])

    total_pop = sum(c["population_M"] for c in sorted_pc)
    total_tok = sum(c["tokens_per_person_K"] * c["population_M"] for c in sorted_pc)

    P = [0.0]  # cumulative population fraction
    L = [0.0]  # cumulative token fraction
    cum_pop = 0.0
    cum_tok = 0.0
    for c in sorted_pc:
        cum_pop += c["population_M"]
        cum_tok += c["tokens_per_person_K"] * c["population_M"]
        P.append(cum_pop / total_pop)
        L.append(cum_tok / total_tok)

    # G = 1 - sum( (P_k - P_{k-1}) * (L_k + L_{k-1}) )
    g = 1.0
    for k in range(1, len(P)):
        g -= (P[k] - P[k - 1]) * (L[k] + L[k - 1])

    return g, P, L, sorted_pc


def percentile_shares(per_capita):
    """Compute share of total tokens held by top 10% / top 1% / bottom 50% of population."""
    expanded = []
    for c in per_capita:
        expanded.extend([c["tokens_per_person_K"]] * c["population_M"])
    expanded.sort()
    n = len(expanded)
    total = sum(expanded)

    top10_idx = int(n * 0.9)
    top1_idx = int(n * 0.99)
    return {
        "top_10_pct_share": sum(expanded[top10_idx:]) / total,
        "top_1_pct_share": sum(expanded[top1_idx:]) / total,
        "bottom_50_pct_share": sum(expanded[: n // 2]) / total,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--data",
        default=str(Path(__file__).resolve().parents[2] / "data" / "tci-latest.json"),
        help="Path to tci-latest.json",
    )
    ap.add_argument("--plot", default=None, help="Optional path to write Lorenz curve PNG")
    args = ap.parse_args()

    pc = load_per_capita(args.data)

    g, P, L, sorted_pc = gini_population_weighted(pc)
    shares = percentile_shares(pc)

    total_pop = sum(c["population_M"] for c in pc)
    total_tok_g = sum(c["tokens_per_person_K"] * c["population_M"] for c in pc) / 1000  # T tokens

    print(f"Population-weighted Gini coefficient (12 countries): {g:.4f}")
    print(f"Top 10% population share of tokens:    {shares['top_10_pct_share']*100:>5.1f}%")
    print(f"Top  1% population share of tokens:    {shares['top_1_pct_share']*100:>5.1f}%")
    print(f"Bottom 50% population share of tokens: {shares['bottom_50_pct_share']*100:>5.2f}%")
    print()
    print(f"Coverage: {total_pop:.0f}M people, {total_tok_g:.1f}T tokens/day reconstructed")
    print()
    print("Lorenz curve points (P, L):")
    for i, c in enumerate(sorted_pc):
        print(
            f"  {c['country']:<18} pp={c['tokens_per_person_K']:>7.2f}K  "
            f"P={P[i+1]*100:>6.2f}%  L={L[i+1]*100:>7.4f}%"
        )

    if args.plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib not available; skipping plot.", file=sys.stderr)
            return
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot([0, 1], [0, 1], "k--", linewidth=0.8, label="perfect equality (Gini=0)")
        ax.plot(P, L, "o-", color="#c0392b", label=f"Token consumption (Gini={g:.3f})")
        ax.fill_between(P, L, P, alpha=0.15, color="#c0392b")
        ax.set_xlabel("Cumulative population fraction")
        ax.set_ylabel("Cumulative token-consumption fraction")
        ax.set_title("Lorenz curve: AI token consumption across 12 countries (May 2026)")
        ax.legend(loc="upper left", fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        plt.tight_layout()
        plt.savefig(args.plot, dpi=150)
        print(f"Lorenz curve written to {args.plot}")


if __name__ == "__main__":
    main()
