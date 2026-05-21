# EIF validation tests

This document describes mathematical and numerical checks for efficient influence functions (EIFs).

The purpose is to help a coding agent detect wrong or mismatched EIF formulas.

---

## 1. What needs to be validated?

Given a proposed EIF \(D_\psi(O)\) for a target \(\psi(P)\), validate the following:

1. Mean-zero property:

\[
E\{D_\psi(O)\}=0.
\]

2. Pathwise derivative identity:

\[
\left.
\frac{d}{d\varepsilon}
\psi(P_\varepsilon)
\right|_{\varepsilon=0}
=
E\{D_\psi(O)S(O)\},
\]

for every valid score \(S\).

3. Correct special-case behavior.

4. Correct nuisance-function definitions.

5. Correct positivity requirements.

6. Correct standard-error formula.

7. Regularity of the target.

---

## 2. Mean-zero check

### 2.1 Mathematical check

The EIF must satisfy:

\[
E\{D_\psi(O)\}=0.
\]

For example, for ATE,

\[
D_\psi(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

Check the first residual term:

\[
E\left[
\frac{A}{e(X)}
\{Y-m_1(X)\}
\mid X
\right]
=
\frac{e(X)}{e(X)}
E\{Y-m_1(X)\mid A=1,X\}
=
0.
\]

Similarly,

\[
E\left[
\frac{1-A}{1-e(X)}
\{Y-m_0(X)\}
\mid X
\right]
=0.
\]

Finally,

\[
E\{m_1(X)-m_0(X)-\psi\}=0.
\]

Therefore,

\[
E\{D_\psi(O)\}=0.
\]

---

### 2.2 Code check

If the estimator is constructed as

\[
\hat\psi=\mathbb P_n D(O;\hat\eta),
\]

and

\[
\hat D_{\psi,i}=D(O_i;\hat\eta)-\hat\psi,
\]

then

```python
np.mean(phi_hat)
```

should be zero up to numerical precision.

Example:

```python
import numpy as np

def check_mean_zero(phi_hat, tol=1e-8):
    mean_phi = np.mean(phi_hat)
    return {
        "mean_phi": mean_phi,
        "passes": abs(mean_phi) < tol,
    }
```

If the EIF values are not constructed by subtracting \(\hat\psi\), the empirical mean may not be exactly zero but should be small in simulation under correct nuisance functions.

---

## 3. Standard-error check

The EIF-based standard error is

\[
\widehat{SE}
=
\frac{\operatorname{sd}(\hat D_{\psi,1},\ldots,\hat D_{\psi,n})}{\sqrt n}.
\]

Code:

```python
def eif_standard_error(phi_hat):
    import numpy as np
    n = len(phi_hat)
    return np.std(phi_hat, ddof=1) / np.sqrt(n)
```

Confidence interval:

```python
def normal_ci(psi_hat, se_hat, level=0.95):
    import scipy.stats as st
    alpha = 1.0 - level
    z = st.norm.ppf(1.0 - alpha / 2.0)
    return psi_hat - z * se_hat, psi_hat + z * se_hat
```

If avoiding scipy:

```python
ci_low = psi_hat - 1.96 * se_hat
ci_high = psi_hat + 1.96 * se_hat
```

for an approximate 95% interval.

---

## 4. Finite-difference pathwise derivative check

### 4.1 Principle

For a small \(\varepsilon\), define a tilted distribution:

\[
p_\varepsilon(o)
=
\frac{\exp\{\varepsilon h(o)\}p(o)}
{E_P[\exp\{\varepsilon h(O)\}]}.
\]

The score at \(\varepsilon=0\) is

\[
S_h(O)=h(O)-E\{h(O)\}.
\]

Then the pathwise derivative identity implies:

\[
\frac{\psi(P_\varepsilon)-\psi(P)}{\varepsilon}
\approx
E\{D_\psi(O)S_h(O)\}.
\]

In an empirical approximation:

\[
\frac{\psi(P_\varepsilon)-\psi(P)}{\varepsilon}
\approx
\mathbb P_n\{D_\psi(O_i)[h(O_i)-\bar h]\}.
\]

---

### 4.2 Generic code skeleton

```python
import numpy as np

def exponential_tilting_weights(h, eps):
    h = np.asarray(h)
    raw = np.exp(eps * h)
    return raw / np.mean(raw)

def finite_difference_check(phi, h, psi_eps, psi_0, eps):
    phi = np.asarray(phi)
    h = np.asarray(h)
    h_centered = h - np.mean(h)

    lhs = (psi_eps - psi_0) / eps
    rhs = np.mean(phi * h_centered)

    return {
        "finite_difference": lhs,
        "eif_inner_product": rhs,
        "difference": lhs - rhs,
        "relative_difference": (lhs - rhs) / (abs(lhs) + 1e-12),
    }
```

---

### 4.3 Important caveat

For simple targets such as \(E(Y)\), \(\psi(P_\varepsilon)\) is easy to compute by weighted averages.

For targets involving nuisance functions, such as ATE, \(\psi(P_\varepsilon)\) must be recomputed under the tilted distribution. This usually requires weighted nuisance regressions. If the target is complex, finite-difference validation may be approximate.

---

## 5. Special-case reduction tests

The agent should check whether a complex EIF reduces to a known simple EIF in special cases.

---

### 5.1 Missing-data mean with no missingness

General MAR EIF:

\[
D_\psi(O)
=
\frac{R}{\pi(X)}\{Y-m(X)\}
+
m(X)-\psi.
\]

If \(R=1\) always and \(\pi(X)=1\), then

\[
D_\psi(O)
=
Y-m(X)+m(X)-\psi
=
Y-\psi.
\]

This must reduce to the full-data mean EIF.

---

### 5.2 ATE with randomized treatment independent of \(X\)

ATE EIF:

\[
D_\psi(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

If treatment is completely randomized with \(e(X)=p\), the formula becomes

\[
D_\psi(O)
=
\frac{A}{p}\{Y-m_1(X)\}
-
\frac{1-A}{1-p}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

If there are no covariates, then \(m_a(X)=\mu_a\), so

\[
D_\psi(O)
=
\frac{A}{p}(Y-\mu_1)
-
\frac{1-A}{1-p}(Y-\mu_0)
+
\mu_1-\mu_0-\psi.
\]

Since \(\psi=\mu_1-\mu_0\), the last two terms cancel.

---

### 5.3 Ratio estimator

If

\[
\psi=\frac{E(Y)}{E(Z)},
\]

then the EIF is

\[
D_\psi(O)=\frac{Y-\psi Z}{E(Z)}.
\]

Check that

\[
E\{D_\psi(O)\}=0.
\]

---

## 6. Orthogonality check

Many EIF-based estimators have Neyman orthogonality with respect to nuisance functions.

Suppose the pseudo-outcome is

\[
D(O;\eta).
\]

At the true nuisance \(\eta_0\),

\[
\left.
\frac{\partial}{\partial t}
E\{D(O;\eta_t)\}
\right|_{t=0}
=
0
\]

for regular nuisance paths \(\eta_t\).

This property explains why second-order nuisance errors are often sufficient for asymptotic normality.

---

### 6.1 Numerical perturbation check

For ATE, perturb nuisance estimates around their true values:

```python
import numpy as np

def perturb(arr, scale, rng):
    return arr + scale * rng.normal(size=len(arr))
```

Evaluate the bias of the pseudo-outcome for different perturbation sizes \(t\). If the estimator is orthogonal, the bias should behave approximately like \(O(t^2)\) near \(t=0\), not \(O(t)\).

This check is easiest in simulation, where true nuisance functions are known.

---

## 7. Positivity diagnostics

EIFs with inverse probabilities require positivity.

Examples:

\[
\frac{1}{e(X)},\quad
\frac{1}{1-e(X)},\quad
\frac{1}{\pi(X)},\quad
\frac{1}{g_t(H_t)}.
\]

The agent should report:

```python
def probability_diagnostics(p_hat):
    import numpy as np
    p_hat = np.asarray(p_hat)
    return {
        "min": float(np.min(p_hat)),
        "max": float(np.max(p_hat)),
        "p01": float(np.quantile(p_hat, 0.01)),
        "p05": float(np.quantile(p_hat, 0.05)),
        "p50": float(np.quantile(p_hat, 0.50)),
        "p95": float(np.quantile(p_hat, 0.95)),
        "p99": float(np.quantile(p_hat, 0.99)),
    }
```

The agent should warn if estimated probabilities are close to 0 or 1.

---

## 8. Cross-fitting validation

If using flexible nuisance estimators, the agent should use out-of-fold predictions.

### 8.1 Check for leakage

The nuisance prediction for observation \(i\) should be made by a model that was not trained on observation \(i\).

The agent should document:

- Number of folds
- Learners used for each nuisance function
- Whether predictions are out-of-fold
- Whether hyperparameter tuning was nested or done carefully

---

### 8.2 Empirical mean of EIF after cross-fitting

After cross-fitting:

\[
\hat\psi=\mathbb P_n D(O_i;\hat\eta_{-k(i)}),
\]

\[
\hat D_{\psi,i}=D(O_i;\hat\eta_{-k(i)})-\hat\psi.
\]

Then

```python
np.mean(phi_hat)
```

should be nearly zero by construction.

---

## 9. Nonregular target checks

The agent should explicitly flag targets that may not have a standard root-\(n\) EIF in a fully nonparametric model.

Examples:

### 9.1 Density at a point

\[
p_Y(y_0).
\]

Usually nonregular without smoothing.

Regularized alternative:

\[
\psi_h=E\{K_h(Y-y_0)\}.
\]

EIF for fixed \(h\):

\[
D_{\psi_h}(O)=K_h(Y-y_0)-\psi_h.
\]

---

### 9.2 Pointwise CATE

\[
\tau(x)=E\{Y(1)-Y(0)\mid X=x\}.
\]

For continuous \(X\), this is generally nonregular.

Regular alternative:

\[
E\{Y(1)-Y(0)\mid X\in\mathcal G\},
\]

where \(\mathcal G\) is a fixed subgroup with positive probability.

---

### 9.3 Max or argmax targets

\[
\max_x m(x),
\]

\[
\arg\max_x m(x).
\]

These are generally nonregular without additional margin, uniqueness, and smoothness conditions.

---

## 10. Validation checklist

Before accepting an EIF formula, verify:

- [ ] The target is pathwise differentiable.
- [ ] The observed-data functional is correct.
- [ ] The nuisance functions are correctly defined.
- [ ] Positivity assumptions are explicit.
- [ ] The EIF is mean-zero.
- [ ] The EIF satisfies the pathwise derivative identity.
- [ ] The EIF reduces to known simpler cases.
- [ ] Ratio and transformation rules are correctly applied.
- [ ] The estimator solves the empirical EIF equation when appropriate.
- [ ] The standard error is based on empirical EIF variance.
- [ ] Cross-fitting is used for flexible nuisance estimation.
- [ ] The target is not nonregular, or nonregularity is explicitly handled.
