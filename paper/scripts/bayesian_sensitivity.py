"""
Bayesian sensitivity analysis for the §5.5 GATT decomposition.

Reproduces Appendix C results:
- Posterior over G/L = (G/G*) · (L*/L) · (G*/L*)
- Triangular priors with central values from §5.5
- Correlation rho between Interp. 2 and Interp. 3 factors

Usage:
    python paper/scripts/bayesian_sensitivity.py [--rho 0.4] [--n 10000]

Outputs:
- Console: percentile table
- paper/data/bayesian_posterior_draws.csv (if --save flag set)
"""

import argparse
import math
import random


def sample_triangular(low: float, mode: float, high: float) -> float:
    """Triangular distribution sample. Python's random.triangular API uses (low, high, mode)."""
    return random.triangular(low, high, mode)


def sample_correlated_normals(rho: float):
    """Two correlated standard normals via Cholesky."""
    z1 = random.gauss(0, 1)
    z2 = random.gauss(0, 1)
    z2_corr = rho * z1 + math.sqrt(1 - rho * rho) * z2
    return z1, z2_corr


def normal_cdf(z: float) -> float:
    """Standard normal CDF via erf."""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def inverse_triangular(p: float, low: float, mode: float, high: float) -> float:
    """Inverse triangular CDF — maps uniform p into triangular sample."""
    f_mode = (mode - low) / (high - low)
    if p < f_mode:
        return low + math.sqrt(p * (high - low) * (mode - low))
    return high - math.sqrt((1 - p) * (high - low) * (high - mode))


def percentile(sorted_vals, p: float) -> float:
    """Linear-interpolated percentile, p in [0, 1]."""
    n = len(sorted_vals)
    if n == 0:
        return float("nan")
    idx_f = p * (n - 1)
    idx_lo = int(idx_f)
    idx_hi = min(idx_lo + 1, n - 1)
    frac = idx_f - idx_lo
    return sorted_vals[idx_lo] * (1 - frac) + sorted_vals[idx_hi] * frac


def run_simulation(rho: float, n: int, seed: int = 42):
    random.seed(seed)
    samples = []
    for _ in range(n):
        # Independent: Interp. 1 factor (GATT overestimation)
        i1 = sample_triangular(1.05, 1.12, 1.20)

        # Correlated: Interp. 2 (ceiling recalibration) and Interp. 3 (compute reuse)
        z1, z2 = sample_correlated_normals(rho)
        u1 = normal_cdf(z1)
        u2 = normal_cdf(z2)
        i2 = inverse_triangular(u1, 2.0, 3.0, 4.0)
        i3 = inverse_triangular(u2, 1.25, 1.4, 1.65)

        samples.append(i1 * i2 * i3)
    samples.sort()
    return samples


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rho", type=float, default=0.4)
    parser.add_argument("--n", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    samples = run_simulation(args.rho, args.n, args.seed)

    print(f"Bayesian sensitivity analysis — Appendix C")
    print(f"N = {args.n}, rho = {args.rho}, seed = {args.seed}")
    print()
    print(f"{'Statistic':<15} {'Value':>8}")
    print(f"{'-' * 25}")
    print(f"{'Mean':<15} {sum(samples) / len(samples):>8.3f}")
    print(f"{'10th pct':<15} {percentile(samples, 0.10):>8.3f}")
    print(f"{'25th pct':<15} {percentile(samples, 0.25):>8.3f}")
    print(f"{'50th pct':<15} {percentile(samples, 0.50):>8.3f}")
    print(f"{'75th pct':<15} {percentile(samples, 0.75):>8.3f}")
    print(f"{'90th pct':<15} {percentile(samples, 0.90):>8.3f}")
    print(f"{'Observed':<15} {2.04:>8.3f}")
    print()
    print(f"Observed 2.04 falls at percentile: ", end="")
    rank = sum(1 for s in samples if s < 2.04)
    print(f"{100 * rank / len(samples):.1f}%")


if __name__ == "__main__":
    main()
