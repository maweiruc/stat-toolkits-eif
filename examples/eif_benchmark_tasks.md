# EIF benchmark tasks

This file provides benchmark tasks for testing whether a coding agent can correctly derive, identify, implement, and validate efficient influence functions (EIFs).

Each benchmark includes:

- Observed data
- Target parameter
- Assumptions
- Expected EIF
- Checks
- Common failure modes

The agent should solve these tasks without directly copying formulas unless it first classifies the problem and verifies the assumptions.

---

## How to use this file

For each task, ask the coding agent:

```text
Use the EIF toolkit. Solve the following benchmark task.

Return:
1. Problem classification
2. Observed-data functional
3. Nuisance functions
4. Likelihood factorization
5. Score decomposition
6. EIF
7. Mean-zero verification
8. Estimator
9. Code implementation
10. Validation checks
```

---

# Level 1: Full-data smooth functionals

## Task 1.1: Mean

Observed data:

\[
O=Y.
\]

Target:

\[
\psi=E(Y).
\]

Expected EIF:

\[
D_\psi(O)=Y-\psi.
\]

Checks:

\[
E(Y-\psi)=0.
\]

Common failure mode:

- Overcomplicating the problem by introducing unnecessary nuisance functions.

---

## Task 1.2: Mean of a transformation

Observed data:

\[
O=Y.
\]

Target:

\[
\psi=E\{g(Y)\}.
\]

Expected EIF:

\[
D_\psi(O)=g(Y)-\psi.
\]

Example:

\[
g(Y)=I(Y\le t).
\]

Then:

\[
D_\psi(O)=I(Y\le t)-P(Y\le t).
\]

---

## Task 1.3: Variance

Observed data:

\[
O=Y.
\]

Target:

\[
\psi=\operatorname{Var}(Y).
\]

Let

\[
\mu=E(Y).
\]

Expected EIF:

\[
D_\psi(O)=(Y-\mu)^2-\psi.
\]

Checks:

\[
E\{(Y-\mu)^2-\psi\}=0.
\]

Common failure mode:

- Writing \(Y^2-E(Y^2)\) instead of the EIF for variance.
- Forgetting that the derivative of the mean cancels in the variance functional.

---

## Task 1.4: Quantile

Observed data:

\[
O=Y.
\]

Target:

\[
q_\tau=F^{-1}(\tau).
\]

Assume \(f(q_\tau)>0\).

Expected EIF:

\[
D_{q_\tau}(O)=
\frac{\tau-I(Y\le q_\tau)}{f(q_\tau)}.
\]

Checks:

\[
E\{D_{q_\tau}(O)\}=0.
\]

Common failure modes:

- Sign error.
- Forgetting the density denominator.
- Applying the formula when \(f(q_\tau)=0\).

---

# Level 2: Ratio and transformation tasks

## Task 2.1: Ratio of means

Observed data:

\[
O=(Y,Z).
\]

Target:

\[
\psi=\frac{E(Y)}{E(Z)}.
\]

Let

\[
\beta=E(Z).
\]

Expected EIF:

\[
D_\psi(O)=\frac{Y-\psi Z}{\beta}.
\]

Equivalent expression:

\[
D_\psi(O)
=
\frac{(Y-EY)-\psi(Z-EZ)}{E(Z)}.
\]

Checks:

\[
E(Y-\psi Z)=0.
\]

Common failure modes:

- Forgetting the denominator \(E(Z)\).
- Using \(Z-\psi Y\) instead of \(Y-\psi Z\).
- Failing to check \(E(Z)\neq 0\).

---

## Task 2.2: Log mean

Observed data:

\[
O=Y.
\]

Target:

\[
\psi=\log E(Y).
\]

Let

\[
\mu=E(Y).
\]

Expected EIF:

\[
D_\psi(O)=\frac{Y-\mu}{\mu}.
\]

Checks:

\[
E\{D_\psi(O)\}=0.
\]

Common failure mode:

- Writing \(\log Y-\psi\), which corresponds to \(E(\log Y)\), not \(\log E(Y)\).

---

# Level 3: Missing-data tasks

## Task 3.1: Mean under MAR

Observed data:

\[
O=(R,RY,X).
\]

Assumptions:

\[
Y\perp R\mid X,
\]

\[
\pi(X)=P(R=1\mid X)>0.
\]

Target:

\[
\psi=E(Y).
\]

Define:

\[
m(X)=E(Y\mid X).
\]

Expected EIF:

\[
D_\psi(O)
=
\frac{R}{\pi(X)}\{Y-m(X)\}
+
m(X)-\psi.
\]

Checks:

1. Residual part has mean zero conditional on \(X\).
2. If \(R=1\) always, EIF reduces to \(Y-\psi\).

Common failure modes:

- Forgetting \(m(X)-\psi\).
- Using \(E(Y\mid R=1,X)\) without stating MAR.
- Not handling unobserved \(Y\) correctly in code.

---

## Task 3.2: Distribution function under MAR

Observed data:

\[
O=(R,RY,X).
\]

Target:

\[
F(t)=P(Y\le t).
\]

Define:

\[
m_t(X)=P(Y\le t\mid X).
\]

Expected EIF:

\[
D_{F(t)}(O)
=
\frac{R}{\pi(X)}
\{I(Y\le t)-m_t(X)\}
+
m_t(X)-F(t).
\]

Checks:

- If \(R=1\), reduces to \(I(Y\le t)-F(t)\).

---

## Task 3.3: Quantile under MAR

Observed data:

\[
O=(R,RY,X).
\]

Target:

\[
q_\tau=F^{-1}(\tau).
\]

Expected EIF:

\[
D_{q_\tau}(O)
=
-\frac{D_{F(q_\tau)}(O)}{f(q_\tau)}.
\]

Expanded:

\[
D_{q_\tau}(O)
=
\frac{
\tau
-
\left[
\frac{R}{\pi(X)}
\{I(Y\le q_\tau)-m_{q_\tau}(X)\}
+
m_{q_\tau}(X)
\right]
}
{f(q_\tau)}.
\]

Common failure modes:

- Sign error.
- Forgetting the density at the quantile.
- Confusing \(m_{q_\tau}(X)\) with \(m(X)=E(Y\mid X)\).

---

# Level 4: Point-treatment causal tasks

## Task 4.1: Mean potential outcome

Observed data:

\[
O=(Y,A,X),
\]

with \(A\in\{0,1\}\).

Assumptions:

\[
Y=AY(1)+(1-A)Y(0),
\]

\[
(Y(1),Y(0))\perp A\mid X,
\]

\[
0<c<P(A=1\mid X)<1-c.
\]

Target:

\[
\mu_a=E\{Y(a)\}.
\]

Define:

\[
m_a(X)=E(Y\mid A=a,X),
\]

\[
g_a(X)=P(A=a\mid X).
\]

Expected EIF:

\[
D_{\mu_a}(O)
=
\frac{I(A=a)}{g_a(X)}
\{Y-m_a(X)\}
+
m_a(X)-\mu_a.
\]

Checks:

- If no covariates and treatment probability is \(p_a\), reduces to the two-sample mean EIF.

---

## Task 4.2: ATE

Target:

\[
\psi=E\{Y(1)-Y(0)\}.
\]

Define:

\[
e(X)=P(A=1\mid X),
\]

\[
m_a(X)=E(Y\mid A=a,X).
\]

Expected EIF:

\[
D_\psi(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

Checks:

- Difference of \(D_{\mu_1}\) and \(D_{\mu_0}\).
- If no covariates, reduces to the standard two-sample influence function.

Common failure modes:

- Forgetting the plug-in contrast \(m_1(X)-m_0(X)\).
- Using \(e(X)\) in the wrong denominator.
- Not clipping or diagnosing propensity scores in code.

---

## Task 4.3: ATT

Target:

\[
\psi=E\{Y(1)-Y(0)\mid A=1\}.
\]

Let:

\[
p=P(A=1),
\]

\[
e(X)=P(A=1\mid X),
\]

\[
m_0(X)=E(Y\mid A=0,X).
\]

Expected EIF:

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

Checks:

- Mean zero.
- If treatment is randomized with constant \(e(X)=p\), verify reduction to a simpler treated-control comparison.

Common failure modes:

- Using the ATE EIF instead of ATT EIF.
- Adding an unnecessary \(m_1(X)\) residual term.
- Forgetting the ratio nature through \(p=P(A=1)\).

---

## Task 4.4: Subgroup ATE

Let:

\[
G=I(X\in\mathcal G),
\]

\[
p_G=P(G=1).
\]

Target:

\[
\psi_{\mathcal G}=E\{Y(1)-Y(0)\mid G=1\}.
\]

Expected EIF:

\[
D_{\psi_{\mathcal G}}(O)
=
\frac{G}{p_G}
\left[
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)
-
\psi_{\mathcal G}
\right].
\]

Checks:

- If \(G=1\) always, reduces to the ATE EIF.

Common failure mode:

- Forgetting the subgroup ratio \(G/p_G\).

---

# Level 5: Distributional causal tasks

## Task 5.1: Distribution of potential outcome

Target:

\[
F_a(t)=P\{Y(a)\le t\}.
\]

Define:

\[
m_{a,t}(X)=P(Y\le t\mid A=a,X).
\]

Expected EIF:

\[
D_{F_a(t)}(O)
=
\frac{I(A=a)}{P(A=a\mid X)}
\{I(Y\le t)-m_{a,t}(X)\}
+
m_{a,t}(X)-F_a(t).
\]

---

## Task 5.2: Quantile treatment effect

Target:

\[
\psi_\tau=q_{1,\tau}-q_{0,\tau}.
\]

Expected EIF:

\[
D_{\psi_\tau}(O)
=
-\frac{D_{F_1(q_{1,\tau})}(O)}{f_1(q_{1,\tau})}
+
\frac{D_{F_0(q_{0,\tau})}(O)}{f_0(q_{0,\tau})}.
\]

Equivalently:

\[
D_{\psi_\tau}=D_{q_{1,\tau}}-D_{q_{0,\tau}}.
\]

Common failure modes:

- Sign error.
- Using the outcome density rather than the counterfactual density.
- Forgetting density positivity.

---

# Level 6: IV and ratio tasks

## Task 6.1: Covariate-adjusted Wald estimand

Observed data:

\[
O=(Y,A,Z,X),
\]

with binary instrument \(Z\).

Define:

\[
q(X)=P(Z=1\mid X),
\]

\[
m_z^Y(X)=E(Y\mid Z=z,X),
\]

\[
m_z^A(X)=E(A\mid Z=z,X).
\]

Target:

\[
\psi=\frac{\nu_Y}{\nu_A},
\]

where

\[
\nu_Y=E\{m_1^Y(X)-m_0^Y(X)\},
\]

\[
\nu_A=E\{m_1^A(X)-m_0^A(X)\}.
\]

Expected EIF:

\[
D_\psi(O)
=
\frac{D_{\nu_Y}(O)-\psi D_{\nu_A}(O)}
{\nu_A}.
\]

with

\[
D_{\nu_Y}(O)
=
\frac{Z}{q(X)}
\{Y-m_1^Y(X)\}
-
\frac{1-Z}{1-q(X)}
\{Y-m_0^Y(X)\}
+
m_1^Y(X)-m_0^Y(X)-\nu_Y,
\]

and similarly for \(D_{\nu_A}\) replacing \(Y\) by \(A\).

Checks:

- Denominator \(\nu_A\) must be bounded away from zero.
- This is a ratio EIF.

---

# Level 7: Longitudinal treatment tasks

## Task 7.1: Two-time dynamic treatment regime

Observed data:

\[
O=(L_0,A_0,L_1,A_1,Y).
\]

Regime:

\[
d=(d_0,d_1).
\]

Histories:

\[
H_0=L_0,
\]

\[
H_1=(L_0,A_0,L_1).
\]

Treatment mechanisms:

\[
g_0(H_0)=P(A_0=d_0(H_0)\mid H_0),
\]

\[
g_1(H_1)=P(A_1=d_1(H_1)\mid H_1).
\]

Sequential regressions:

\[
Q_2=Y,
\]

\[
Q_1(H_1)=E(Y\mid H_1,A_1=d_1(H_1)),
\]

\[
Q_0(H_0)=E\{Q_1(H_1)\mid H_0,A_0=d_0(H_0)\}.
\]

Target:

\[
\psi_d=E\{Y^d\}=E\{Q_0(H_0)\}.
\]

Expected EIF:

\[
D_{\psi_d}(O)
=
W_0^d\{Q_1(H_1)-Q_0(H_0)\}
+
W_1^d\{Y-Q_1(H_1)\}
+
Q_0(H_0)-\psi_d,
\]

where

\[
W_0^d=
\frac{I(A_0=d_0(H_0))}{g_0(H_0)},
\]

\[
W_1^d=
\frac{I(A_0=d_0(H_0))I(A_1=d_1(H_1))}
{g_0(H_0)g_1(H_1)}.
\]

Common failure modes:

- Incorrect history definition.
- Missing one sequential regression term.
- Incorrect cumulative weight.

---

# Level 8: Nonregular warning tasks

## Task 8.1: Pointwise CATE with continuous covariates

Observed data:

\[
O=(Y,A,X),
\]

where \(X\) is continuous.

Target:

\[
\tau(x)=E\{Y(1)-Y(0)\mid X=x\}.
\]

Expected answer:

```text
In a fully nonparametric model, this is generally not a root-n pathwise differentiable target. A standard EIF does not exist without smoothing, parametric structure, or additional restrictions.
```

Acceptable alternatives:

\[
E\{Y(1)-Y(0)\mid X\in\mathcal G\},
\]

or a kernel-smoothed target.

---

## Task 8.2: Density at a point

Target:

\[
p_Y(y_0).
\]

Expected answer:

```text
The density at a point is generally not a regular root-n estimable parameter in a fully nonparametric model. Use a smoothed target such as E[K_h(Y-y_0)] with fixed h.
```

For fixed \(h\),

\[
\psi_h=E\{K_h(Y-y_0)\},
\]

\[
D_{\psi_h}(O)=K_h(Y-y_0)-\psi_h.
\]

---

## Task 8.3: Maximum of a regression function

Target:

\[
\max_x E(Y\mid X=x).
\]

Expected answer:

```text
This is generally nonregular without additional uniqueness, smoothness, and margin conditions. Do not force a standard EIF.
```

---

# Scoring rubric

A coding agent passes a benchmark if it:

- [ ] Correctly classifies the problem.
- [ ] States the observed-data functional.
- [ ] Defines nuisance functions.
- [ ] Gives the correct EIF.
- [ ] Verifies mean-zero.
- [ ] States positivity or density conditions.
- [ ] Gives a valid estimator.
- [ ] Identifies nonregular targets instead of forcing an EIF.
- [ ] Provides implementation checks.
