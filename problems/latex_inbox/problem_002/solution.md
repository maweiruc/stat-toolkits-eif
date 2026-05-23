# Problem 002 Solution: Partially Linear Single Index Model

## 1. Normalized Problem

Observed data:

\[
O=(Y,X,Z),
\qquad W=(X,Z).
\]

The model is

\[
Y=X^\top\beta+g(Z^\top\alpha)+\varepsilon,
\qquad
E(\varepsilon\mid X,Z)=0.
\]

Let

\[
T=Z^\top\alpha,
\qquad
\mu(W)=X^\top\beta+g(T),
\qquad
\varepsilon=Y-\mu(W).
\]

Because \(g(Z^\top\alpha)\) is invariant under scale changes of \(\alpha\),
the parameter \(\alpha\) must be normalized. The problem statement uses
\(\|\alpha\|_2=1\) and \(\alpha_1>0\). For derivation it is cleanest to use a
local unconstrained parameterization

\[
\alpha=\alpha(\gamma),
\qquad
\gamma\in\mathbb R^{q-1},
\]

and define

\[
\vartheta=(\beta^\top,\gamma^\top)^\top.
\]

Let

\[
J_\gamma=\frac{\partial \alpha(\gamma)}{\partial\gamma^\top},
\qquad
Z_\gamma=J_\gamma^\top Z.
\]

The EIF below is first for the local parameter
\(\vartheta=(\beta^\top,\gamma^\top)^\top\). The IF for constrained
\(\alpha\) is obtained by \(D_\alpha=J_\gamma D_\gamma\).

## 2. Identification and Assumptions

The finite-dimensional parameter is identified under the normalization of
\(\alpha\), sufficient variation in \(X,Z\), and nonsingularity of the
efficient information matrix.

Regularity assumptions:

1. \(g\) is smooth enough for \(g'(T)\) to exist.
2. The local parameterization \(\alpha=\alpha(\gamma)\) is valid near the true
   value.
3. The conditional error density is regular enough for integration by parts.
4. \(E(\varepsilon\mid X,Z)=0\).
5. \(0<\sigma^2(W)<\infty\), where
   \[
   \sigma^2(W)=E(\varepsilon^2\mid W).
   \]
6. Weighted conditional expectations given \(T=Z^\top\alpha\) exist.
7. The efficient information matrix is nonsingular.
8. The nuisance tangent space is closed, or all projections are interpreted in
   its \(L_2(P)\) closure.

## 3. Nuisance Functions

The density factorization is

\[
p(o)=p_{X,Z}(x,z)\eta(\varepsilon,x,z),
\qquad
\varepsilon=y-x^\top\beta-g(z^\top\alpha).
\]

The nuisance functions are:

- the joint law \(p_{X,Z}\);
- the conditional error density \(\eta(\varepsilon,x,z)\), subject to
  \(E(\varepsilon\mid X,Z)=0\);
- the unknown smooth link function \(g\);
- the conditional variance \(\sigma^2(W)\), which enters the efficient score.

## 4. Tangent Spaces

The covariate-law tangent space is

\[
\Lambda_{X,Z}
=
\{a(X,Z):E(a(X,Z))=0\}.
\]

The conditional error-law tangent space is

\[
\Lambda_{\varepsilon\mid X,Z}
=
\left\{
a(\varepsilon,X,Z):
E(a\mid X,Z)=0,\,
E(a\varepsilon\mid X,Z)=0
\right\}.
\]

The unknown link \(g\) generates nuisance scores of the form

\[
\rho(\varepsilon,W)a(T),
\]

where

\[
\rho(\varepsilon,W)
=
-\frac{\partial}{\partial\varepsilon}\log\eta(\varepsilon,W).
\]

After projecting away the conditional error-law nuisance, this space is
represented as

\[
\widetilde\Lambda_g
=
\{\varepsilon\sigma^{-2}(W)a(T):a\text{ square-integrable}\}.
\]

Thus the relevant nuisance space is

\[
\Lambda
=
\Lambda_{X,Z}
\oplus
\Lambda_{\varepsilon\mid X,Z}
\oplus
\widetilde\Lambda_g.
\]

## 5. Raw Scores

For the local parameter
\(\vartheta=(\beta^\top,\gamma^\top)^\top\), define

\[
H(W)
=
\begin{pmatrix}
H_\beta(W)\\
H_\gamma(W)
\end{pmatrix}
=
\begin{pmatrix}
X\\
g'(T)Z_\gamma
\end{pmatrix}.
\]

The raw scores are

\[
S_\beta=\rho(\varepsilon,W)X,
\]

and

\[
S_\gamma=\rho(\varepsilon,W)g'(T)Z_\gamma.
\]

Equivalently,

\[
S_\vartheta=\rho(\varepsilon,W)H(W).
\]

These are candidate scores, not yet efficient scores, because they still
contain nuisance components from the error-law shape and the unknown \(g\).

## 6. Projection Away from Conditional Error Shape

The orthocomplement of
\(\Lambda_{\varepsilon\mid X,Z}\) inside the conditional error score space is
spanned by \(\varepsilon\). Under integration by parts,

\[
E\{\rho(\varepsilon,W)\varepsilon\mid W\}=1.
\]

Therefore the raw score projects to

\[
S_{\vartheta,0}(O)
=
\varepsilon\sigma^{-2}(W)H(W).
\]

This is a valid intermediate score, but not yet the efficient score because it
may still have a component in \(\widetilde\Lambda_g\).

## 7. Projection Away from the Unknown Link \(g\)

The remaining nuisance space is

\[
\widetilde\Lambda_g
=
\{\varepsilon\sigma^{-2}(W)a(T)\}.
\]

Project \(H(W)\) onto functions of \(T\) using the weighted inner product

\[
\langle u,v\rangle_w
=
E\{\sigma^{-2}(W)u(W)v(W)^\top\}.
\]

The weighted projection is

\[
\Pi(H\mid T)
=
\frac{
E\{\sigma^{-2}(W)H(W)\mid T\}
}{
E\{\sigma^{-2}(W)\mid T\}
}.
\]

Define

\[
H^\perp(W)=H(W)-\Pi(H\mid T).
\]

Then

\[
E\{\sigma^{-2}(W)H^\perp(W)\mid T\}=0,
\]

which gives orthogonality to every link-function nuisance direction
\(\varepsilon\sigma^{-2}(W)a(T)\).

## 8. Efficient Score

The efficient score for \(\vartheta\) is

\[
\boxed{
S_{\vartheta,\mathrm{eff}}(O)
=
\varepsilon\sigma^{-2}(W)H^\perp(W).
}
\]

Blockwise,

\[
S_{\beta,\mathrm{eff}}
=
\varepsilon\sigma^{-2}(X,Z)
\left[
X
-
\frac{
E\{\sigma^{-2}(X,Z)X\mid Z^\top\alpha\}
}{
E\{\sigma^{-2}(X,Z)\mid Z^\top\alpha\}
}
\right],
\]

and

\[
S_{\gamma,\mathrm{eff}}
=
\varepsilon g'(Z^\top\alpha)\sigma^{-2}(X,Z)
\left[
Z_\gamma
-
\frac{
E\{\sigma^{-2}(X,Z)Z_\gamma\mid Z^\top\alpha\}
}{
E\{\sigma^{-2}(X,Z)\mid Z^\top\alpha\}
}
\right].
\]

Under a delete-one-component parameterization, \(Z_\gamma\) is the appropriate
Jacobian-adjusted version of \(Z_{-1}\).

## 9. Efficient Information and EIF

The efficient information matrix is

\[
I_{\mathrm{eff}}
=
E\{S_{\vartheta,\mathrm{eff}}S_{\vartheta,\mathrm{eff}}^\top\}
=
E\left[
\sigma^{-2}(W)H^\perp(W)H^\perp(W)^\top
\right].
\]

If \(I_{\mathrm{eff}}\) is nonsingular, the efficient influence function for
the local parameter \(\vartheta\) is

\[
\boxed{
D_\vartheta(O)
=
I_{\mathrm{eff}}^{-1}S_{\vartheta,\mathrm{eff}}(O)
=
I_{\mathrm{eff}}^{-1}
\varepsilon\sigma^{-2}(W)H^\perp(W).
}
\]

The \(\beta\)-block of \(D_\vartheta\) is the EIF for \(\beta\) jointly
estimated with \(\gamma\). The \(\gamma\)-block maps to the constrained
\(\alpha\) scale by

\[
\boxed{
D_\alpha(O)=J_\gamma D_\gamma(O).
}
\]

For the unit-norm constraint, this implies

\[
\alpha^\top D_\alpha(O)=0,
\]

so the IF for \(\alpha\) lies in the tangent space of the constraint.

Status:

```text
derived and verified under stated assumptions
```

## 10. Homoskedastic Simplification

If

\[
\sigma^2(W)\equiv\sigma^2,
\]

then

\[
\Pi(H\mid T)=E(H\mid T),
\]

and

\[
H^\perp(W)=H(W)-E(H\mid T).
\]

Thus

\[
S_{\vartheta,\mathrm{eff}}
=
\varepsilon\sigma^{-2}\{H(W)-E(H\mid T)\}.
\]

## 11. Verification

### Mean Zero

\[
E\{S_{\vartheta,\mathrm{eff}}\mid W\}
=
\sigma^{-2}(W)H^\perp(W)E(\varepsilon\mid W)
=0.
\]

Therefore \(E(S_{\vartheta,\mathrm{eff}})=0\) and \(E(D_\vartheta)=0\).

### Orthogonality to \(\Lambda_{X,Z}\)

Since

\[
E(S_{\vartheta,\mathrm{eff}}\mid W)=0,
\]

the efficient score is orthogonal to every \(a(X,Z)\in\Lambda_{X,Z}\).

### Orthogonality to \(\Lambda_{\varepsilon\mid X,Z}\)

For any \(a\in\Lambda_{\varepsilon\mid X,Z}\),

\[
E(a\mid W)=0,
\qquad
E(a\varepsilon\mid W)=0.
\]

Thus

\[
E\{S_{\vartheta,\mathrm{eff}}a\}
=
E\left[
\sigma^{-2}(W)H^\perp(W)E(\varepsilon a\mid W)
\right]
=0.
\]

### Orthogonality to \(\widetilde\Lambda_g\)

For any \(b(T)\),

\[
\begin{aligned}
&E\left[
\varepsilon\sigma^{-2}(W)H^\perp(W)
\cdot
\varepsilon\sigma^{-2}(W)b(T)
\right]\\
&\qquad
=
E\left[
b(T)E\{\sigma^{-2}(W)H^\perp(W)\mid T\}
\right]
=0.
\end{aligned}
\]

This is exactly the weighted projection condition.

### Pathwise Derivative Identity

The raw score for \(\vartheta\) is first projected away from the conditional
error-law nuisance and then away from the unknown-\(g\) nuisance. Hence
\(S_{\vartheta,\mathrm{eff}}\) is the canonical score for the finite-dimensional
local parameter. The canonical gradient is
\(D_\vartheta=I_{\mathrm{eff}}^{-1}S_{\vartheta,\mathrm{eff}}\), so for every
regular score \(S\) in the model tangent space,

\[
\dot\vartheta(S)=E\{D_\vartheta(O)S(O)\}.
\]

## 12. Warnings

- A naive estimating equation using \(\varepsilon X\) or
  \(\varepsilon g'(T)Z_\gamma\) is generally not efficient.
- The projection onto functions of \(T=Z^\top\alpha\) is essential because
  \(g\) is unknown.
- The EIF is for the local unconstrained parameter
  \(\vartheta=(\beta^\top,\gamma^\top)^\top\). The constrained \(\alpha\) IF
  must be mapped using \(J_\gamma\).
- If \(I_{\mathrm{eff}}\) is singular, if \(g'\) is not well defined, or if the
  weighted conditional projections do not exist, the efficient score should be
  treated as candidate until those conditions are verified.
