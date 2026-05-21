# Worked derivation: Restricted Moment Model

This note gives a worked semiparametric efficiency derivation for the restricted moment model

\[
Y=m(X,\beta)+\varepsilon,
\qquad
E(\varepsilon\mid X)=0.
\]

This is a core projection example. It is simpler than the partially linear single index model and is useful as a template for restricted conditional mean models.

---

## 1. Model and target

Observed data:

\[
O=(Y,X).
\]

Let

\[
\varepsilon=Y-m(X,\beta),
\qquad
\dot m_\beta(X)=\frac{\partial m(X,\beta)}{\partial\beta}.
\]

The parameter of interest is the finite-dimensional parameter \(\beta\), defined by the conditional mean restriction

\[
E\{Y-m(X,\beta)\mid X\}=0.
\]

The joint density can be written as

\[
p(x,y)
=
p_X(x)\eta(\varepsilon,x),
\qquad
\varepsilon=y-m(x,\beta),
\]

with the conditional mean restriction

\[
E(\varepsilon\mid X)=0.
\]

---

## 2. Nuisance tangent spaces

The nuisance tangent space has two parts.

### 2.1 Covariate-law tangent space

\[
\Lambda_1
=
\{a(X):E\{a(X)\}=0\}.
\]

### 2.2 Conditional error-law tangent space

The conditional error law is otherwise unrestricted, but perturbations must preserve:

1. conditional density normalization;
2. conditional mean zero.

Thus

\[
\Lambda_2
=
\left\{
a(\varepsilon,X):
E(a\mid X)=0,\,
E(a\varepsilon\mid X)=0
\right\}.
\]

The nuisance tangent space is

\[
\Lambda=\Lambda_1\oplus\Lambda_2.
\]

---

## 3. Orthocomplement of the nuisance tangent space

Since functions in \(\Lambda_1\) depend only on \(X\), any function orthogonal to \(\Lambda_1\) must have conditional mean zero given \(X\).

Since functions in \(\Lambda_2\) are all conditional error perturbations orthogonal to both \(1\) and \(\varepsilon\), the orthocomplement inside the conditional error space is spanned by \(\varepsilon\).

Therefore

\[
\Lambda^\perp
=
\{a(X)\varepsilon:a \text{ square-integrable}\}.
\]

This is the key geometric fact: any efficient score for \(\beta\) must be of the form

\[
\varepsilon a(X).
\]

---

## 4. Raw score for \(\beta\)

Let

\[
\ell_\varepsilon(\varepsilon,X)
=
\frac{\partial}{\partial\varepsilon}\log\eta(\varepsilon,X),
\qquad
\rho(\varepsilon,X)=-\ell_\varepsilon(\varepsilon,X).
\]

Changing \(\beta\) shifts the residual by

\[
\frac{\partial\varepsilon}{\partial\beta}
=
-\dot m_\beta(X).
\]

Therefore the raw score for \(\beta\) is

\[
S_\beta
=
\rho(\varepsilon,X)\dot m_\beta(X)
=
-\ell_\varepsilon(\varepsilon,X)\dot m_\beta(X).
\]

Equivalently, if the conditional error density is denoted by \(\eta_2(\varepsilon,x)\),

\[
S_\beta
=
-
\frac{
\eta_{21}'\{Y-m(X,\beta),X\}
}{
\eta_2\{Y-m(X,\beta),X\}
}
\dot m_\beta(X).
\]

This raw score is not generally efficient because it is not guaranteed to lie in \(\Lambda^\perp\).

---

## 5. Projection to the orthocomplement

The efficient score must be the projection of \(S_\beta\) onto

\[
\Lambda^\perp=\{a(X)\varepsilon\}.
\]

Projecting \(\rho(\varepsilon,X)\dot m_\beta(X)\) onto the span of \(\varepsilon\) conditionally on \(X\) gives

\[
E\{\rho(\varepsilon,X)\varepsilon\mid X\}
\sigma^{-2}(X)\varepsilon\dot m_\beta(X),
\]

where

\[
\sigma^2(X)=E(\varepsilon^2\mid X).
\]

Under standard regularity and integration-by-parts,

\[
E\{\rho(\varepsilon,X)\varepsilon\mid X\}=1.
\]

Therefore the efficient score is

\[
\boxed{
S_{\mathrm{eff}}(O)
=
\varepsilon\sigma^{-2}(X)\dot m_\beta(X).
}
\]

---

## 6. Efficient information and EIF

The efficient information matrix is

\[
I_{\mathrm{eff}}
=
E\{S_{\mathrm{eff}}S_{\mathrm{eff}}^\top\}
=
E\left[
\sigma^{-2}(X)\dot m_\beta(X)\dot m_\beta(X)^\top
\right].
\]

If \(I_{\mathrm{eff}}\) is nonsingular, the EIF for \(\beta\) is

\[
\boxed{
D_\beta(O)
=
I_{\mathrm{eff}}^{-1}
S_{\mathrm{eff}}(O)
=
I_{\mathrm{eff}}^{-1}
\sigma^{-2}(X)\dot m_\beta(X)\{Y-m(X,\beta)\}.
}
\]

---

## 7. Efficient estimating equation

The efficient estimating equation is

\[
\sum_{i=1}^n
\{Y_i-m(X_i,\beta)\}
\sigma^{-2}(X_i)
\dot m_\beta(X_i)
=0.
\]

This is the sample analogue of setting the efficient score mean to zero.

Any equation of the form

\[
\sum_{i=1}^n
\{Y_i-m(X_i,\beta)\}a(X_i)=0
\]

can give a regular asymptotically linear estimator under suitable conditions, but the efficient choice is

\[
a(X)=\sigma^{-2}(X)\dot m_\beta(X).
\]

---

## 8. Verification

### Mean zero

\[
E(S_{\mathrm{eff}}\mid X)
=
\sigma^{-2}(X)\dot m_\beta(X)E(\varepsilon\mid X)
=0.
\]

### Orthogonality to \(\Lambda_1\)

For any \(a(X)\in\Lambda_1\),

\[
E\{S_{\mathrm{eff}}a(X)\}
=
E[a(X)E(S_{\mathrm{eff}}\mid X)]
=0.
\]

### Orthogonality to \(\Lambda_2\)

For any \(a(\varepsilon,X)\in\Lambda_2\),

\[
E(a\varepsilon\mid X)=0.
\]

Thus

\[
E\{S_{\mathrm{eff}}a\}
=
E\left[
\sigma^{-2}(X)\dot m_\beta(X)E(\varepsilon a\mid X)
\right]
=0.
\]

Hence \(S_{\mathrm{eff}}\in\Lambda^\perp\).

---

## 9. Regularity assumptions and status

The display above is the semiparametric EIF under the restricted moment model if:

- \(m(x,\beta)\) is differentiable in \(\beta\);
- the conditional error density is regular enough for integration by parts;
- \(E(\varepsilon\mid X)=0\) holds at the true \(\beta\);
- \(0<\sigma^2(X)<\infty\) almost surely, with enough integrability for the information matrix;
- \(I_{\mathrm{eff}}\) is nonsingular;
- the tangent space is the closure of \(\Lambda_1\oplus\Lambda_2\).

If these conditions are not established, the score remains a candidate efficient score until regularity and tangent-space closure are verified.

