# EIF implementation guide

This document explains how to turn an efficient influence function (EIF) into code, estimators, standard errors, and confidence intervals.

The focus is on practical implementation for a coding agent.

---

## 1. General EIF-based estimator

Suppose the EIF can be written as

\[
D_\psi(O;\eta,\psi)
=
D(O;\eta)-\psi,
\]

where \(\eta\) denotes nuisance functions.

Then the EIF-based estimator is

\[
\hat\psi
=
\mathbb P_n D(O;\hat\eta).
\]

The estimated EIF values are

\[
\hat D_{\psi,i}
=
D(O_i;\hat\eta)-\hat\psi.
\]

The standard error is

\[
\widehat{SE}
=
\frac{\operatorname{sd}(\hat D_{\psi,1},\ldots,\hat D_{\psi,n})}{\sqrt n}.
\]

A Wald-type confidence interval is

\[
\hat\psi
\pm
z_{1-\alpha/2}\widehat{SE}.
\]

---

## 2. Standard implementation steps

The coding agent should implement the following steps.

```text
1. Parse the observed data.
2. Define the target parameter.
3. Identify nuisance functions.
4. Estimate nuisance functions.
5. Use cross-fitting if nuisance estimators are flexible.
6. Construct the pseudo-outcome.
7. Estimate psi as the sample mean of the pseudo-outcome.
8. Estimate EIF values as pseudo_outcome - psi_hat.
9. Estimate standard error as sd(EIF) / sqrt(n).
10. Report confidence interval and diagnostics.
```

---

## 3. Generic Python skeleton

```python
import numpy as np

def estimate_from_pseudo_outcome(pseudo_outcome):
    pseudo_outcome = np.asarray(pseudo_outcome)
    n = len(pseudo_outcome)

    psi_hat = np.mean(pseudo_outcome)
    phi_hat = pseudo_outcome - psi_hat
    se_hat = np.std(phi_hat, ddof=1) / np.sqrt(n)

    ci_low = psi_hat - 1.96 * se_hat
    ci_high = psi_hat + 1.96 * se_hat

    return {
        "psi_hat": psi_hat,
        "se_hat": se_hat,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "phi_hat": phi_hat,
        "mean_phi": np.mean(phi_hat),
    }
```

---

## 4. Cross-fitting

### 4.1 Why cross-fitting?

If nuisance functions are estimated using flexible methods, such as random forests, gradient boosting, neural networks, splines, lasso, or super learner, in-sample nuisance predictions can create bias and invalidate simple asymptotic arguments.

Cross-fitting avoids using the same observation both to fit nuisance functions and to evaluate the EIF.

---

### 4.2 K-fold cross-fitting algorithm

```text
Input:
- Data O_1, ..., O_n
- Number of folds K
- Nuisance learners

Algorithm:
1. Randomly split observations into K folds.
2. For each fold k:
   a. Let train = all folds except k.
   b. Let test = fold k.
   c. Fit nuisance learners on train.
   d. Predict nuisance functions on test.
3. Combine all out-of-fold nuisance predictions.
4. Compute EIF-based pseudo-outcomes.
5. Estimate psi, EIF values, SE, and CI.
```

---

### 4.3 Cross-fitting template

```python
import numpy as np
from sklearn.model_selection import KFold

def crossfit_predictions(X, y, learner_factory, n_splits=5, random_state=123):
    X = np.asarray(X)
    y = np.asarray(y)

    n = len(y)
    preds = np.empty(n)

    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    for train_idx, test_idx in kf.split(X):
        model = learner_factory()
        model.fit(X[train_idx], y[train_idx])
        preds[test_idx] = model.predict(X[test_idx])

    return preds
```

For classifiers, use predicted probabilities rather than class labels.

```python
def crossfit_probabilities(X, a, classifier_factory, n_splits=5, random_state=123):
    X = np.asarray(X)
    a = np.asarray(a)

    n = len(a)
    preds = np.empty(n)

    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    for train_idx, test_idx in kf.split(X):
        model = classifier_factory()
        model.fit(X[train_idx], a[train_idx])
        preds[test_idx] = model.predict_proba(X[test_idx])[:, 1]

    return preds
```

---

## 5. Example: ATE

Observed data:

\[
O=(Y,A,X).
\]

Nuisance functions:

\[
m_1(X)=E(Y\mid A=1,X),
\]

\[
m_0(X)=E(Y\mid A=0,X),
\]

\[
e(X)=P(A=1\mid X).
\]

Pseudo-outcome:

\[
D(O;\eta)
=
m_1(X)-m_0(X)
+
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}.
\]

Estimator:

\[
\hat\psi=\mathbb P_n D(O;\hat\eta).
\]

---

### 5.1 ATE implementation

```python
import numpy as np

def aipw_ate(y, a, m1_hat, m0_hat, e_hat, eps=1e-6):
    y = np.asarray(y)
    a = np.asarray(a)
    m1_hat = np.asarray(m1_hat)
    m0_hat = np.asarray(m0_hat)
    e_hat = np.clip(np.asarray(e_hat), eps, 1.0 - eps)

    pseudo_outcome = (
        m1_hat
        - m0_hat
        + a / e_hat * (y - m1_hat)
        - (1.0 - a) / (1.0 - e_hat) * (y - m0_hat)
    )

    psi_hat = np.mean(pseudo_outcome)
    phi_hat = pseudo_outcome - psi_hat
    se_hat = np.std(phi_hat, ddof=1) / np.sqrt(len(y))

    return {
        "psi_hat": psi_hat,
        "se_hat": se_hat,
        "ci_low": psi_hat - 1.96 * se_hat,
        "ci_high": psi_hat + 1.96 * se_hat,
        "phi_hat": phi_hat,
        "pseudo_outcome": pseudo_outcome,
    }
```

---

### 5.2 Cross-fitted ATE nuisance estimation

```python
import numpy as np
from sklearn.base import clone
from sklearn.model_selection import KFold

def crossfit_ate_nuisance(X, a, y, outcome_model, propensity_model, n_splits=5, random_state=123):
    X = np.asarray(X)
    a = np.asarray(a)
    y = np.asarray(y)

    n = len(y)

    m1_hat = np.empty(n)
    m0_hat = np.empty(n)
    e_hat = np.empty(n)

    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    for train_idx, test_idx in kf.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        a_train, y_train = a[train_idx], y[train_idx]

        # Propensity model
        prop = clone(propensity_model)
        prop.fit(X_train, a_train)
        e_hat[test_idx] = prop.predict_proba(X_test)[:, 1]

        # Outcome model for treated
        out1 = clone(outcome_model)
        out1.fit(X_train[a_train == 1], y_train[a_train == 1])
        m1_hat[test_idx] = out1.predict(X_test)

        # Outcome model for controls
        out0 = clone(outcome_model)
        out0.fit(X_train[a_train == 0], y_train[a_train == 0])
        m0_hat[test_idx] = out0.predict(X_test)

    return {
        "m1_hat": m1_hat,
        "m0_hat": m0_hat,
        "e_hat": e_hat,
    }
```

---

## 6. Example: missing-data mean

Observed data:

\[
O=(R,RY,X).
\]

Nuisance functions:

\[
m(X)=E(Y\mid X),
\]

\[
\pi(X)=P(R=1\mid X).
\]

Pseudo-outcome:

\[
D(O;\eta)
=
\frac{R}{\pi(X)}
\{Y-m(X)\}
+
m(X).
\]

Implementation:

```python
import numpy as np

def aipw_missing_mean(y, r, m_hat, pi_hat, eps=1e-6):
    y = np.asarray(y)
    r = np.asarray(r)
    m_hat = np.asarray(m_hat)
    pi_hat = np.clip(np.asarray(pi_hat), eps, 1.0)

    pseudo_outcome = r / pi_hat * (y - m_hat) + m_hat

    psi_hat = np.mean(pseudo_outcome)
    phi_hat = pseudo_outcome - psi_hat
    se_hat = np.std(phi_hat, ddof=1) / np.sqrt(len(y))

    return {
        "psi_hat": psi_hat,
        "se_hat": se_hat,
        "ci_low": psi_hat - 1.96 * se_hat,
        "ci_high": psi_hat + 1.96 * se_hat,
        "phi_hat": phi_hat,
        "pseudo_outcome": pseudo_outcome,
    }
```

Important: if \(Y\) is unobserved when \(R=0\), then the array `y` must be filled in a way that does not affect the product `r * (y - m_hat)`. For example, missing values can be set to zero after masking, or the residual can be computed only for observed cases.

---

## 7. Example: mean potential outcome

For treatment value \(a_0\),

\[
\mu_{a_0}=E\{Y(a_0)\}.
\]

Nuisance functions:

\[
m_{a_0}(X)=E(Y\mid A=a_0,X),
\]

\[
g_{a_0}(X)=P(A=a_0\mid X).
\]

Pseudo-outcome:

\[
D(O;\eta)
=
\frac{I(A=a_0)}{g_{a_0}(X)}
\{Y-m_{a_0}(X)\}
+
m_{a_0}(X).
\]

Implementation:

```python
import numpy as np

def aipw_mean_potential_outcome(y, a, a_value, m_a_hat, g_a_hat, eps=1e-6):
    y = np.asarray(y)
    a = np.asarray(a)
    m_a_hat = np.asarray(m_a_hat)
    g_a_hat = np.clip(np.asarray(g_a_hat), eps, 1.0)

    indicator = (a == a_value).astype(float)

    pseudo_outcome = indicator / g_a_hat * (y - m_a_hat) + m_a_hat

    psi_hat = np.mean(pseudo_outcome)
    phi_hat = pseudo_outcome - psi_hat
    se_hat = np.std(phi_hat, ddof=1) / np.sqrt(len(y))

    return {
        "psi_hat": psi_hat,
        "se_hat": se_hat,
        "ci_low": psi_hat - 1.96 * se_hat,
        "ci_high": psi_hat + 1.96 * se_hat,
        "phi_hat": phi_hat,
        "pseudo_outcome": pseudo_outcome,
    }
```

---

## 8. Ratio and transformation implementation

### 8.1 Ratio

If

\[
\psi=\frac{\alpha}{\beta},
\]

and the agent has estimates \(\hat\alpha,\hat\beta\) and EIF values \(\hat D_\alpha,\hat D_\beta\), then

\[
\hat D_\psi
=
\frac{\hat D_\alpha-\hat\psi\hat D_\beta}{\hat\beta}.
\]

Implementation:

```python
import numpy as np

def ratio_from_eifs(alpha_hat, beta_hat, phi_alpha, phi_beta):
    phi_alpha = np.asarray(phi_alpha)
    phi_beta = np.asarray(phi_beta)

    psi_hat = alpha_hat / beta_hat
    phi_psi = (phi_alpha - psi_hat * phi_beta) / beta_hat
    se_hat = np.std(phi_psi, ddof=1) / np.sqrt(len(phi_psi))

    return {
        "psi_hat": psi_hat,
        "se_hat": se_hat,
        "ci_low": psi_hat - 1.96 * se_hat,
        "ci_high": psi_hat + 1.96 * se_hat,
        "phi_hat": phi_psi,
    }
```

---

### 8.2 Log transformation

If

\[
\psi=\log \theta,
\]

then

\[
D_\psi=\frac{D_\theta}{\theta}.
\]

Implementation:

```python
import numpy as np

def log_transform_from_eif(theta_hat, phi_theta):
    phi_theta = np.asarray(phi_theta)
    psi_hat = np.log(theta_hat)
    phi_psi = phi_theta / theta_hat
    se_hat = np.std(phi_psi, ddof=1) / np.sqrt(len(phi_psi))

    return {
        "psi_hat": psi_hat,
        "se_hat": se_hat,
        "ci_low": psi_hat - 1.96 * se_hat,
        "ci_high": psi_hat + 1.96 * se_hat,
        "phi_hat": phi_psi,
    }
```

---

## 9. Probability clipping and diagnostics

Inverse probability terms are numerically unstable when probabilities are close to 0 or 1.

Use clipping only as stabilization, not as a substitute for positivity.

```python
import numpy as np

def clip_probability(p, eps=1e-6):
    return np.clip(np.asarray(p), eps, 1.0 - eps)

def summarize_probability(p):
    p = np.asarray(p)
    return {
        "min": float(np.min(p)),
        "max": float(np.max(p)),
        "q01": float(np.quantile(p, 0.01)),
        "q05": float(np.quantile(p, 0.05)),
        "q50": float(np.quantile(p, 0.50)),
        "q95": float(np.quantile(p, 0.95)),
        "q99": float(np.quantile(p, 0.99)),
    }
```

The agent should report these diagnostics for:

\[
e(X),\quad
1-e(X),\quad
\pi(X),\quad
g_t(H_t),
\]

or any other probability that appears in a denominator.

---

## 10. Confidence intervals

Given \(\hat\psi\), \(\hat D_{\psi,i}\), and

\[
\widehat{SE}
=
\frac{\operatorname{sd}(\hat D_{\psi,i})}{\sqrt n},
\]

the 95% Wald interval is

\[
\hat\psi\pm 1.96\widehat{SE}.
\]

Implementation:

```python
def wald_ci(psi_hat, se_hat, z=1.96):
    return psi_hat - z * se_hat, psi_hat + z * se_hat
```

For small samples, highly skewed EIF values, or weak positivity, bootstrap or robust alternatives may be considered, but the EIF-based standard error is the default first implementation.

---

## 11. Practical warnings

### 11.1 Positivity

Large inverse weights can dominate the estimator.

The agent should report:

- Minimum estimated probability
- Maximum estimated probability
- Quantiles of inverse weights
- Number of observations affected by clipping

---

### 11.2 Nuisance overfitting

Without cross-fitting, flexible nuisance models may overfit. The agent should use cross-fitting unless explicitly told not to.

---

### 11.3 Poor nuisance estimation

EIF estimators are robust to some nuisance errors, but not arbitrary errors. For ATE, the AIPW estimator is doubly robust, but accurate inference still needs suitable rates or empirical-process control.

---

### 11.4 Ratio instability

For ratio targets,

\[
\psi=\alpha/\beta,
\]

the denominator \(\beta\) must be bounded away from zero.

---

### 11.5 Quantile density

For quantile targets,

\[
q_\tau=F^{-1}(\tau),
\]

the density at the quantile must satisfy

\[
f(q_\tau)>0.
\]

---

### 11.6 Nonregular targets

Do not implement a standard EIF estimator for:

\[
p_Y(y_0),
\]

\[
E\{Y(1)-Y(0)\mid X=x\}
\]

with continuous \(X\),

\[
\max_x m(x),
\]

without additional smoothing or regularity assumptions.

---

## 12. Final implementation checklist

- [ ] The pseudo-outcome is correctly constructed.
- [ ] The estimator is the sample mean of the pseudo-outcome.
- [ ] EIF values are pseudo-outcome minus point estimate.
- [ ] Standard error is empirical EIF standard deviation divided by \(\sqrt n\).
- [ ] Confidence interval is reported.
- [ ] Cross-fitting is used for flexible nuisances.
- [ ] Inverse probabilities are clipped only for numerical stability.
- [ ] Positivity diagnostics are reported.
- [ ] Ratio denominators are checked.
- [ ] Quantile density conditions are checked.
- [ ] Nonregularity warnings are issued when needed.
