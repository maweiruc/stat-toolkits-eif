# EIF target triage guide

This guide is the first-pass routing system for EIF problems. Its purpose is to decide what kind of derivation is needed before doing algebra.

The agent should use this guide after normalizing a LaTeX/prose problem and before using the formula registry.

---

## 1. Triage output

Every EIF task should receive a triage label:

```text
Target class:
...

Derivation route:
direct / delta method / observed-data coarsening / causal g-formula /
longitudinal sequential / projection / nonregular / clarification needed

Regularity status:
regular / likely regular with conditions / nonregular / unknown

Registry use:
exact match / comparison only / not applicable
```

---

## 2. Routing table

```text
Target shape                         | Route                         | Main risk
-------------------------------------|-------------------------------|-------------------------------
E[h(O)]                              | Direct centering              | h not integrable
h(theta), theta smooth               | Delta method                  | wrong gradient
alpha / beta                         | Ratio delta method            | beta near zero
F(t)=P(Y<=t)                         | Direct centering              | t data-adaptive
q_tau                                | Invert CDF IF                 | f(q_tau)=0 or discrete Y
E[Y(a)]                              | Causal mean / AIPW            | missing identification
E[Y(1)-Y(0)]                         | Difference of two means       | ATE/ATT confusion
E[Y(1)-Y(0)|A=1]                     | ATT-specific derivation       | using ATE EIF
E[Y(a)|G=1] fixed subgroup           | Ratio/subgroup route          | P(G=1)=0
E[Y(a)|X=x] continuous X             | Nonregular                    | point conditioning
E[Y] with missing outcome            | Observed-data coarsening      | MAR/positivity omitted
Survival under censoring             | Censoring model first         | wrong filtration/model
E[Y^d] fixed longitudinal regime     | Sequential g-formula          | wrong histories/weights
Stochastic intervention              | Density-ratio route           | intervention support
Modified treatment policy            | Transformation-specific route | wrong Jacobian/support
Natural direct/indirect effect       | Mediation-specific route      | mediator density components
Wald/LATE ratio                      | Ratio of adjusted contrasts   | weak denominator
Population regression coefficient    | M-estimation route            | wrong estimating equation
Optimal rule or argmax               | Hard/nonregular route         | nonunique or nonsmooth target
Restricted semiparametric model      | Projection route              | full IF mislabeled EIF
```

---

## 3. Primitive routes

### 3.1 Direct centering

If

\[
\psi(P)=E_P\{h(O)\},
\]

then the nonparametric EIF is

\[
D_\psi(O)=h(O)-\psi.
\]

Use only if \(h\) is fixed and does not contain unknown nuisance functions that depend on \(P\).

### 3.2 Delta method

If

\[
\psi=h(\theta),\qquad \theta=(\theta_1,\ldots,\theta_k),
\]

first derive \(D_{\theta_j}\), then use

\[
D_\psi=\nabla h(\theta)^\top D_\theta.
\]

This route covers ratios, logs, odds, correlations, and quantiles after deriving the CDF IF.

### 3.3 Conditional-mean route

If the target involves

\[
m(x)=E(Y\mid X=x),
\]

ask whether the target averages \(m(X)\) over a positive-probability distribution or evaluates it at a point.

Regular examples:

\[
E\{m(X)\},\qquad E\{m(X)\mid G=1\},\quad P(G=1)>0.
\]

Potentially nonregular examples:

\[
m(x_0),\qquad E\{Y(a)\mid X=x_0\}
\]

when \(X\) is continuous and no smoothing or model restriction is supplied.

### 3.4 Coarsening route

If the full-data target involves variables not always observed, identify:

- full data
- observed data
- coarsening variable
- coarsening mechanism
- independence/coarsening-at-random assumptions
- positivity

Then derive the observed-data IF by adding inverse-probability residual corrections and checking the exact coarsening model.

### 3.5 Causal g-formula route

For causal targets, first write:

```text
Scientific target:
...

Identification assumptions:
consistency / exchangeability / positivity / SUTVA or interference assumptions

Observed-data functional:
...
```

Only then derive the EIF for the observed-data functional.

### 3.6 M-estimation route

If \(\beta\) is defined by

\[
E\{\varphi(O;\beta)\}=0,
\]

and

\[
A=E\left[\frac{\partial}{\partial\beta^\top}\varphi(O;\beta)\right],
\]

then

\[
D_\beta(O)=-A^{-1}\varphi(O;\beta).
\]

Use this for population OLS, working GLMs, quantile regression coefficients, and other estimating-equation parameters.

### 3.7 Projection route

If the model is restricted, derive or retrieve the full nonparametric gradient only as a starting point. Then project onto the restricted model tangent space. See:

```text
theory/eif_projection_guide.md
```

---

## 4. Red flags requiring hard mode

Enter hard mode immediately if the target includes:

- \(X=x\) for continuous \(X\)
- \(p(y_0)\), \(f(y_0)\), or a density at a point
- \(q_\tau\) with discrete outcomes or \(f(q_\tau)=0\)
- \(\max\), \(\arg\max\), selected thresholds, or learned rules
- nuisance-dependent weights or interventions
- continuous treatment densities
- right censoring or competing risks
- mediator densities
- transport/source sampling mechanisms
- known randomization, known censoring, or other model restrictions
- weak ratio denominators

Hard mode does not mean the target is impossible. It means formula lookup is unsafe.

---

## 5. Registry use after triage

The registry can be used directly only if all of the following match:

- observed data
- target
- model
- identification assumptions
- nuisance definitions
- support and positivity conditions
- regularity status

If one of these differs, use the registry only as a comparison check.

