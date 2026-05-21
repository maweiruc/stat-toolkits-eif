# EIF worked derivations

This document gives detailed derivations for selected efficient influence functions (EIFs).

The goal is to teach the derivation pattern, not just list formulas.

For restricted semiparametric projection examples involving nuisance tangent spaces, see:

```text
eif_restricted_moment_worked_derivation.md
eif_plsim_worked_derivation.md
```

---

## 1. Mean

Observed data:

\[
O=Y.
\]

Target:

\[
\psi(P)=E_P(Y)=\int y\,dP(y).
\]

Let \(P_\varepsilon\) be a parametric submodel through \(P\) with score \(S(Y)\).

Then

\[
\left.
\frac{d}{d\varepsilon}
\psi(P_\varepsilon)
\right|_{\varepsilon=0}
=
\left.
\frac{d}{d\varepsilon}
\int y p_\varepsilon(y)\,dy
\right|_{\varepsilon=0}.
\]

Since

\[
\left.
\frac{d}{d\varepsilon}p_\varepsilon(y)
\right|_{\varepsilon=0}
=
S(y)p(y),
\]

we have

\[
\left.
\frac{d}{d\varepsilon}
\psi(P_\varepsilon)
\right|_{\varepsilon=0}
=
\int y S(y)p(y)\,dy
=
E\{YS(Y)\}.
\]

Because every score satisfies \(E\{S(Y)\}=0\),

\[
E\{YS(Y)\}
=
E\{(Y-\psi)S(Y)\}.
\]

Therefore,

\[
D_\psi(Y)=Y-\psi.
\]

---

## 2. Variance

Observed data:

\[
O=Y.
\]

Target:

\[
\psi(P)=\operatorname{Var}_P(Y).
\]

Write

\[
\mu=E(Y),
\]

\[
\psi=E(Y^2)-\mu^2.
\]

The EIF for \(E(Y^2)\) is

\[
Y^2-E(Y^2).
\]

The EIF for \(\mu\) is

\[
Y-\mu.
\]

By the delta rule, the EIF for \(\mu^2\) is

\[
2\mu(Y-\mu).
\]

Therefore,

\[
D_\psi(Y)
=
\{Y^2-E(Y^2)\}
-
2\mu(Y-\mu).
\]

Simplify:

\[
D_\psi(Y)
=
Y^2-E(Y^2)-2\mu Y+2\mu^2.
\]

Since

\[
E(Y^2)=\psi+\mu^2,
\]

we get

\[
D_\psi(Y)
=
Y^2-2\mu Y+\mu^2-\psi
=
(Y-\mu)^2-\psi.
\]

Thus,

\[
D_\psi(Y)=(Y-\mu)^2-\operatorname{Var}(Y).
\]

---

## 3. Quantile

Observed data:

\[
O=Y.
\]

Target:

\[
q_\tau=F^{-1}(\tau),
\]

where

\[
F(q_\tau)=\tau.
\]

Assume \(F\) has density \(f\) and

\[
f(q_\tau)>0.
\]

Let \(F_\varepsilon\) be a submodel and \(q_\varepsilon\) satisfy

\[
F_\varepsilon(q_\varepsilon)=\tau.
\]

Differentiate both sides at \(\varepsilon=0\):

\[
\left.
\frac{d}{d\varepsilon}
F_\varepsilon(q_\varepsilon)
\right|_{\varepsilon=0}
=0.
\]

By the chain rule:

\[
\left.
\frac{\partial}{\partial\varepsilon}
F_\varepsilon(q_\tau)
\right|_{\varepsilon=0}
+
f(q_\tau)
\left.
\frac{d}{d\varepsilon}
q_\varepsilon
\right|_{\varepsilon=0}
=
0.
\]

The EIF for \(F(q_\tau)\) is

\[
I(Y\le q_\tau)-F(q_\tau)
=
I(Y\le q_\tau)-\tau.
\]

Thus,

\[
\left.
\frac{\partial}{\partial\varepsilon}
F_\varepsilon(q_\tau)
\right|_{\varepsilon=0}
=
E\left[
\{I(Y\le q_\tau)-\tau\}S(Y)
\right].
\]

Therefore,

\[
\left.
\frac{d}{d\varepsilon}
q_\varepsilon
\right|_{\varepsilon=0}
=
-
\frac{
E\left[
\{I(Y\le q_\tau)-\tau\}S(Y)
\right]
}
{f(q_\tau)}.
\]

Hence the EIF is

\[
D_{q_\tau}(Y)
=
-\frac{I(Y\le q_\tau)-\tau}{f(q_\tau)}
=
\frac{\tau-I(Y\le q_\tau)}{f(q_\tau)}.
\]

---

## 4. Missing-data mean under MAR

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

Identification:

\[
\psi=E\{m(X)\},
\]

where

\[
m(X)=E(Y\mid X).
\]

Likelihood factorization:

\[
p(o)=p(x)p(r\mid x)p(y\mid x)^r.
\]

Score decomposition:

\[
S(O)=S_X(X)+S_R(R\mid X)+R S_Y(Y\mid X),
\]

with

\[
E(S_X)=0,
\]

\[
E(S_R\mid X)=0,
\]

\[
E(S_Y\mid X)=0.
\]

The target depends on \(p(x)\) and \(p(y\mid x)\), but not directly on \(p(r\mid x)\).

### Contribution from \(p(x)\)

Since

\[
\psi=E\{m(X)\},
\]

perturbing \(p(x)\) gives

\[
E[\{m(X)-\psi\}S_X(X)].
\]

So the \(X\)-component is

\[
m(X)-\psi.
\]

### Contribution from \(p(y\mid x)\)

The conditional mean changes as

\[
\left.
\frac{d}{d\varepsilon}
m_\varepsilon(X)
\right|_0
=
E[\{Y-m(X)\}S_Y(Y\mid X)\mid X].
\]

In observed data, \(Y\) is only observed when \(R=1\). To express this as an observed-data inner product, use inverse probability weighting:

\[
E\left[
\frac{R}{\pi(X)}
\{Y-m(X)\}
S_Y(Y\mid X)
\right].
\]

Therefore, the residual component is

\[
\frac{R}{\pi(X)}
\{Y-m(X)\}.
\]

Combining components:

\[
D_\psi(O)
=
\frac{R}{\pi(X)}
\{Y-m(X)\}
+
m(X)-\psi.
\]

Mean-zero verification:

\[
E\left[
\frac{R}{\pi(X)}
\{Y-m(X)\}
\mid X
\right]
=
\frac{\pi(X)}{\pi(X)}
E\{Y-m(X)\mid X\}
=
0.
\]

And

\[
E\{m(X)-\psi\}=0.
\]

---

## 5. ATE under unconfoundedness

Observed data:

\[
O=(Y,A,X),
\]

where \(A\in\{0,1\}\).

Assumptions:

\[
Y=AY(1)+(1-A)Y(0),
\]

\[
(Y(1),Y(0))\perp A\mid X,
\]

\[
0<c<e(X)<1-c,
\]

where

\[
e(X)=P(A=1\mid X).
\]

Target:

\[
\psi=E\{Y(1)-Y(0)\}.
\]

Identification:

\[
\psi=E\{m_1(X)-m_0(X)\},
\]

where

\[
m_a(X)=E(Y\mid A=a,X).
\]

Likelihood factorization:

\[
p(o)=p(y\mid a,x)p(a\mid x)p(x).
\]

Score decomposition:

\[
S(O)=S_Y(Y\mid A,X)+S_A(A\mid X)+S_X(X).
\]

### Contribution from \(p(x)\)

The target is

\[
\psi=E_X\{m_1(X)-m_0(X)\}.
\]

Perturbing \(p(x)\) gives

\[
E[
\{m_1(X)-m_0(X)-\psi\}S_X(X)
].
\]

So the \(X\)-component is

\[
m_1(X)-m_0(X)-\psi.
\]

### Contribution from \(p(y\mid a,x)\)

For \(m_1(X)\),

\[
\left.
\frac{d}{d\varepsilon}
m_{1,\varepsilon}(X)
\right|_0
=
E[
\{Y-m_1(X)\}S_Y(Y\mid A,X)
\mid A=1,X
].
\]

Convert to observed-data form:

\[
E\left[
\frac{A}{e(X)}
\{Y-m_1(X)\}
S_Y(Y\mid A,X)
\right].
\]

Similarly, for \(m_0(X)\):

\[
E\left[
\frac{1-A}{1-e(X)}
\{Y-m_0(X)\}
S_Y(Y\mid A,X)
\right].
\]

Because the target is \(m_1-m_0\), the residual component is

\[
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}.
\]

### Contribution from \(p(a\mid x)\)

The target does not directly depend on \(p(a\mid x)\), so there is no separate \(S_A\)-component.

Thus,

\[
D_\psi(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

---

## 6. ATT

Observed data:

\[
O=(Y,A,X).
\]

Target:

\[
\psi=E\{Y(1)-Y(0)\mid A=1\}.
\]

Under standard identification assumptions,

\[
\psi
=
E\{Y-m_0(X)\mid A=1\}.
\]

Let

\[
p=P(A=1).
\]

Then

\[
\psi
=
\frac{
E[A\{Y-m_0(X)\}]
}
{p}.
\]

This ratio representation is useful.

Define numerator:

\[
\alpha=E[A\{Y-m_0(X)\}].
\]

Then

\[
\psi=\alpha/p.
\]

The EIF for ATT is

\[
D_\psi(O)
=
\frac{D_\alpha(O)-\psi D_p(O)}{p}.
\]

Here

\[
D_p(O)=A-p.
\]

The numerator component leads to the final known expression:

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

Mean-zero check:

First term expectation:

\[
E\left[
\frac{A}{p}
\{Y-m_0(X)-\psi\}
\right]
=
\frac{1}{p}E[A\{Y-m_0(X)\}]-\psi
=
0.
\]

Second term expectation:

\[
E\left[
\frac{1-A}{p}
\frac{e(X)}{1-e(X)}
\{Y-m_0(X)\}
\right]
=0,
\]

because

\[
E\{Y-m_0(X)\mid A=0,X\}=0.
\]

Therefore,

\[
E\{D_\psi(O)\}=0.
\]

---

## 7. Ratio of means

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
\alpha=E(Y),
\qquad
\beta=E(Z).
\]

Then

\[
\psi=\alpha/\beta.
\]

The EIFs for \(\alpha\) and \(\beta\) are:

\[
D_\alpha=Y-\alpha,
\]

\[
D_\beta=Z-\beta.
\]

By the ratio rule:

\[
D_\psi
=
\frac{D_\alpha-\psi D_\beta}{\beta}.
\]

Therefore,

\[
D_\psi
=
\frac{(Y-\alpha)-\psi(Z-\beta)}{\beta}.
\]

Since \(\alpha=\psi\beta\), this simplifies to

\[
D_\psi
=
\frac{Y-\psi Z}{\beta}.
\]

---

## 8. Longitudinal dynamic treatment regime

Observed data:

\[
O=(L_0,A_0,L_1,A_1,\ldots,L_K,A_K,Y).
\]

Let \(d=(d_0,\ldots,d_K)\) be a fixed regime.

Histories:

\[
H_t=(L_0,A_0,L_1,\ldots,A_{t-1},L_t).
\]

Treatment mechanisms:

\[
g_t(H_t)=P\{A_t=d_t(H_t)\mid H_t\}.
\]

Cumulative weights:

\[
W_t^d
=
\prod_{s=0}^t
\frac{I\{A_s=d_s(H_s)\}}{g_s(H_s)}.
\]

Sequential regressions:

\[
Q_{K+1}=Y,
\]

\[
Q_t(H_t)
=
E\{Q_{t+1}(H_{t+1})\mid H_t,A_t=d_t(H_t)\}.
\]

Target:

\[
\psi_d=E\{Y^d\}=E\{Q_0(L_0)\}.
\]

EIF:

\[
D_{\psi_d}(O)
=
\sum_{t=0}^K
W_t^d
\{Q_{t+1}(H_{t+1})-Q_t(H_t)\}
+
Q_0(L_0)-\psi_d.
\]

Mean-zero intuition:

For each \(t\),

\[
E[
Q_{t+1}(H_{t+1})-Q_t(H_t)
\mid H_t,A_t=d_t(H_t)
]
=0.
\]

The weight \(W_t^d\) converts the conditional residual under the regime into an observed-data residual. The final term

\[
Q_0(L_0)-\psi_d
\]

accounts for variation in the baseline covariate distribution.

---

## 9. General derivation pattern

Across the examples above, the same pattern appears:

1. Express target as observed-data functional.
2. Factorize the likelihood.
3. Decompose the score.
4. Perturb each likelihood component.
5. Convert conditional residuals into observed-data residuals using inverse probabilities.
6. Add the plug-in target component.
7. Subtract the target to center.

The common structure is:

\[
D_\psi(O)
=
\text{weighted residual correction}
+
\text{plug-in target}
-
\text{target}.
\]
