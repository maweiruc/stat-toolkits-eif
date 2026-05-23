# Semiparametric 中 influence function 的一般求法

核心思想是：**influence function 是目标泛函对分布扰动的 Gateaux derivative / pathwise derivative 的 Riesz representer**。在 semiparametric 问题里，我们通常真正想要的是 **efficient influence function, EIF**，也叫 **canonical gradient**。

---

## 1. 基本定义

设观测数据为

\[
O \sim P,\qquad P \in \mathcal M,
\]

目标参数为一个分布泛函

\[
\psi(P).
\]

一个函数 \(\phi_P(O)\) 是 \(\psi(P)\) 的 influence function，如果它满足：

\[
E_P\{\phi_P(O)\}=0,
\]

并且对任意经过 \(P\) 的一维正则 parametric submodel \(P_\varepsilon\)，其 score 为

\[
S(O)=\left.\frac{\partial}{\partial \varepsilon}\log p_\varepsilon(O)\right|_{\varepsilon=0},
\]

都有

\[
\left.\frac{\partial}{\partial \varepsilon}\psi(P_\varepsilon)\right|_{\varepsilon=0}
=
E_P\{\phi_P(O)S(O)\}.
\]

这就是最核心的公式。

直观地说：

\[
\text{pathwise derivative}
=
\text{inner product of IF and score}.
\]

也就是说，IF 是目标参数相对于分布扰动的梯度。

---

## 2. 一般性原则

求 semiparametric influence function 时，可以记住下面几个原则。

### 原则 1：先把目标写成 observable law 的泛函

比如 ATE：

\[
\psi(P)=E\{m_1(X)-m_0(X)\},
\]

其中

\[
m_a(X)=E(Y\mid A=a,X).
\]

这一步非常重要。不要一开始就对 estimator 求导，而是对 population-level target functional 求导。

---

### 原则 2：把数据分布分解成若干条件分布

例如对 treatment effect 问题，观测数据为

\[
O=(Y,A,X).
\]

可以写成

\[
p(o)=p(y\mid a,x)p(a\mid x)p(x).
\]

对应三个部分：

\[
p(y\mid a,x),\qquad p(a\mid x),\qquad p(x).
\]

一般来说，score 可以分解为：

\[
S(O)
=
S_Y(Y\mid A,X)+S_A(A\mid X)+S_X(X),
\]

其中

\[
E\{S_Y\mid A,X\}=0,
\]

\[
E\{S_A\mid X\}=0,
\]

\[
E(S_X)=0.
\]

然后分别看目标参数对每一部分分布扰动的导数。

---

### 原则 3：每个分布部分对应 EIF 的一个 component

很多 EIF 都可以理解为几个部分的和：

\[
\phi(O)
=
\phi_Y(O)+\phi_A(O)+\phi_X(O).
\]

例如 ATE 的 EIF 是：

\[
\phi(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

其中：

\[
e(X)=P(A=1\mid X).
\]

这里三个部分的含义是：

\[
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
\]

来自 outcome regression \(p(y\mid a,x)\) 的扰动；

\[
m_1(X)-m_0(X)-\psi
\]

来自 covariate distribution \(p(x)\) 的扰动；

而 \(p(a\mid x)\) 对 ATE 目标本身没有直接贡献，所以没有单独的 treatment mechanism residual 项。propensity score \(e(X)\) 出现在 EIF 中，是因为它把 \(Y\mid A=a,X\) 的 conditional perturbation 转换成 observed-data expression。

---

### 原则 4：EIF 必须 mean zero

最后一定要检查：

\[
E\{\phi(O)\}=0.
\]

如果不是 mean zero，通常要减去它的 expectation。

很多时候 EIF 形式中最后的

\[
-\psi
\]

就是为了保证 mean zero。

---

### 原则 5：在 restricted semiparametric model 中要投影

如果模型是 nonparametric model，那么 tangent space 通常是整个 \(L_0^2(P)\)，EIF 就是唯一的 canonical gradient。

但如果模型有限制，比如：

\[
E(Y\mid X)=\beta^\top X,
\]

或者 treatment model 被限制为 logistic regression，那么 tangent space 变小。此时需要把 nonparametric IF 投影到该 tangent space 上。

一般原则是：

\[
\phi_{\text{EIF}}
=
\Pi_{\mathcal T}\phi_{\text{full}},
\]

其中 \(\mathcal T\) 是 semiparametric model 的 tangent space。

如果 coding agent 不处理 restricted model，可以先默认使用 nonparametric model 下的 EIF。

---

## 3. 求 EIF 的通用步骤

下面是最适合交给 coding agent 的工作流。

---

## Step 0：明确输入

让 coding agent 先明确四件事：

1. 观测数据结构  
2. 统计模型假设  
3. 目标参数  
4. 是否需要 efficient IF 还是任意 IF  

例如：

```text
Observed data:
O = (Y, A, X)

Assumptions:
Consistency, ignorability, positivity.

Target:
psi = E[m1(X) - m0(X)],
where ma(X) = E[Y | A=a, X].

Model:
Nonparametric observed-data model.
```

---

## Step 1：把目标参数写成 nuisance functions 的形式

例如 ATE：

\[
\psi
=
E_X\{m_1(X)-m_0(X)\}.
\]

这里 nuisance functions 是：

\[
m_1(x)=E(Y\mid A=1,X=x),
\]

\[
m_0(x)=E(Y\mid A=0,X=x),
\]

\[
e(x)=P(A=1\mid X=x).
\]

尽管 \(e(x)\) 不直接出现在 target 中，但它会出现在 observed-data EIF 中。

---

## Step 2：写出 likelihood factorization

例如：

\[
p(o)
=
p(y\mid a,x)p(a\mid x)p(x).
\]

然后写出 score decomposition：

\[
S(O)
=
S_Y(Y\mid A,X)
+
S_A(A\mid X)
+
S_X(X).
\]

并标注条件 mean-zero 约束：

\[
E(S_Y\mid A,X)=0,
\]

\[
E(S_A\mid X)=0,
\]

\[
E(S_X)=0.
\]

这一步对 coding agent 很重要，因为它决定 derivative 该怎么分组。

---

## Step 3：构造 parametric submodel

理论上，需要对每个分布成分构造扰动：

\[
p_\varepsilon(o)
=
p_\varepsilon(y\mid a,x)
p_\varepsilon(a\mid x)
p_\varepsilon(x).
\]

对应 score：

\[
S_\varepsilon(O)
=
S_Y+S_A+S_X.
\]

实际推导时不需要指定具体 \(p_\varepsilon\)，只需要使用 score 的性质即可。

如果要做数值验证，可以用 exponential tilting：

\[
p_\varepsilon(o)
=
\frac{\exp\{\varepsilon h(o)\}p(o)}
{E_P[\exp\{\varepsilon h(O)\}]}.
\]

其 score 是：

\[
S(O)=h(O)-E\{h(O)\}.
\]

---

## Step 4：对目标参数求 pathwise derivative

以 ATE 为例：

\[
\psi(P)
=
\int \{m_1(x)-m_0(x)\}dP_X(x).
\]

它有两类 perturbation：

### 第一类：\(P_X\) 的扰动

如果 \(p(x)\) 被扰动，则

\[
\left.\frac{d}{d\varepsilon}\psi(P_\varepsilon)\right|_0
=
E\left[
\{m_1(X)-m_0(X)-\psi\}S_X(X)
\right].
\]

因此 covariate distribution component 是：

\[
\phi_X(O)
=
m_1(X)-m_0(X)-\psi.
\]

---

### 第二类：\(m_a(x)\) 的扰动

对 \(m_1(x)\) 而言，

\[
m_1(x)=E(Y\mid A=1,X=x).
\]

在 \(p(y\mid a,x)\) 的扰动下，

\[
\left.\frac{d}{d\varepsilon}m_1^\varepsilon(x)\right|_0
=
E\left[
\{Y-m_1(X)\}S_Y(Y\mid A,X)
\mid A=1,X=x
\right].
\]

要把它变成 full observed-data expectation，需要乘上 inverse propensity：

\[
E\left[
\frac{A}{e(X)}
\{Y-m_1(X)\}
S_Y(Y\mid A,X)
\right].
\]

类似地，对 \(m_0(x)\)：

\[
E\left[
\frac{1-A}{1-e(X)}
\{Y-m_0(X)\}
S_Y(Y\mid A,X)
\right].
\]

因为 ATE 是 \(m_1-m_0\)，所以 outcome part 是：

\[
\phi_Y(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}.
\]

---

## Step 5：合并所有 components

因此：

\[
\phi(O)
=
\phi_Y(O)+\phi_X(O).
\]

即

\[
\phi(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

这就是 ATE 的 EIF。

---

## Step 6：验证 mean zero

检查：

\[
E\left[\frac{A}{e(X)}\{Y-m_1(X)\}\right]=0.
\]

因为：

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

同理 control arm 那部分也是 0。

最后：

\[
E\{m_1(X)-m_0(X)-\psi\}=0.
\]

所以：

\[
E\{\phi(O)\}=0.
\]

---

## 4. Coding agent 可执行的通用算法

可以让 coding agent 按下面步骤操作。

```text
Task: Derive and implement the efficient influence function for a semiparametric target.

Inputs:
1. Observed data O.
2. Factorization of the observed-data likelihood.
3. Target parameter psi(P).
4. Model assumptions.
5. Nuisance functions.
6. Whether the model is nonparametric or restricted.

Procedure:
1. Express psi(P) as an explicit functional of the observed-data law.
2. Identify all nuisance functions appearing in the target and in the observed-data representation.
3. Factorize the likelihood into conditional densities.
4. Write the score decomposition corresponding to each conditional density.
5. For each likelihood component:
   a. Perturb only that component.
   b. Compute the pathwise derivative of psi(P).
   c. Rewrite the derivative as E[component * score].
   d. Extract the corresponding EIF component.
6. Sum all EIF components.
7. Center the result so that E[EIF] = 0.
8. If the model is restricted, project the full-model EIF onto the nuisance tangent space.
9. Verify:
   a. Mean-zero property.
   b. Pathwise derivative identity.
   c. Finite-difference check using exponential tilting.
   d. Orthogonality / double robustness if applicable.
10. Implement the EIF as a function of observed data and nuisance estimates.
```

---

## 5. 推荐给 coding agent 的输出格式

可以要求 coding agent 每次输出下面几部分：

```text
1. Observed data structure
2. Target parameter
3. Identification formula
4. Nuisance functions
5. Likelihood factorization
6. Score decomposition
7. Pathwise derivative calculation
8. EIF expression
9. Mean-zero verification
10. Implementation function
11. Unit tests / numerical checks
```

---

## 6. 常见参数的 EIF 模板

### 6.1 Mean

数据：

\[
O=Y.
\]

目标：

\[
\psi=E(Y).
\]

EIF：

\[
\phi(Y)=Y-\psi.
\]

Estimator：

\[
\hat\psi=\mathbb P_n Y.
\]

Asymptotic variance：

\[
\frac{1}{n}Var(Y).
\]

---

### 6.2 Missing data mean under MAR

观测数据：

\[
O=(R,RY,X),
\]

其中 \(R=1\) 表示 \(Y\) 被观测到。

目标：

\[
\psi=E(Y).
\]

假设：

\[
Y \perp R \mid X.
\]

定义：

\[
m(X)=E(Y\mid X),
\]

\[
\pi(X)=P(R=1\mid X).
\]

EIF：

\[
\phi(O)
=
\frac{R}{\pi(X)}\{Y-m(X)\}
+
m(X)-\psi.
\]

这里第一项是 inverse probability weighted residual，第二项是 covariate distribution part。

---

### 6.3 ATE under unconfoundedness

观测数据：

\[
O=(Y,A,X),
\]

其中 \(A\in\{0,1\}\)。

目标：

\[
\psi=E\{Y(1)-Y(0)\}.
\]

假设：

\[
(Y(1),Y(0))\perp A\mid X.
\]

定义：

\[
m_a(X)=E(Y\mid A=a,X),
\]

\[
e(X)=P(A=1\mid X).
\]

EIF：

\[
\phi(O)
=
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi.
\]

对应 one-step / AIPW estimator：

\[
\hat\psi
=
\mathbb P_n
\left[
\hat m_1(X)-\hat m_0(X)
+
\frac{A}{\hat e(X)}\{Y-\hat m_1(X)\}
-
\frac{1-A}{1-\hat e(X)}\{Y-\hat m_0(X)\}
\right].
\]

---

### 6.4 Average treatment effect on the treated, ATT

目标：

\[
\psi=E\{Y(1)-Y(0)\mid A=1\}.
\]

定义：

\[
p=P(A=1),
\]

\[
m_0(X)=E(Y\mid A=0,X),
\]

\[
e(X)=P(A=1\mid X).
\]

一个常用 EIF 形式是：

\[
\phi(O)
=
\frac{A}{p}
\{Y-m_0(X)-\psi\}
-
\frac{1-A}{p}
\frac{e(X)}{1-e(X)}
\{Y-m_0(X)\}.
\]

对应 estimator：

\[
\hat\psi
=
\frac{1}{\sum_i A_i}
\sum_i
\left[
A_i\{Y_i-\hat m_0(X_i)\}
-
(1-A_i)
\frac{\hat e(X_i)}{1-\hat e(X_i)}
\{Y_i-\hat m_0(X_i)\}
\right].
\]

---

## 7. 从 EIF 到 estimator 的一般原则

如果已经有 EIF：

\[
\phi(O;\eta,\psi),
\]

其中 \(\eta\) 是 nuisance functions，则常见做法是求解 estimating equation：

\[
\mathbb P_n \phi(O;\hat\eta,\hat\psi)=0.
\]

很多时候 EIF 可以写成：

\[
\phi(O;\eta,\psi)
=
D(O;\eta)-\psi.
\]

那么 estimator 就是：

\[
\hat\psi
=
\mathbb P_n D(O;\hat\eta).
\]

例如 ATE 中：

\[
D(O;\eta)
=
m_1(X)-m_0(X)
+
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}.
\]

所以：

\[
\hat\psi
=
\mathbb P_n D(O;\hat\eta).
\]

---

## 8. Coding implementation skeleton

以 ATE 为例，可以让 coding agent 写成这样。

```python
import numpy as np

def eif_ate(y, a, x, m1_hat, m0_hat, e_hat, psi_hat, eps=1e-6):
    """
    Efficient influence function for ATE under unconfoundedness.

    Parameters
    ----------
    y : array-like, shape (n,)
        Outcome.
    a : array-like, shape (n,)
        Binary treatment indicator.
    x : array-like
        Covariates. Included for interface consistency.
    m1_hat : array-like, shape (n,)
        Estimated E[Y | A=1, X].
    m0_hat : array-like, shape (n,)
        Estimated E[Y | A=0, X].
    e_hat : array-like, shape (n,)
        Estimated P[A=1 | X].
    psi_hat : float
        Estimated ATE.
    eps : float
        Clipping constant for propensity scores.

    Returns
    -------
    phi : ndarray, shape (n,)
        Estimated EIF values.
    """
    y = np.asarray(y)
    a = np.asarray(a)

    e_hat = np.clip(np.asarray(e_hat), eps, 1.0 - eps)
    m1_hat = np.asarray(m1_hat)
    m0_hat = np.asarray(m0_hat)

    phi = (
        a / e_hat * (y - m1_hat)
        - (1.0 - a) / (1.0 - e_hat) * (y - m0_hat)
        + m1_hat
        - m0_hat
        - psi_hat
    )

    return phi


def aipw_ate(y, a, x, m1_hat, m0_hat, e_hat, eps=1e-6):
    """
    AIPW / one-step estimator for ATE.
    """
    y = np.asarray(y)
    a = np.asarray(a)

    e_hat = np.clip(np.asarray(e_hat), eps, 1.0 - eps)
    m1_hat = np.asarray(m1_hat)
    m0_hat = np.asarray(m0_hat)

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

## 9. Cross-fitting 的建议

如果 nuisance functions 用机器学习估计，例如 random forest, gradient boosting, neural networks, lasso，需要 cross-fitting。

基本流程：

```text
1. Split data into K folds.
2. For each fold k:
   a. Fit nuisance functions on all folds except k.
   b. Predict nuisance functions on fold k.
3. Combine out-of-fold predictions.
4. Plug out-of-fold nuisance estimates into EIF-based estimator.
5. Estimate standard error using empirical variance of EIF.
```

这样可以避免过拟合导致的 empirical process 问题。

ATE 的 cross-fitting estimator：

\[
\hat\psi
=
\mathbb P_n
\left[
\hat m_1^{(-k_i)}(X_i)-\hat m_0^{(-k_i)}(X_i)
+
\frac{A_i}{\hat e^{(-k_i)}(X_i)}
\{Y_i-\hat m_1^{(-k_i)}(X_i)\}
-
\frac{1-A_i}{1-\hat e^{(-k_i)}(X_i)}
\{Y_i-\hat m_0^{(-k_i)}(X_i)\}
\right].
\]

---

## 10. 数值验证方法

这是指导 coding agent 非常重要的一部分。

### Check 1：mean-zero check

在模拟数据中，计算：

```python
np.mean(phi_hat)
```

应该接近 0。

注意，如果用的是 estimated nuisance functions，有限样本下不一定严格为 0。但如果 estimator 是

```python
psi_hat = np.mean(pseudo_outcome)
phi_hat = pseudo_outcome - psi_hat
```

则 empirical mean 会严格为 0。

---

### Check 2：variance check

标准误：

\[
\widehat{SE}
=
\sqrt{\frac{\mathbb P_n\{\hat\phi^2\}}{n}}.
\]

代码：

```python
se_hat = np.std(phi_hat, ddof=1) / np.sqrt(n)
```

---

### Check 3：finite-difference pathwise derivative check

使用 exponential tilting 构造扰动：

\[
w_\varepsilon(O_i)
=
\frac{\exp\{\varepsilon h(O_i)\}}
{\frac{1}{n}\sum_{j=1}^n \exp\{\varepsilon h(O_j)\}}.
\]

然后计算 weighted target：

\[
\psi(P_\varepsilon)
\]

并比较：

\[
\frac{\psi(P_\varepsilon)-\psi(P)}{\varepsilon}
\]

和

\[
\mathbb P_n\{\phi(O)h(O)\}.
\]

伪代码：

```python
def finite_difference_check(phi, h, psi_eps, psi_0, eps):
    lhs = (psi_eps - psi_0) / eps
    rhs = np.mean(phi * (h - np.mean(h)))
    return lhs, rhs, lhs - rhs
```

这个 check 的难点是：不同 target 的 \(\psi(P_\varepsilon)\) 需要重新定义 weighted version。对简单 target 比较容易，对 treatment effect target 需要 weighted nuisance regressions。

---

### Check 4：orthogonality check

EIF-based estimator 通常有 Neyman orthogonality。可以检查：

\[
\left.
\frac{\partial}{\partial t}
E\{D(O;\eta_t)\}
\right|_{t=0}
=
0
\]

在 true nuisance \(\eta_0\) 附近成立。

实践中可以做 perturbation：

```python
m1_t = m1_true + t * noise1
m0_t = m0_true + t * noise0
e_t = e_true + t * noise_e
```

然后观察 bias 是否是一阶消失，即 bias 大约是 \(O(t^2)\)，而不是 \(O(t)\)。

---

## 11. 一个可直接给 coding agent 的 prompt

下面这段可以直接复制给 coding agent。

```text
You are given a semiparametric target parameter. Derive its influence function or efficient influence function, and implement the estimator only if requested or useful.

Please follow this procedure exactly:

1. Define the observed data structure O.
2. State the target parameter psi(P).
3. Normalize the problem and assign a target triage route.
4. State identification assumptions.
5. State whether the target is identified and pathwise differentiable.
6. Express psi(P) as a functional of the observed-data distribution.
7. Identify all nuisance functions.
8. Factorize the observed-data likelihood into conditional densities.
9. Write the score decomposition for this factorization.
10. For hard problems, build a component ledger.
11. For each score component:
   a. Perturb only the corresponding likelihood component.
   b. Compute the pathwise derivative of psi(P).
   c. Rewrite the derivative as an inner product E[phi_j(O) S_j(O)].
   d. Extract the IF component phi_j(O).
12. Sum all components.
13. Center the IF to ensure E[phi(O)] = 0.
14. If the model is restricted, project the full-model gradient onto the tangent space or state that projection is required.
15. If the target is nonregular, stop and suggest a regularized alternative instead of forcing an EIF.
16. Verify the final IF/EIF by checking:
    a. mean-zero property;
    b. pathwise derivative identity;
    c. finite-difference perturbation using exponential tilting;
    d. orthogonality to nuisance perturbations, if applicable.
17. If implementation is requested, implement:
    a. a function that computes the EIF values;
    b. a one-step or estimating-equation estimator;
    c. a standard error estimator based on empirical variance of EIF;
    d. optional K-fold cross-fitting for nuisance estimation.

Output format:
- Observed data
- Target parameter
- Target triage and derivation route
- Identification formula
- Model and regularity status
- Nuisance functions
- Likelihood factorization
- Score decomposition
- Component ledger for hard problems
- Pathwise derivative derivation
- Candidate IF / valid IF / EIF / projection or nonregularity conclusion
- Mean-zero verification
- Implementation, if requested
- Numerical checks
```

---

## 12. 最常见的错误

### 错误 1：把 estimator 的 derivative 当作 IF

IF 是 target functional \(\psi(P)\) 对 distribution \(P\) 的 derivative，不是某个具体 estimator 的普通导数。

---

### 错误 2：忘记 center

EIF 必须满足：

\[
E\{\phi(O)\}=0.
\]

如果最后没有 \(-\psi\)，通常要检查是否漏掉了 centering term。

---

### 错误 3：忽略 likelihood factorization

比如 ATE 的 EIF 不是凭空出现的。它来自：

\[
p(y\mid a,x),\quad p(a\mid x),\quad p(x).
\]

不分解 likelihood，就很容易漏掉 component。

---

### 错误 4：混淆 nuisance function 和 target parameter

例如在 ATE 中：

\[
m_1(x),m_0(x),e(x)
\]

都是 nuisance functions。

目标参数是：

\[
\psi=E\{m_1(X)-m_0(X)\}.
\]

---

### 错误 5：positivity 问题没有处理

ATE 的 EIF 中有：

\[
\frac{1}{e(X)},\qquad \frac{1}{1-e(X)}.
\]

所以必须要求：

\[
0<c<e(X)<1-c.
\]

coding 时需要 clipping：

```python
e_hat = np.clip(e_hat, eps, 1 - eps)
```

---

## 13. 一个简洁的记忆方法

对很多 semiparametric target，EIF 常常可以写成：

\[
\text{EIF}
=
\text{residual correction}
+
\text{plug-in target contrast}
-
\text{target parameter}.
\]

例如 ATE：

\[
\text{EIF}
=
\text{IPW residual correction}
+
\{m_1(X)-m_0(X)\}
-
\psi.
\]

Missing data mean：

\[
\text{EIF}
=
\text{IPW residual correction}
+
m(X)
-
\psi.
\]

普通均值：

\[
\text{EIF}
=
Y-\psi.
\]

这个结构非常适合指导 coding agent：先找 plug-in target，再找 residual correction，最后减去 \(\psi\)。
