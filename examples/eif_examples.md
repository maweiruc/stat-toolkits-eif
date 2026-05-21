# EIF examples: checked reference library

This document collects common efficient influence function (EIF) examples for semiparametric estimation. Unless otherwise stated, all nuisance functions are population-level quantities. In code, replace them by estimates, preferably using cross-fitting when flexible machine learning methods are used.

Throughout, \(O\sim P\), the target is \(\psi=\psi(P)\), and the EIF is denoted by \(D_\psi(O)\), satisfying

\[
E\{D_\psi(O)\}=0.
\]

For many examples below, the EIF has the form

\[
D_\psi(O)
=
\text{weighted residual correction}
+
\text{plug-in target}
-
\text{target}.
\]

---

## 0. General rules

### 0.1 Mean-type functional

If

\[
\psi=E\{h(O)\},
\]

then

\[
D_\psi(O)=h(O)-\psi.
\]

---

### 0.2 Ratio functional

If

\[
\psi=\frac{\alpha}{\beta},
\]

and \(D_\alpha,D_\beta\) are EIFs for \(\alpha,\beta\), then

\[
D_\psi(O)
=
\frac{D_\alpha(O)-\psi D_\beta(O)}{\beta}.
\]

---

### 0.3 Smooth transformation

If

\[
\psi=h(\theta),
\]

then

\[
D_\psi(O)
=
h'(\theta)D_\theta(O).
\]

For vector \(\theta\),

\[
D_\psi(O)
=
\nabla h(\theta)^\top D_\theta(O).
\]

---

### 0.4 Estimating-equation parameter

If \(\beta\) is defined by

\[
E\{\varphi(O;\beta)\}=0,
\]

and

\[
A
=
E\left[
\frac{\partial}{\partial \beta^\top}
\varphi(O;\beta)
\right],
\]

then

\[
D_\beta(O)
=
-A^{-1}\varphi(O;\beta).
\]

This is the general M-estimation EIF.

---

## 1. Full-data basic functionals

### 1.1 Mean

Target:

\[
\psi=E(Y).
\]

EIF:

\[
D_\psi(O)=Y-\psi.
\]

---

### 1.2 Mean of a transformation

Target:

\[
\psi=E\{g(Y)\}.
\]

EIF:

\[
D_\psi(O)=g(Y)-\psi.
\]

Examples include \(g(Y)=Y^2\), \(g(Y)=\log Y\), and \(g(Y)=I(Y\le t)\).

---

### 1.3 Probability / risk

For binary \(Y\),

\[
\psi=P(Y=1)=E(Y).
\]

EIF:

\[
D_\psi(O)=Y-\psi.
\]

More generally, for an event \(B\),

\[
\psi=P(Y\in B),
\]

\[
D_\psi(O)=I(Y\in B)-\psi.
\]

---

### 1.4 Distribution function

Target:

\[
F(t)=P(Y\le t).
\]

EIF:

\[
D_{F(t)}(O)=I(Y\le t)-F(t).
\]

---

### 1.5 Survival function without censoring

Target:

\[
S(t)=P(Y>t).
\]

EIF:

\[
D_{S(t)}(O)=I(Y>t)-S(t).
\]

---

### 1.6 Second moment

Target:

\[
\psi=E(Y^2).
\]

EIF:

\[
D_\psi(O)=Y^2-\psi.
\]

---

### 1.7 Variance

Let

\[
\mu=E(Y),
\]

\[
\sigma^2=E\{(Y-\mu)^2\}.
\]

EIF:

\[
D_{\sigma^2}(O)
=
(Y-\mu)^2-\sigma^2.
\]

---

### 1.8 Standard deviation

Target:

\[
\sigma=\sqrt{\sigma^2}.
\]

EIF:

\[
D_\sigma(O)
=
\frac{(Y-\mu)^2-\sigma^2}{2\sigma}.
\]

---

### 1.9 Covariance

Let \(O=(X,Y)\),

\[
\mu_X=E(X),\qquad \mu_Y=E(Y),
\]

\[
\sigma_{XY}=E\{(X-\mu_X)(Y-\mu_Y)\}.
\]

EIF:

\[
D_{\sigma_{XY}}(O)
=
(X-\mu_X)(Y-\mu_Y)-\sigma_{XY}.
\]

---

### 1.10 Correlation

Define

\[
\rho=\frac{\sigma_{XY}}{\sigma_X\sigma_Y}.
\]

Let

\[
D_{\sigma_{XY}}(O)
=
(X-\mu_X)(Y-\mu_Y)-\sigma_{XY},
\]

\[
D_{\sigma_X^2}(O)
=
(X-\mu_X)^2-\sigma_X^2,
\]

\[
D_{\sigma_Y^2}(O)
=
(Y-\mu_Y)^2-\sigma_Y^2.
\]

Then

\[
D_\rho(O)
=
\frac{D_{\sigma_{XY}}(O)}{\sigma_X\sigma_Y}
-
\frac{\rho}{2}
\left[
\frac{D_{\sigma_X^2}(O)}{\sigma_X^2}
+
\frac{D_{\sigma_Y^2}(O)}{\sigma_Y^2}
\right].
\]

---

### 1.11 Ratio of means

Target:

\[
\psi=\frac{E(Y)}{E(Z)}.
\]

Let

\[
\alpha=E(Y),\qquad \beta=E(Z).
\]

EIF:

\[
D_\psi(O)
=
\frac{(Y-\alpha)-\psi(Z-\beta)}{\beta}.
\]

Equivalently,

\[
D_\psi(O)=\frac{Y-\psi Z}{\beta}.
\]

---

### 1.12 Log mean

Target:

\[
\psi=\log E(Y).
\]

Let

\[
\mu=E(Y).
\]

EIF:

\[
D_\psi(O)=\frac{Y-\mu}{\mu}.
\]

---

### 1.13 Odds

Let

\[
p=P(Y=1).
\]

Target:

\[
\psi=\frac{p}{1-p}.
\]

EIF:

\[
D_\psi(O)=\frac{Y-p}{(1-p)^2}.
\]

---

### 1.14 Log odds

Target:

\[
\psi=\log\frac{p}{1-p}.
\]

EIF:

\[
D_\psi(O)=\frac{Y-p}{p(1-p)}.
\]

---

### 1.15 Quantile

Target:

\[
q_\tau=F^{-1}(\tau),
\]

where

\[
F(q_\tau)=\tau.
\]

Assume \(Y\) has density \(f\) and \(f(q_\tau)>0\). Then

\[
D_{q_\tau}(O)
=
\frac{\tau-I(Y\le q_\tau)}{f(q_\tau)}.
\]

---

## 2. Regression and M-estimation examples

### 2.1 General estimating-equation parameter

If

\[
E\{\varphi(O;\beta)\}=0,
\]

then, with

\[
A
=
E\left[
\frac{\partial}{\partial \beta^\top}
\varphi(O;\beta)
\right],
\]

the EIF is

\[
D_\beta(O)
=
-A^{-1}\varphi(O;\beta).
\]

---

### 2.2 OLS population coefficient

Target:

\[
\beta
=
\arg\min_b E\{Y-X^\top b\}^2.
\]

Equivalently,

\[
E\{X(Y-X^\top\beta)\}=0.
\]

Let

\[
M=E(XX^\top).
\]

EIF:

\[
D_\beta(O)
=
M^{-1}X(Y-X^\top\beta).
\]

---

### 2.3 Logistic working-regression coefficient

Define \(\beta\) by

\[
E\left[
X\{Y-\operatorname{expit}(X^\top\beta)\}
\right]=0.
\]

Let

\[
p_\beta(X)=\operatorname{expit}(X^\top\beta),
\]

\[
M
=
E\left[
p_\beta(X)\{1-p_\beta(X)\}XX^\top
\right].
\]

EIF:

\[
D_\beta(O)
=
M^{-1}X\{Y-p_\beta(X)\}.
\]

This is the EIF for the population estimating-equation target, not necessarily for a correctly specified parametric model only.

---

### 2.4 General GLM score parameter

If \(\beta\) is defined by

\[
E\{S_\beta(O)\}=0,
\]

let

\[
A=
E\left[
\frac{\partial S_\beta(O)}{\partial \beta^\top}
\right].
\]

Then

\[
D_\beta(O)=-A^{-1}S_\beta(O).
\]

---

### 2.5 Quantile regression coefficient

Define \(\beta_\tau\) by

\[
E\left[
X\{\tau-I(Y\le X^\top\beta_\tau)\}
\right]=0.
\]

Let

\[
M
=
E\left[
f_{Y\mid X}(X^\top\beta_\tau\mid X)XX^\top
\right].
\]

Then

\[
D_{\beta_\tau}(O)
=
M^{-1}X\{\tau-I(Y\le X^\top\beta_\tau)\}.
\]

---

## 3. Missing-data examples

Observed data:

\[
O=(R,RY,X),
\]

where \(R=1\) means \(Y\) is observed.

Assume missing at random:

\[
Y\perp R\mid X,
\]

and positivity:

\[
\pi(X)=P(R=1\mid X)>0.
\]

---

### 3.1 Mean under MAR

Target:

\[
\psi=E(Y).
\]

Define

\[
m(X)=E(Y\mid X).
\]

EIF:

\[
D_\psi(O)
=
\frac{R}{\pi(X)}\{Y-m(X)\}
+
m(X)-\psi.
\]

---

### 3.2 Mean of a transformation under MAR

Target:

\[
\psi=E\{g(Y)\}.
\]

Define

\[
m_g(X)=E\{g(Y)\mid X\}.
\]

EIF:

\[
D_\psi(O)
=
\frac{R}{\pi(X)}
\{g(Y)-m_g(X)\}
+
m_g(X)-\psi.
\]

---

### 3.3 Distribution function under MAR

Target:

\[
F(t)=P(Y\le t).
\]

Define

\[
m_t(X)=P(Y\le t\mid X).
\]

EIF:

\[
D_{F(t)}(O)
=
\frac{R}{\pi(X)}
\{I(Y\le t)-m_t(X)\}
+
m_t(X)-F(t).
\]

---

### 3.4 Quantile under MAR

Target:

\[
q_\tau=F^{-1}(\tau).
\]

Use the EIF for \(F(t)\) at \(t=q_\tau\):

\[
D_{F(q_\tau)}(O)
=
\frac{R}{\pi(X)}
\{I(Y\le q_\tau)-m_{q_\tau}(X)\}
+
m_{q_\tau}(X)-\tau.
\]

Assuming \(f(q_\tau)>0\),

\[
D_{q_\tau}(O)
=
-\frac{D_{F(q_\tau)}(O)}{f(q_\tau)}.
\]

Equivalently,

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

---

## 4. Point-treatment causal examples

Observed data:

\[
O=(Y,A,X),
\]

where \(A\in\{0,1\}\).

Assume consistency, conditional exchangeability, and positivity:

\[
Y=AY(1)+(1-A)Y(0),
\]

\[
(Y(1),Y(0))\perp A\mid X,
\]

\[
0<c<P(A=1\mid X)<1-c.
\]

Define

\[
e(X)=P(A=1\mid X),
\]

\[
m_a(X)=E(Y\mid A=a,X).
\]

---

### 4.1 Mean potential outcome

Target:

\[
\mu_a=E\{Y(a)\}.
\]

Identification:

\[
\mu_a=E\{m_a(X)\}.
\]

EIF:

\[
D_{\mu_a}(O)
=
\frac{I(A=a)}{P(A=a\mid X)}
\{Y-m_a(X)\}
+
m_a(X)-\mu_a.
\]

Special cases:

\[
D_{\mu_1}(O)
=
\frac{A}{e(X)}
\{Y-m_1(X)\}
+
m_1(X)-\mu_1,
\]

\[
D_{\mu_0}(O)
=
\frac{1-A}{1-e(X)}
\{Y-m_0(X)\}
+
m_0(X)-\mu_0.
\]

---

### 4.2 Average treatment effect, ATE

Target:

\[
\psi=E\{Y(1)-Y(0)\}
=
\mu_1-\mu_0.
\]

EIF:

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

### 4.3 Average treatment effect on the treated, ATT

Target:

\[
\psi=E\{Y(1)-Y(0)\mid A=1\}.
\]

Let

\[
p=P(A=1).
\]

Identification:

\[
\psi
=
\frac{E\left[A\{Y-m_0(X)\}\right]}{p}.
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

---

### 4.4 Average treatment effect on the controls, ATC

Target:

\[
\psi=E\{Y(1)-Y(0)\mid A=0\}.
\]

Let

\[
p_0=P(A=0)=1-p.
\]

Identification:

\[
\psi
=
\frac{E\left[(1-A)\{m_1(X)-Y\}\right]}{p_0}.
\]

EIF:

\[
D_\psi(O)
=
\frac{A}{p_0}
\frac{1-e(X)}{e(X)}
\{Y-m_1(X)\}
+
\frac{1-A}{p_0}
\{m_1(X)-Y-\psi\}.
\]

---

### 4.5 Subgroup ATE

Let

\[
G=I(X\in\mathcal G),
\]

and

\[
p_G=P(G=1).
\]

Target:

\[
\psi_{\mathcal G}
=
E\{Y(1)-Y(0)\mid G=1\}.
\]

Define

\[
\tau(X)=m_1(X)-m_0(X).
\]

EIF:

\[
D_{\psi_{\mathcal G}}(O)
=
\frac{G}{p_G}
\left[
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
\tau(X)
-
\psi_{\mathcal G}
\right].
\]

This is for a fixed subgroup. A pointwise CATE at a continuous \(X=x\) is generally not root-\(n\) regular in a fully nonparametric model.

---

### 4.6 Weighted ATE with fixed weights

Let \(w(X)\) be a fixed known function.

Target:

\[
\psi_w
=
\frac{E\{w(X)[m_1(X)-m_0(X)]\}}{E\{w(X)\}}.
\]

Let

\[
\bar w=E\{w(X)\},
\]

\[
\tau(X)=m_1(X)-m_0(X).
\]

EIF:

\[
D_{\psi_w}(O)
=
\frac{w(X)}{\bar w}
\left[
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
\tau(X)
-
\psi_w
\right].
\]

Important: if \(w(X)\) depends on unknown nuisance functions, such as \(w(X)=e(X)\{1-e(X)\}\), additional terms may be needed.

---

### 4.7 Deterministic policy value

Let

\[
d(X)\in\{0,1\}
\]

be a fixed deterministic policy.

Target:

\[
\psi_d=E\{Y(d)\}.
\]

Define

\[
g_d(X)=P(A=d(X)\mid X),
\]

\[
m_d(X)=E\{Y\mid A=d(X),X\}.
\]

EIF:

\[
D_{\psi_d}(O)
=
\frac{I\{A=d(X)\}}{g_d(X)}
\{Y-m_d(X)\}
+
m_d(X)-\psi_d.
\]

---

### 4.8 Policy contrast

For two fixed policies \(d_1,d_0\),

\[
\psi=E\{Y(d_1)-Y(d_0)\}.
\]

EIF:

\[
D_\psi(O)
=
D_{\psi_{d_1}}(O)-D_{\psi_{d_0}}(O).
\]

---

## 5. Binary-outcome causal contrasts

Let

\[
\mu_a=E\{Y(a)\},
\]

with EIF \(D_{\mu_a}\) as above.

---

### 5.1 Risk difference

Target:

\[
\psi=\mu_1-\mu_0.
\]

EIF:

\[
D_\psi=D_{\mu_1}-D_{\mu_0}.
\]

---

### 5.2 Risk ratio

Target:

\[
\psi=\frac{\mu_1}{\mu_0}.
\]

EIF:

\[
D_\psi
=
\frac{D_{\mu_1}-\psi D_{\mu_0}}{\mu_0}.
\]

---

### 5.3 Log risk ratio

Target:

\[
\psi=\log\frac{\mu_1}{\mu_0}.
\]

EIF:

\[
D_\psi
=
\frac{D_{\mu_1}}{\mu_1}
-
\frac{D_{\mu_0}}{\mu_0}.
\]

---

### 5.4 Log odds ratio

Target:

\[
\theta
=
\log
\frac{\mu_1/(1-\mu_1)}
{\mu_0/(1-\mu_0)}.
\]

EIF:

\[
D_\theta
=
\frac{D_{\mu_1}}{\mu_1(1-\mu_1)}
-
\frac{D_{\mu_0}}{\mu_0(1-\mu_0)}.
\]

For the odds ratio itself,

\[
\operatorname{OR}=e^\theta,
\]

\[
D_{\operatorname{OR}}=\operatorname{OR}\,D_\theta.
\]

---

## 6. Causal distribution and quantile examples

### 6.1 Distribution of a potential outcome

Target:

\[
F_a(t)=P\{Y(a)\le t\}.
\]

Define

\[
m_{a,t}(X)=P(Y\le t\mid A=a,X).
\]

EIF:

\[
D_{F_a(t)}(O)
=
\frac{I(A=a)}{P(A=a\mid X)}
\{I(Y\le t)-m_{a,t}(X)\}
+
m_{a,t}(X)-F_a(t).
\]

---

### 6.2 Quantile of a potential outcome

Target:

\[
q_{a,\tau}=F_a^{-1}(\tau).
\]

Assume \(F_a\) has density \(f_a\) and \(f_a(q_{a,\tau})>0\). Then

\[
D_{q_{a,\tau}}(O)
=
-\frac{D_{F_a(q_{a,\tau})}(O)}
{f_a(q_{a,\tau})}.
\]

---

### 6.3 Quantile treatment effect, QTE

Target:

\[
\psi_\tau=q_{1,\tau}-q_{0,\tau}.
\]

EIF:

\[
D_{\psi_\tau}(O)
=
D_{q_{1,\tau}}(O)
-
D_{q_{0,\tau}}(O).
\]

---

## 7. Instrumental variable examples

Observed data:

\[
O=(Y,A,Z,X),
\]

where \(Z\in\{0,1\}\) is an instrument.

Define

\[
q(X)=P(Z=1\mid X),
\]

\[
m^Y_z(X)=E(Y\mid Z=z,X),
\]

\[
m^A_z(X)=E(A\mid Z=z,X).
\]

The following formulas give the EIF for covariate-adjusted Wald-type functionals. Interpretation as LATE requires the usual IV assumptions.

---

### 7.1 Wald numerator

Target:

\[
\nu_Y=E\{m^Y_1(X)-m^Y_0(X)\}.
\]

EIF:

\[
D_{\nu_Y}(O)
=
\frac{Z}{q(X)}
\{Y-m^Y_1(X)\}
-
\frac{1-Z}{1-q(X)}
\{Y-m^Y_0(X)\}
+
m^Y_1(X)-m^Y_0(X)-\nu_Y.
\]

---

### 7.2 Wald denominator

Target:

\[
\nu_A=E\{m^A_1(X)-m^A_0(X)\}.
\]

EIF:

\[
D_{\nu_A}(O)
=
\frac{Z}{q(X)}
\{A-m^A_1(X)\}
-
\frac{1-Z}{1-q(X)}
\{A-m^A_0(X)\}
+
m^A_1(X)-m^A_0(X)-\nu_A.
\]

---

### 7.3 Wald ratio / LATE estimand

Target:

\[
\psi=\frac{\nu_Y}{\nu_A}.
\]

EIF:

\[
D_\psi(O)
=
\frac{D_{\nu_Y}(O)-\psi D_{\nu_A}(O)}{\nu_A}.
\]

---

## 8. Treatment with missing outcome

Observed data:

\[
O=(R,RY,A,X),
\]

where \(R=1\) means \(Y\) is observed.

Assume

\[
Y\perp R\mid A,X.
\]

Define

\[
e(X)=P(A=1\mid X),
\]

\[
\pi_a(X)=P(R=1\mid A=a,X),
\]

\[
m_a(X)=E(Y\mid A=a,R=1,X).
\]

---

### 8.1 Mean potential outcome with missing outcome

Target:

\[
\mu_a=E\{Y(a)\}.
\]

EIF:

\[
D_{\mu_a}(O)
=
\frac{I(A=a)R}
{P(A=a\mid X)\pi_a(X)}
\{Y-m_a(X)\}
+
m_a(X)-\mu_a.
\]

---

### 8.2 ATE with missing outcome

Target:

\[
\psi=\mu_1-\mu_0.
\]

EIF:

\[
D_\psi(O)
=
\frac{AR}{e(X)\pi_1(X)}
\{Y-m_1(X)\}
-
\frac{(1-A)R}{\{1-e(X)\}\pi_0(X)}
\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

---

## 9. Longitudinal treatment regime

Observed data:

\[
O=(L_0,A_0,L_1,A_1,\ldots,L_K,A_K,Y).
\]

Let \(d=(d_0,\ldots,d_K)\) be a fixed dynamic treatment rule.

Define pre-treatment history at time \(t\):

\[
H_t=(L_0,A_0,L_1,\ldots,A_{t-1},L_t).
\]

Define

\[
g_t(H_t)=P\{A_t=d_t(H_t)\mid H_t\}.
\]

Define cumulative inverse-probability weight

\[
W_t^d
=
\prod_{s=0}^t
\frac{I\{A_s=d_s(H_s)\}}{g_s(H_s)}.
\]

Let

\[
Q_{K+1}=Y,
\]

and recursively define

\[
Q_t(H_t)
=
E\{Q_{t+1}(H_{t+1})\mid H_t,A_t=d_t(H_t)\},
\qquad t=K,\ldots,0.
\]

The target is

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

This is the standard sequential-regression / longitudinal AIPW / TMLE structure.

---

## 10. Survival examples

### 10.1 Survival probability without censoring

Let \(T\) be an event time.

Target:

\[
S(t)=P(T>t).
\]

EIF:

\[
D_{S(t)}(O)=I(T>t)-S(t).
\]

---

### 10.2 Restricted mean survival time without censoring

Target:

\[
\operatorname{RMST}(\tau)
=
E\{\min(T,\tau)\}
=
\int_0^\tau S(t)\,dt.
\]

Since

\[
\min(T,\tau)=\int_0^\tau I(T>t)\,dt,
\]

the EIF is

\[
D_{\operatorname{RMST}(\tau)}(O)
=
\min(T,\tau)-\operatorname{RMST}(\tau).
\]

Equivalently,

\[
D_{\operatorname{RMST}(\tau)}(O)
=
\int_0^\tau
\{I(T>t)-S(t)\}
\,dt.
\]

---

### 10.3 Survival probability with right censoring: status-at-\(t\) MAR representation

Let

\[
\tilde T=\min(T,C),
\qquad
\Delta=I(T\le C).
\]

For a fixed \(t\), define

\[
Y_t=I(T>t).
\]

The survival status \(Y_t\) is observed if

\[
R_t=I(\tilde T\ge t \ \text{or}\ \Delta=1,\tilde T\le t).
\]

That is, either the subject is known to be event-free at \(t\), or the event has already occurred by \(t\).

Assume conditional independent censoring such that

\[
Y_t\perp R_t\mid X.
\]

Define

\[
\pi_t(X)=P(R_t=1\mid X),
\]

\[
m_t(X)=E(Y_t\mid X).
\]

Then a useful EIF under this status-at-\(t\) MAR representation is

\[
D_{S(t)}(O)
=
\frac{R_t}{\pi_t(X)}
\{Y_t-m_t(X)\}
+
m_t(X)-S(t).
\]

Note: fully efficient right-censoring EIFs are often written using counting-process martingales. This status-at-\(t\) expression is useful for implementation and intuition, but one should check the exact censoring model when using it for formal efficiency claims.

---

### 10.4 Causal survival without censoring

Target:

\[
S_a(t)=P\{T(a)>t\}.
\]

Define

\[
m_{a,t}(X)=P(T>t\mid A=a,X).
\]

EIF:

\[
D_{S_a(t)}(O)
=
\frac{I(A=a)}{P(A=a\mid X)}
\{I(T>t)-m_{a,t}(X)\}
+
m_{a,t}(X)-S_a(t).
\]

---

## 11. Continuous exposure examples

Observed data:

\[
O=(Y,A,X),
\]

where \(A\) may be continuous.

---

### 11.1 Stochastic intervention mean with known intervention density

Let \(g(a\mid X)\) be the observed exposure density and \(g^\star(a\mid X)\) be a fixed known intervention density.

Define

\[
m(a,X)=E(Y\mid A=a,X).
\]

Target:

\[
\psi
=
E_X
\left[
\int m(a,X)g^\star(a\mid X)\,da
\right].
\]

EIF:

\[
D_\psi(O)
=
\frac{g^\star(A\mid X)}{g(A\mid X)}
\{Y-m(A,X)\}
+
\int m(a,X)g^\star(a\mid X)\,da
-
\psi.
\]

This requires positivity:

\[
g(a\mid X)>0
\quad
\text{whenever}
\quad
g^\star(a\mid X)>0.
\]

---

### 11.2 Modified treatment policy

For a modified treatment policy

\[
A^\star=d(A,X),
\]

the target is often

\[
\psi=E\{Y(d(A,X))\}.
\]

The EIF depends on the transformation \(d\), its inverse map, and possible Jacobian terms. The general structure is often

\[
D_\psi
=
\text{density-ratio residual correction}
+
\text{plug-in regression part}
-
\psi,
\]

but this should be derived for the specific policy rather than copied from a generic template.

---

## 12. Stochastic mediation-style examples

Observed data:

\[
O=(Y,A,M,X),
\]

where \(M\) is a mediator.

---

### 12.1 Fixed mediator intervention distribution

Let

\[
m_Y(a,m,X)=E(Y\mid A=a,M=m,X).
\]

Let \(q(m\mid X)\) be a fixed known intervention distribution for \(M\). Define

\[
e_a(X)=P(A=a\mid X),
\]

\[
p_M(m\mid a,X)=p(M=m\mid A=a,X).
\]

Target:

\[
\psi
=
E_X
\left[
\int m_Y(a,m,X)q(m\mid X)\,dm
\right].
\]

EIF:

\[
D_\psi(O)
=
\frac{I(A=a)q(M\mid X)}
{e_a(X)p_M(M\mid a,X)}
\{Y-m_Y(a,M,X)\}
+
\int m_Y(a,m,X)q(m\mid X)\,dm
-
\psi.
\]

Important: if \(q(m\mid X)\) is itself a functional of the observed law, as in natural direct or indirect effect parameters, additional EIF components are needed.

---

## 13. Two-phase sampling and cluster examples

### 13.1 Two-phase sampling mean

Suppose \(Y\) is only measured in a phase-2 sample.

Observed data:

\[
O=(R,RY,V),
\]

where \(V\) is phase-1 information.

Target:

\[
\psi=E(Y).
\]

Define

\[
\pi(V)=P(R=1\mid V),
\]

\[
m(V)=E(Y\mid V).
\]

EIF:

\[
D_\psi(O)
=
\frac{R}{\pi(V)}
\{Y-m(V)\}
+
m(V)-\psi.
\]

This is algebraically the same as the MAR missing-data mean EIF.

---

### 13.2 Cluster-level mean with iid clusters

Suppose the iid unit is a cluster:

\[
O_i=(Y_{i1},\ldots,Y_{im_i},X_i).
\]

Target:

\[
\psi
=
E\left[
\frac{1}{m_i}
\sum_{j=1}^{m_i}Y_{ij}
\right].
\]

Let

\[
\bar Y_i=\frac{1}{m_i}\sum_{j=1}^{m_i}Y_{ij}.
\]

EIF at the cluster level:

\[
D_\psi(O_i)=\bar Y_i-\psi.
\]

The important point is that the iid unit is the cluster, not the individual observation.

---

## 14. Smoothed and nonregular examples

### 14.1 Smoothed density at a point

The unsmoothed density \(p_Y(y_0)\) is generally not a regular root-\(n\) estimable parameter in a fully nonparametric model.

For a fixed bandwidth \(h>0\), define the smoothed target

\[
\psi_h=E\{K_h(Y-y_0)\}.
\]

EIF:

\[
D_{\psi_h}(O)=K_h(Y-y_0)-\psi_h.
\]

If \(h\to 0\), the problem becomes nonregular and requires separate smoothing-rate analysis.

---

### 14.2 Pointwise CATE with continuous covariates

Target:

\[
\tau(x)=E\{Y(1)-Y(0)\mid X=x\}.
\]

When \(X\) is continuous, this is generally not a regular root-\(n\) target in a fully nonparametric model.

Possible regular alternatives:

\[
E\{Y(1)-Y(0)\mid X\in\mathcal G\},
\]

or a kernel-smoothed CATE target.

---

### 14.3 Maximum of a regression function

Target:

\[
\max_x m(x).
\]

This is generally nonregular, especially if the maximizer is not unique or lies on a boundary. Do not apply a standard EIF template without additional assumptions.

---

## 15. Implementation patterns

### 15.1 Generic pseudo-outcome pattern

Many EIF-based estimators are implemented as:

```python
pseudo_outcome = residual_correction + plug_in_part

psi_hat = np.mean(pseudo_outcome)
phi_hat = pseudo_outcome - psi_hat
se_hat = np.std(phi_hat, ddof=1) / np.sqrt(n)
```

---

### 15.2 ATE implementation

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

    return psi_hat, se_hat, phi_hat
```

---

### 15.3 Missing-data mean implementation

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

    return psi_hat, se_hat, phi_hat
```

---

### 15.4 Mean potential outcome implementation

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

    return psi_hat, se_hat, phi_hat
```

---

## 16. Final checklist

Before using an EIF formula, verify:

- [ ] The observed-data structure matches the formula.
- [ ] The target parameter matches the formula.
- [ ] The nuisance functions are correctly defined.
- [ ] The target is identified under the stated assumptions.
- [ ] Positivity holds for all inverse-probability terms.
- [ ] The EIF has empirical mean close to zero after plug-in estimation.
- [ ] The estimated standard error is based on the empirical variance of the EIF.
- [ ] Cross-fitting is used for flexible nuisance estimation.
- [ ] For ratio parameters, the denominator is bounded away from zero.
- [ ] For quantiles, the density at the quantile is positive.
- [ ] For censoring/survival problems, the censoring model matches the EIF form.
- [ ] Nonregular targets are not treated as standard root-\(n\) parameters without smoothing or extra assumptions.
