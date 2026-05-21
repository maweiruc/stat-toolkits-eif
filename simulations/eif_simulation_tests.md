# EIF simulation tests

This document provides simulation designs for testing EIF-based estimators.

The goal is to help a coding agent verify:

1. Bias
2. Standard error
3. Confidence interval coverage
4. Mean-zero EIF property
5. Positivity sensitivity
6. Double robustness where applicable

---

## 1. General Monte Carlo protocol

For each simulation:

```text
For b = 1, ..., B:
  1. Generate a dataset of size n.
  2. Estimate nuisance functions.
  3. Construct the EIF-based estimator.
  4. Store:
     - psi_hat
     - se_hat
     - confidence interval
     - mean(phi_hat)
     - nuisance diagnostics
After B repetitions:
  1. Estimate bias.
  2. Estimate Monte Carlo standard deviation.
  3. Average estimated SE.
  4. Estimate CI coverage.
  5. Summarize positivity diagnostics.
```

Suggested metrics:

\[
\operatorname{Bias}
=
\frac{1}{B}\sum_{b=1}^B \hat\psi_b-\psi_0.
\]

\[
\operatorname{MCSD}
=
\sqrt{
\frac{1}{B-1}\sum_{b=1}^B
(\hat\psi_b-\bar{\hat\psi})^2
}.
\]

\[
\operatorname{AvgSE}
=
\frac{1}{B}\sum_{b=1}^B \widehat{SE}_b.
\]

Coverage:

\[
\frac{1}{B}
\sum_{b=1}^B
I\{\psi_0\in CI_b\}.
\]

---

## 2. Simulation 1: Full-data mean

Data-generating process:

\[
Y\sim N(1,4).
\]

Target:

\[
\psi_0=E(Y)=1.
\]

EIF:

\[
D_\psi(Y)=Y-1.
\]

Estimator:

\[
\hat\psi=\bar Y.
\]

Expected behavior:

- Bias close to 0.
- Estimated SE close to \(2/\sqrt n\).
- Coverage close to 95%.

---

## 3. Simulation 2: Variance

Data-generating process:

\[
Y\sim N(1,4).
\]

Target:

\[
\psi_0=\operatorname{Var}(Y)=4.
\]

EIF:

\[
D_\psi(Y)=(Y-\mu)^2-\psi.
\]

Expected behavior:

- Bias of plug-in variance may be small.
- EIF-based SE should use empirical variance of \((Y-\hat\mu)^2-\hat\psi\).

Implementation note:

Use

```python
psi_hat = np.mean((y - np.mean(y))**2)
phi_hat = (y - np.mean(y))**2 - psi_hat
se_hat = np.std(phi_hat, ddof=1) / np.sqrt(n)
```

---

## 4. Simulation 3: Missing-data mean under MAR

Generate:

\[
X\sim N(0,1),
\]

\[
Y=1+X+\epsilon,\qquad \epsilon\sim N(0,1),
\]

\[
R\sim \operatorname{Bernoulli}(\pi(X)),
\]

where

\[
\pi(X)=\operatorname{expit}(0.2+0.5X).
\]

Observed data:

\[
O=(R,RY,X).
\]

Target:

\[
\psi_0=E(Y)=1.
\]

Nuisance functions:

\[
m(X)=E(Y\mid X)=1+X,
\]

\[
\pi(X)=\operatorname{expit}(0.2+0.5X).
\]

EIF:

\[
D_\psi(O)
=
\frac{R}{\pi(X)}\{Y-m(X)\}
+
m(X)-\psi_0.
\]

Expected behavior with true nuisances:

- Bias close to 0.
- Mean EIF close to 0.
- Coverage close to 95%.

Double robustness test:

1. Correct \(m\), wrong \(\pi\): estimate should remain consistent.
2. Wrong \(m\), correct \(\pi\): estimate should remain consistent.
3. Both wrong: estimate generally biased.

---

## 5. Simulation 4: ATE with randomized treatment

Generate:

\[
X\sim N(0,1),
\]

\[
A\sim \operatorname{Bernoulli}(0.5),
\]

\[
Y=1+2A+X+\epsilon,
\qquad \epsilon\sim N(0,1).
\]

Target:

\[
\psi_0=E\{Y(1)-Y(0)\}=2.
\]

Nuisance functions:

\[
e(X)=0.5,
\]

\[
m_1(X)=3+X,
\]

\[
m_0(X)=1+X.
\]

EIF:

\[
D_\psi(O)
=
\frac{A}{0.5}\{Y-m_1(X)\}
-
\frac{1-A}{0.5}\{Y-m_0(X)\}
+
2-\psi_0.
\]

Since \(\psi_0=2\), the last part cancels.

Expected behavior:

- AIPW estimate close to 2.
- Difference-in-means may also be unbiased but less efficient if \(X\) is predictive.
- Covariate adjustment can reduce variance.

---

## 6. Simulation 5: ATE with observational treatment

Generate:

\[
X\sim N(0,1),
\]

\[
e(X)=\operatorname{expit}(0.2+0.8X),
\]

\[
A\sim \operatorname{Bernoulli}(e(X)),
\]

\[
Y=1+2A+X+\epsilon,
\qquad \epsilon\sim N(0,1).
\]

Target:

\[
\psi_0=2.
\]

Nuisance functions:

\[
m_1(X)=3+X,
\]

\[
m_0(X)=1+X,
\]

\[
e(X)=\operatorname{expit}(0.2+0.8X).
\]

Expected behavior:

- Naive difference in means is biased.
- AIPW with correct nuisances is unbiased.
- AIPW with one of \(m_a\) or \(e\) correct remains consistent.
- Severe positivity problems increase variance.

---

## 7. Simulation 6: ATT

Generate:

\[
X\sim N(0,1),
\]

\[
e(X)=\operatorname{expit}(0.2+0.8X),
\]

\[
A\sim \operatorname{Bernoulli}(e(X)),
\]

\[
Y=1+2A+X+\epsilon.
\]

Target:

\[
\psi_0=E\{Y(1)-Y(0)\mid A=1\}=2.
\]

Because the treatment effect is constant.

Nuisance:

\[
m_0(X)=1+X,
\]

\[
e(X)=\operatorname{expit}(0.2+0.8X),
\]

\[
p=P(A=1)=E\{e(X)\}.
\]

EIF:

\[
D_\psi(O)
=
\frac{A}{p}
\{Y-m_0(X)-\psi\}
-
\frac{1-A}{p}
\frac{e(X)}{1-e(X)}
\{Y-m_0(X)\}.
\]

Expected behavior:

- ATT estimator close to 2.
- ATE and ATT are equal only because treatment effect is constant.
- If effect heterogeneity is introduced, ATE and ATT differ.

---

## 8. Simulation 7: Heterogeneous treatment effect

Generate:

\[
X\sim N(0,1),
\]

\[
e(X)=\operatorname{expit}(0.2+0.8X),
\]

\[
A\sim \operatorname{Bernoulli}(e(X)),
\]

\[
Y=1+A(1+X)+X+\epsilon.
\]

Potential outcomes:

\[
Y(0)=1+X+\epsilon,
\]

\[
Y(1)=2+2X+\epsilon.
\]

Treatment effect:

\[
Y(1)-Y(0)=1+X.
\]

ATE:

\[
E(1+X)=1.
\]

ATT:

\[
E(1+X\mid A=1)=1+E(X\mid A=1).
\]

This simulation is useful for checking that ATE and ATT estimators target different estimands.

---

## 9. Simulation 8: Ratio of means

Generate:

\[
Y=2+X+\epsilon_Y,
\]

\[
Z=1+0.5X+\epsilon_Z,
\]

where \(X,\epsilon_Y,\epsilon_Z\) have mean zero and \(E(Z)=1\).

Target:

\[
\psi_0=\frac{E(Y)}{E(Z)}=2.
\]

EIF:

\[
D_\psi(O)=\frac{Y-\psi Z}{E(Z)}.
\]

Expected behavior:

- Estimate \(\hat\psi=\bar Y/\bar Z\).
- EIF-based SE should match Monte Carlo SD.
- If \(E(Z)\) is close to zero, estimator becomes unstable.

---

## 10. Simulation 9: Quantile

Generate:

\[
Y\sim N(0,1).
\]

Target:

\[
q_{0.5}=0.
\]

Density at median:

\[
f(0)=\frac{1}{\sqrt{2\pi}}.
\]

EIF:

\[
D_{q_{0.5}}(O)=
\frac{0.5-I(Y\le 0)}{f(0)}.
\]

Expected asymptotic variance:

\[
\frac{\tau(1-\tau)}{f(q_\tau)^2}.
\]

For \(\tau=0.5\):

\[
\frac{0.25}{f(0)^2}.
\]

Implementation note:

For real data, \(f(q_\tau)\) must be estimated.

---

## 11. Simulation 10: Nonregular warning

Generate:

\[
X\sim N(0,1),
\]

\[
A\sim \operatorname{Bernoulli}(0.5),
\]

\[
Y=1+A(1+X)+X+\epsilon.
\]

Ask the agent for the EIF of:

\[
\tau(0)=E\{Y(1)-Y(0)\mid X=0\}.
\]

Expected answer:

```text
In the fully nonparametric model with continuous X, this is a pointwise conditional target and is generally not root-n pathwise differentiable. A standard EIF is not available without smoothing or modeling restrictions.
```

Acceptable alternative target:

\[
\tau_h(0)
=
\frac{
E\left[K_h(X)\{m_1(X)-m_0(X)\}\right]
}{
E\left[K_h(X)\right]
}.
\]

---

## 12. Python template for Monte Carlo evaluation

```python
import numpy as np

def summarize_mc(estimates, ses, ci_lows, ci_highs, truth):
    estimates = np.asarray(estimates)
    ses = np.asarray(ses)
    ci_lows = np.asarray(ci_lows)
    ci_highs = np.asarray(ci_highs)

    return {
        "truth": truth,
        "mean_estimate": float(np.mean(estimates)),
        "bias": float(np.mean(estimates) - truth),
        "mc_sd": float(np.std(estimates, ddof=1)),
        "avg_se": float(np.mean(ses)),
        "coverage": float(np.mean((ci_lows <= truth) & (truth <= ci_highs))),
    }
```

---

## 13. Recommended simulation settings

For quick checks:

```text
n = 1000
B = 200
```

For more stable Monte Carlo results:

```text
n = 2000
B = 1000
```

For debugging code:

```text
n = 200
B = 20
```

---

## 14. Simulation checklist

For each simulation, report:

- [ ] Data-generating process
- [ ] True target
- [ ] Nuisance functions
- [ ] Estimator
- [ ] Bias
- [ ] Monte Carlo SD
- [ ] Average EIF-based SE
- [ ] Coverage
- [ ] Mean EIF
- [ ] Positivity diagnostics
- [ ] Notes on failures or instability
