# Appendix C. Bayesian Sensitivity Analysis of the §5.5 Decomposition

This appendix converts the §5.5 quantitative decomposition into a formal Bayesian sensitivity analysis, addressing the methodological concern (raised by Polson in our pre-submission peer review and synthesized by the Harvard editorial review) that the §5.5 decomposition as stated reports point estimates and asserts consistency rather than computing a posterior over the joint factor space.

## C.1 Setup

The decomposition under analysis is:

$$
\frac{G}{L} = \underbrace{\frac{G}{G^{*}}}_{\text{Interp. 1}} \cdot \underbrace{\frac{L^{*}}{L}}_{\text{Interp. 2}} \cdot \underbrace{\frac{G^{*}}{L^{*}}}_{\text{Interp. 3}}
$$

with the §5.5 central estimates and ranges (after the v1.0 per-factor tightening):

| Factor | Central | Low | High |
|---|---:|---:|---:|
| Interp. 1: $G/G^{*}$ | 1.12 | 1.05 | 1.20 |
| Interp. 2: $L^{*}/L$ | 3.0 | 2.0 | 4.0 |
| Interp. 3: $G^{*}/L^{*}$ | 1.4 | 1.25 | 1.65 |

The observable is $G/L = 459.7 / 225 \approx 2.04$.

## C.2 Prior specification

We specify a triangular prior on each factor anchored at the central value with bounds at the stated low and high. Triangular priors are appropriate for this setting because (a) the central values reflect our best estimate, (b) the bounds are interpretable (not just "wide" or "narrow"), and (c) the triangular distribution does not assume the symmetry or unboundedness that a Normal prior would impose.

Formally:
- $G/G^{*} \sim \text{Triangular}(1.05, 1.12, 1.20)$
- $L^{*}/L \sim \text{Triangular}(2.0, 3.0, 4.0)$
- $G^{*}/L^{*} \sim \text{Triangular}(1.25, 1.4, 1.65)$

**Modeling overlap between Interpretations 2 and 3.** The §5.5.5 discussion notes that Interpretation 2 (ASIC efficiency factor) and Interpretation 3 (compute-reuse mechanism) partially overlap because both exploit workload-pattern predictability. We model this overlap by introducing positive correlation $\rho = 0.4$ between the standardized values of $L^{*}/L$ and $G^{*}/L^{*}$ in the joint distribution. This correlation has two interpretations: (a) hardware-software co-design (ASIC efficiency depends on the workload-pattern predictability that also drives cache hits), or (b) shared underlying technology (better speculative decoding algorithms simultaneously improve both the ceiling-recalibration multiplier and the compute-reuse fraction). The choice of $\rho = 0.4$ is editorial; sensitivity to $\rho \in [0.2, 0.6]$ is tested below.

## C.3 Monte Carlo procedure

We draw $N = 10{,}000$ samples from the joint prior:

```
for i in 1 to N:
    interp1[i] = sample from Triangular(1.05, 1.12, 1.20)
    
    # Correlated draws for Interp. 2 and 3
    z1, z2 = draw two iid standard normals
    z2_corr = rho * z1 + sqrt(1 - rho^2) * z2  # rho=0.4
    
    interp2[i] = inverse_triangular_cdf(Phi(z1), 2.0, 3.0, 4.0)
    interp3[i] = inverse_triangular_cdf(Phi(z2_corr), 1.25, 1.4, 1.65)
    
    # Combined effect, with overlap modeled via correlation
    # Note: the overlap between Interp. 2 and Interp. 3 is captured by
    # the correlation in the standardized space, NOT by the
    # /4 ad-hoc correction removed from the v1.0 paper.
    G_over_L[i] = interp1[i] * interp2[i] * interp3[i]
```

This procedure replaces the v0.92 §5.5.5 ad-hoc /4 overlap correction with an explicit correlation model in the prior.

## C.4 Posterior over $G/L$

Running 10,000 MC draws under $\rho = 0.4$:

| Statistic | Value |
|---|---:|
| Mean of posterior $G/L$ | 4.85 |
| Median of posterior $G/L$ | 4.72 |
| 10th percentile | 3.30 |
| 25th percentile | 3.95 |
| 50th percentile | 4.72 |
| 75th percentile | 5.55 |
| 90th percentile | 6.50 |
| Observed $G/L$ | 2.04 |

**Result.** The observed 2.04 lies *outside* the central 80% credibility interval of the posterior — specifically, well below the 10th percentile of 3.30. This is the signal that the decomposition as stated is **insufficiently constrained by overlap**. Even under a correlation of 0.4 between Interpretations 2 and 3, the joint product overstates the implied gap by approximately 2× — which is precisely the tension that the v0.92 ad-hoc /4 correction was attempting (incorrectly) to repair.

## C.5 Re-calibrating the overlap correlation

The honest interpretation of §C.4 is that the decomposition's three factors must overlap *more* than $\rho = 0.4$ implies, *or* the per-factor central values must be lower, *or* both. We test the sensitivity by varying $\rho$ and reporting the $\rho$ at which the posterior median of $G/L$ matches the observed 2.04:

| Correlation $\rho$ | Posterior median $G/L$ | Posterior 10-90% interval |
|---:|---:|---:|
| 0.0 (independent) | 4.71 | [3.42, 6.42] |
| 0.4 | 4.72 | [3.30, 6.50] |
| 0.7 | 4.69 | [3.04, 6.83] |
| 1.0 (perfectly correlated) | 4.65 | [2.95, 7.04] |

Even under perfect positive correlation between Interpretations 2 and 3, the posterior median remains around 4.65 — far above the observed 2.04. **Correlation alone cannot reconcile the decomposition with the observable; the per-factor central values must shrink.**

## C.6 Implication for §5.5

The Appendix C analysis demonstrates that the §5.5 decomposition, as stated with Sokolov-tightened factor ranges (1.05-1.20, 2.0-4.0, 1.25-1.65), is **inconsistent with the observed 2.04× discrepancy under any plausible correlation structure**. The decomposition as a whole overstates the implied gap by approximately 2.3× (4.72 / 2.04).

This is informative, not falsifying. There are three possible resolutions:

**Resolution 1: Per-factor central values are higher than stated.** If the actual Interp. 2 central is 1.5× rather than 3.0×, and Interp. 3 central is 1.2× rather than 1.4×, the product 1.12 × 1.5 × 1.2 = 2.02 matches the observable. This would require accepting that the inference-stack efficiency multiplier is much smaller than §5.3 argues, which contradicts our engineering analysis. We do not endorse this resolution.

**Resolution 2: A fourth factor is missing from the decomposition.** The §5.5 decomposition may be incomplete. A natural candidate: the *empirical-vs-theoretical-throughput* gap — actual hardware utilization is far below theoretical peak. If 2026 inference deployments run at 30-50% of theoretical peak (a plausible figure given memory-bandwidth bottlenecks, scheduler inefficiencies, and load variability), an additional 0.3-0.5× factor would close the gap. We will explore this in v1.1.

**Resolution 3: The correlation structure should be modeled differently.** Rather than positive correlation between Interp. 2 and 3, the factors may exhibit a *substitution* relationship: when one factor is high (e.g., aggressive ASIC deployment), the other is correspondingly low (e.g., less reliance on cache-hit reuse because the ASIC handles fresh-compute efficiently). Negative correlation would shrink the posterior central tendency. We test this:

| Correlation $\rho$ | Posterior median $G/L$ |
|---:|---:|
| -0.5 (substitution) | 4.74 |
| -0.8 (strong substitution) | 4.78 |

Negative correlation actually *raises* the central posterior slightly. Substitution does not resolve the gap either.

## C.7 Honest conclusion and pre-registered prediction

The §5.5 decomposition is inconsistent with the observed 2.04× discrepancy under the per-factor ranges stated. This means either the per-factor central values are systematically biased upward (Resolution 1, which we reject on engineering grounds), or the decomposition is missing a fourth factor (Resolution 2, which we identify as theoretical-vs-empirical-utilization gap and quantify below), or both.

We report this honestly in the v1.0 paper: §5.5 is a *partial* decomposition that captures three of the relevant mechanisms but probably not all of them. The 2.04× observation is consistent with the partial decomposition once a 0.3-0.5× theoretical-vs-empirical-utilization factor is included; it is inconsistent with the partial decomposition as standalone.

### C.7.1 Pre-registered numerical prediction

To convert this finding from a soft "v1.1 will explore" into a falsifiable scientific claim, we commit to a specific numerical prediction in advance of empirical measurement:

> **Prediction.** When third-party benchmarking studies or vendor disclosures report aggregate hardware-utilization figures for representative 2026-2027 production inference deployments (H100/H200/TPU 8th-gen clusters serving frontier-model workloads), the volume-weighted average will satisfy $\eta \in [0.30, 0.50]$, with central expectation $\eta \approx 0.40$.

The four-factor model — adding $\eta$ to the §5.5.5 decomposition — yields:

$$
\frac{G}{L} = \underbrace{\frac{G}{G^{*}}}_{\approx 1.12} \cdot \underbrace{\frac{L^{*}}{L}}_{\approx 3.0} \cdot \underbrace{\frac{G^{*}}{L^{*}}}_{\approx 1.4} \cdot \underbrace{\eta}_{\approx 0.4} \approx 1.88
$$

against the observed $G/L = 2.04$. The 8% remaining residual sits well within the joint credibility band. This is *not* curve-fitting — $\eta \approx 0.4$ is the value implied by published 2024-2025 H100 utilization studies (Patel SemiAnalysis [22]; Epoch AI [18]) for memory-bandwidth-bound inference workloads, applied here as a forward extrapolation rather than a free parameter.

**Falsification rule:**

- **Confirmation** ($\eta \in [0.30, 0.50]$): the four-factor model is consistent with both empirical observation and engineering priors. Joint posterior of $G/L$ centers near 1.88-2.20, encompassing 2.04.
- **Falsification at the upper end** ($\eta > 0.70$): production hardware runs close to theoretical peak. The §5.5 per-factor central values overstate efficiency gains. Either Interpretation 2 ($L^{*}/L = 3.0$) is too aggressive or Interpretation 3 ($G^{*}/L^{*} = 1.4$) is too aggressive. The decomposition must be re-derived with the per-factor centrals revised downward.
- **Falsification at the lower end** ($\eta < 0.20$): production hardware is so under-utilized that capacity is software-throttled, not hardware-bounded. The Litowitz-Polson-Sokolov physical ceiling has implicit assumptions about scheduler/utilization efficiency that need to be made explicit. The framework requires an additional utilization parameter rather than treating utilization as part of the calibration.

The prediction is registered here, in v1.0, before any measurement. The author commits to publishing a v1.x revision within six months of the first credible empirical $\eta$ measurement, either confirming or retracting the prediction.

### C.7.2 Significance for the §5.5 program

The v0.92 manuscript reported "consistent with the observable" without sensitivity analysis. The v1.0 manuscript reports the sensitivity analysis, identifies the missing fourth factor, and pre-registers a specific numerical prediction with explicit falsification thresholds. The progression — from consistency assertion to identified-gap analysis to pre-registered prediction — is the appropriate scientific path for a hypothesis that cannot yet be uniquely identified from a single observable.

**The §5.5 decomposition is necessary but not sufficient. The fourth factor's central value is now an empirical question with a stated answer; the next study to measure $\eta$ in production deployments will either confirm or refute this paper's central reconciliation hypothesis.**

## C.8 Reproducibility

The Monte Carlo simulation code is deposited at the GATT repository:
```
paper/scripts/bayesian_sensitivity.py
```

The script accepts custom factor ranges and correlation values via command-line arguments and reproduces the Tables in §C.4 and §C.5. Posterior draws are released as `paper/data/bayesian_posterior_draws.csv`.
