# Mathematical Foundations for Machine Learning & Deep Learning

## Table of Contents

1. [Statistics Fundamentals](#statistics-fundamentals)
2. [Probability Theory](#probability-theory)
3. [Linear Algebra](#linear-algebra)
4. [Calculus for ML](#calculus-for-ml)
5. [Optimization](#optimization)
6. [Information Theory](#information-theory)

---

# Part 1: Statistics Fundamentals

## Descriptive Statistics

### Measures of Central Tendency

#### Mean (Average)

The sum of all values divided by the number of values.

```python
import numpy as np

data = [2, 4, 6, 8, 10]

# Arithmetic Mean
mean = np.mean(data)  # (2+4+6+8+10)/5 = 6.0

# Manual calculation
mean_manual = sum(data) / len(data)

# Weighted Mean
weights = [0.1, 0.2, 0.3, 0.2, 0.2]
weighted_mean = np.average(data, weights=weights)

# Geometric Mean (for rates of change, percentages)
from scipy.stats import gmean
geo_mean = gmean(data)  # (2*4*6*8*10)^(1/5)

# Harmonic Mean (for rates, speeds)
from scipy.stats import hmean
harm_mean = hmean(data)  # n / (1/x₁ + 1/x₂ + ... + 1/xₙ)

print(f"Arithmetic Mean: {mean}")
print(f"Geometric Mean: {geo_mean:.4f}")
print(f"Harmonic Mean: {harm_mean:.4f}")
```

**When to use:**
| Mean Type | Use Case |
|-----------|----------|
| Arithmetic | General average, symmetric data |
| Weighted | Different importance for values |
| Geometric | Growth rates, compound interest |
| Harmonic | Rates, speeds, ratios |

---

#### Median

The middle value when data is sorted.

```python
import numpy as np

data_odd = [3, 1, 4, 1, 5, 9, 2]
data_even = [3, 1, 4, 1, 5, 9]

median_odd = np.median(data_odd)   # Middle value: 3
median_even = np.median(data_even)  # Average of two middle values: 2.5

# Robust to outliers
data_with_outlier = [1, 2, 3, 4, 100]
print(f"Mean: {np.mean(data_with_outlier)}")    # 22.0 (affected by outlier)
print(f"Median: {np.median(data_with_outlier)}")  # 3.0 (not affected)
```

---

#### Mode

The most frequently occurring value.

```python
from scipy import stats
import numpy as np

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

mode_result = stats.mode(data, keepdims=True)
mode_value = mode_result.mode[0]    # 3
mode_count = mode_result.count[0]   # 3

# For multiple modes
from collections import Counter
counter = Counter(data)
max_count = max(counter.values())
modes = [k for k, v in counter.items() if v == max_count]
print(f"Mode(s): {modes}")
```

**Comparison:**

```
Data: [1, 2, 3, 4, 5, 100]
Mean = 19.17  (pulled by outlier)
Median = 3.5  (robust)
Mode = None   (no repeats)

Distribution shape:
- Symmetric: Mean ≈ Median ≈ Mode
- Right-skewed: Mean > Median > Mode
- Left-skewed: Mean < Median < Mode
```

---

### Measures of Dispersion

#### Range

```python
data = [2, 4, 6, 8, 10]
range_val = np.max(data) - np.min(data)  # 10 - 2 = 8
```

#### Variance

Average of squared deviations from the mean.

```python
import numpy as np

data = [2, 4, 6, 8, 10]

# Population Variance (σ²)
# When you have the entire population
pop_variance = np.var(data)  # Divides by N

# Sample Variance (s²)
# When you have a sample from population
sample_variance = np.var(data, ddof=1)  # Divides by N-1 (Bessel's correction)

# Manual calculation
mean = np.mean(data)
squared_diff = [(x - mean)**2 for x in data]
pop_var_manual = sum(squared_diff) / len(data)
sample_var_manual = sum(squared_diff) / (len(data) - 1)

print(f"Population Variance: {pop_variance}")
print(f"Sample Variance: {sample_variance}")
```

**Formula:**

```
Population Variance: σ² = Σ(xᵢ - μ)² / N
Sample Variance: s² = Σ(xᵢ - x̄)² / (N-1)
```

---

#### Standard Deviation

Square root of variance - in the same units as the data.

```python
import numpy as np

data = [2, 4, 6, 8, 10]

# Population Standard Deviation (σ)
pop_std = np.std(data)

# Sample Standard Deviation (s)
sample_std = np.std(data, ddof=1)

print(f"Population Std Dev: {pop_std:.4f}")
print(f"Sample Std Dev: {sample_std:.4f}")

# Interpretation: 68-95-99.7 rule (for normal distribution)
# ~68% of data within μ ± 1σ
# ~95% of data within μ ± 2σ
# ~99.7% of data within μ ± 3σ
```

---

#### Coefficient of Variation

Relative measure of variability (unitless).

```python
# CV = (Standard Deviation / Mean) × 100%
data = [2, 4, 6, 8, 10]
cv = (np.std(data, ddof=1) / np.mean(data)) * 100
print(f"Coefficient of Variation: {cv:.2f}%")

# Useful for comparing variability across different scales
prices = [100, 110, 95, 105, 100]
quantities = [1000, 1100, 950, 1050, 1000]

cv_prices = (np.std(prices, ddof=1) / np.mean(prices)) * 100
cv_quantities = (np.std(quantities, ddof=1) / np.mean(quantities)) * 100
print(f"Price CV: {cv_prices:.2f}%, Quantity CV: {cv_quantities:.2f}%")
```

---

### Quartiles and Percentiles

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Quartiles
Q1 = np.percentile(data, 25)  # 25th percentile
Q2 = np.percentile(data, 50)  # 50th percentile (median)
Q3 = np.percentile(data, 75)  # 75th percentile

# Interquartile Range (IQR)
IQR = Q3 - Q1

# Five-number summary
min_val = np.min(data)
max_val = np.max(data)
print(f"Min: {min_val}, Q1: {Q1}, Median: {Q2}, Q3: {Q3}, Max: {max_val}")
print(f"IQR: {IQR}")

# Outlier detection using IQR
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(data < lower_bound) | (data > upper_bound)]
print(f"Outlier bounds: [{lower_bound}, {upper_bound}]")
```

---

### Moments

Moments describe the shape of a distribution.

```python
import numpy as np
from scipy import stats

data = np.random.normal(loc=5, scale=2, size=1000)

# 1st Moment: Mean (measure of location)
first_moment = np.mean(data)

# 2nd Moment: Variance (measure of spread)
second_moment = np.var(data)

# 3rd Moment: Skewness (measure of asymmetry)
skewness = stats.skew(data)
# Positive skew: tail extends right (mean > median)
# Negative skew: tail extends left (mean < median)
# Zero: symmetric

# 4th Moment: Kurtosis (measure of tailedness)
kurtosis = stats.kurtosis(data)
# Positive (leptokurtic): heavy tails, sharp peak
# Negative (platykurtic): light tails, flat peak
# Zero (mesokurtic): normal distribution

print(f"Mean (1st moment): {first_moment:.4f}")
print(f"Variance (2nd moment): {second_moment:.4f}")
print(f"Skewness (3rd moment): {skewness:.4f}")
print(f"Kurtosis (4th moment): {kurtosis:.4f}")
```

**Visual Representation:**

```
Skewness:
Left-skewed          Symmetric           Right-skewed
    ____                 /\                   ____
   /    \               /  \                 /    \
  /      \____         /    \           ____/      \

Kurtosis:
Platykurtic         Mesokurtic          Leptokurtic
(flat)              (normal)            (peaked)
   ___                 /\                   |
  /   \               /  \                 /|\
 /     \             /    \               / | \
```

---

### Covariance and Correlation

#### Covariance

Measures how two variables change together.

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Covariance
cov_matrix = np.cov(x, y)
cov_xy = cov_matrix[0, 1]

# Manual calculation
mean_x, mean_y = np.mean(x), np.mean(y)
cov_manual = np.sum((x - mean_x) * (y - mean_y)) / (len(x) - 1)

print(f"Covariance: {cov_xy:.4f}")
print(f"Covariance Matrix:\n{cov_matrix}")
```

**Interpretation:**

- Cov > 0: Variables increase together
- Cov < 0: One increases as other decreases
- Cov ≈ 0: No linear relationship

---

#### Correlation (Pearson)

Standardized covariance, ranges from -1 to 1.

```python
import numpy as np
from scipy import stats

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Pearson correlation coefficient
corr_matrix = np.corrcoef(x, y)
corr_xy = corr_matrix[0, 1]

# Using scipy (includes p-value)
corr, p_value = stats.pearsonr(x, y)

# Manual calculation
# r = Cov(X,Y) / (σx * σy)
r_manual = np.cov(x, y)[0, 1] / (np.std(x, ddof=1) * np.std(y, ddof=1))

print(f"Pearson Correlation: {corr:.4f}")
print(f"P-value: {p_value:.4f}")
```

**Interpretation:**

```
r = 1.0  : Perfect positive correlation
r = 0.7  : Strong positive
r = 0.3  : Weak positive
r = 0.0  : No linear correlation
r = -0.3 : Weak negative
r = -0.7 : Strong negative
r = -1.0 : Perfect negative correlation
```

---

#### Spearman Correlation (Rank-based)

For non-linear monotonic relationships.

```python
from scipy import stats

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])  # y = x² (non-linear but monotonic)

pearson_corr, _ = stats.pearsonr(x, y)
spearman_corr, _ = stats.spearmanr(x, y)

print(f"Pearson: {pearson_corr:.4f}")   # ~0.98
print(f"Spearman: {spearman_corr:.4f}")  # 1.0 (perfect monotonic)
```

---

### Z-Score (Standard Score)

```python
import numpy as np
from scipy import stats

data = np.array([65, 70, 75, 80, 85, 90, 95])

# Z-score: how many standard deviations from mean
z_scores = stats.zscore(data)

# Manual calculation
mean = np.mean(data)
std = np.std(data, ddof=0)
z_manual = (data - mean) / std

print(f"Original data: {data}")
print(f"Z-scores: {z_scores}")

# Interpret: value of 95
z_95 = (95 - mean) / std
print(f"Z-score for 95: {z_95:.4f}")
# Positive z-score: above mean
# Negative z-score: below mean
```

---

## Distributions

### Normal Distribution (Gaussian)

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Parameters
mu = 0      # mean
sigma = 1   # standard deviation

# Create normal distribution
norm_dist = stats.norm(loc=mu, scale=sigma)

# Probability Density Function (PDF)
x = np.linspace(-4, 4, 100)
pdf = norm_dist.pdf(x)

# Cumulative Distribution Function (CDF)
cdf = norm_dist.cdf(x)

# Random samples
samples = norm_dist.rvs(size=1000)

# Probability calculations
prob_less_than_1 = norm_dist.cdf(1)  # P(X < 1)
prob_between = norm_dist.cdf(1) - norm_dist.cdf(-1)  # P(-1 < X < 1)

# Inverse CDF (quantile function)
percentile_95 = norm_dist.ppf(0.95)  # Value at 95th percentile

print(f"P(X < 1): {prob_less_than_1:.4f}")
print(f"P(-1 < X < 1): {prob_between:.4f}")  # ~68%
print(f"95th percentile: {percentile_95:.4f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x, pdf)
axes[0].set_title('Normal Distribution PDF')
axes[0].fill_between(x, pdf, alpha=0.3)

axes[1].plot(x, cdf)
axes[1].set_title('Normal Distribution CDF')
plt.show()
```

---

### Other Important Distributions

```python
from scipy import stats

# Binomial Distribution (discrete)
# Number of successes in n trials
n, p = 10, 0.5
binom_dist = stats.binom(n=n, p=p)
print(f"Binomial P(X=5): {binom_dist.pmf(5):.4f}")
print(f"Binomial Mean: {binom_dist.mean()}")

# Poisson Distribution (discrete)
# Number of events in fixed interval
lambda_param = 3
poisson_dist = stats.poisson(mu=lambda_param)
print(f"Poisson P(X=2): {poisson_dist.pmf(2):.4f}")

# Exponential Distribution (continuous)
# Time between events
exp_dist = stats.expon(scale=1/lambda_param)
print(f"Exponential P(X<1): {exp_dist.cdf(1):.4f}")

# Uniform Distribution
uniform_dist = stats.uniform(loc=0, scale=10)  # [0, 10]
print(f"Uniform Mean: {uniform_dist.mean()}")

# Chi-Square Distribution
# Used in hypothesis testing
chi2_dist = stats.chi2(df=5)
print(f"Chi-Square 95th percentile: {chi2_dist.ppf(0.95):.4f}")

# Student's t-Distribution
# Used when sample size is small
t_dist = stats.t(df=10)
print(f"t-Distribution 95th percentile: {t_dist.ppf(0.95):.4f}")
```

---

### Central Limit Theorem

```python
import numpy as np
import matplotlib.pyplot as plt

# CLT: Sample means approach normal distribution
# regardless of original distribution

# Original non-normal distribution (uniform)
population = np.random.uniform(0, 100, 100000)

# Take many samples and compute means
sample_means = []
sample_size = 30
num_samples = 1000

for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(population, bins=50, edgecolor='black')
axes[0].set_title('Original Distribution (Uniform)')

axes[1].hist(sample_means, bins=50, edgecolor='black')
axes[1].set_title(f'Distribution of Sample Means (n={sample_size})')

plt.tight_layout()
plt.show()

print(f"Population Mean: {np.mean(population):.4f}")
print(f"Mean of Sample Means: {np.mean(sample_means):.4f}")
print(f"Std of Sample Means: {np.std(sample_means):.4f}")
print(f"Expected SE: {np.std(population)/np.sqrt(sample_size):.4f}")
```

---

# Part 2: Probability Theory

## Basic Probability

```python
# Sample space for a die roll
sample_space = {1, 2, 3, 4, 5, 6}

# Event: rolling an even number
event_even = {2, 4, 6}

# Probability
prob_even = len(event_even) / len(sample_space)
print(f"P(even) = {prob_even}")  # 0.5

# Complement: P(not A) = 1 - P(A)
prob_odd = 1 - prob_even
```

### Conditional Probability

```python
# P(A|B) = P(A ∩ B) / P(B)

# Example: Card drawn from deck
# P(King | Face card)

# Face cards: J, Q, K of each suit = 12 cards
# Kings: 4 cards
# P(King | Face card) = 4/12 = 1/3

p_king_given_face = 4 / 12
print(f"P(King | Face card) = {p_king_given_face:.4f}")
```

### Bayes' Theorem

```python
# P(A|B) = P(B|A) * P(A) / P(B)

# Example: Medical test
# - Disease prevalence: 1%
# - Test sensitivity (true positive rate): 95%
# - Test specificity (true negative rate): 90%

# What's P(Disease | Positive test)?

p_disease = 0.01
p_no_disease = 0.99
p_positive_given_disease = 0.95      # sensitivity
p_negative_given_no_disease = 0.90   # specificity
p_positive_given_no_disease = 0.10   # false positive rate

# P(Positive) using law of total probability
p_positive = (p_positive_given_disease * p_disease +
              p_positive_given_no_disease * p_no_disease)

# Bayes' Theorem
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive

print(f"P(Disease | Positive) = {p_disease_given_positive:.4f}")
# Only ~8.7% chance of actually having disease with positive test!
```

### Expected Value and Variance

```python
import numpy as np

# Discrete random variable
values = np.array([1, 2, 3, 4, 5, 6])  # Die faces
probabilities = np.array([1/6] * 6)    # Fair die

# Expected Value: E[X] = Σ xᵢ * P(xᵢ)
expected_value = np.sum(values * probabilities)
print(f"E[X] = {expected_value}")  # 3.5

# Variance: Var(X) = E[(X - μ)²] = E[X²] - (E[X])²
e_x_squared = np.sum(values**2 * probabilities)
variance = e_x_squared - expected_value**2
print(f"Var(X) = {variance:.4f}")

# Properties
# E[aX + b] = a*E[X] + b
# Var(aX + b) = a²*Var(X)
# E[X + Y] = E[X] + E[Y]
# Var(X + Y) = Var(X) + Var(Y)  (if independent)
```

---

# Part 3: Linear Algebra

## Scalars, Vectors, Matrices, and Tensors

### Scalar

A single number.

```python
import numpy as np

# Scalar
scalar = 5
scalar_float = 3.14

# Scalar operations
a, b = 3, 4
print(f"Addition: {a + b}")
print(f"Multiplication: {a * b}")
print(f"Power: {a ** 2}")
```

### Vector

A 1D array of numbers.

```python
import numpy as np

# Creating vectors
v1 = np.array([1, 2, 3])           # Row vector (1D array)
v2 = np.array([[1], [2], [3]])     # Column vector (2D array)

# Vector properties
print(f"Shape: {v1.shape}")         # (3,)
print(f"Dimension: {v1.ndim}")      # 1
print(f"Size: {v1.size}")           # 3

# Vector operations
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])

# Element-wise operations
print(f"Addition: {v + w}")         # [5, 7, 9]
print(f"Subtraction: {v - w}")      # [-3, -3, -3]
print(f"Scalar multiplication: {2 * v}")  # [2, 4, 6]
print(f"Element-wise product: {v * w}")   # [4, 10, 18]

# Dot product (inner product)
dot_product = np.dot(v, w)          # 1*4 + 2*5 + 3*6 = 32
print(f"Dot product: {dot_product}")

# Vector magnitude (L2 norm)
magnitude = np.linalg.norm(v)       # √(1² + 2² + 3²) = √14
print(f"Magnitude: {magnitude:.4f}")

# Unit vector (normalization)
unit_vector = v / np.linalg.norm(v)
print(f"Unit vector: {unit_vector}")
print(f"Unit vector magnitude: {np.linalg.norm(unit_vector)}")  # 1.0
```

### Matrix

A 2D array of numbers.

```python
import numpy as np

# Creating matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])           # 2x3 matrix

B = np.array([[1, 2],
              [3, 4],
              [5, 6]])              # 3x2 matrix

# Matrix properties
print(f"Shape: {A.shape}")          # (2, 3)
print(f"Rows: {A.shape[0]}")        # 2
print(f"Columns: {A.shape[1]}")     # 3

# Special matrices
identity = np.eye(3)                # 3x3 identity matrix
zeros = np.zeros((2, 3))            # 2x3 zeros
ones = np.ones((2, 3))              # 2x3 ones
diagonal = np.diag([1, 2, 3])       # Diagonal matrix

print(f"Identity matrix:\n{identity}")

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise operations
print(f"Addition:\n{A + B}")
print(f"Scalar multiplication:\n{2 * A}")
print(f"Element-wise product (Hadamard):\n{A * B}")

# Matrix multiplication
C = np.matmul(A, B)                 # or A @ B
print(f"Matrix multiplication:\n{C}")

# Transpose
print(f"Transpose:\n{A.T}")

# Inverse
A_inv = np.linalg.inv(A)
print(f"Inverse:\n{A_inv}")
print(f"A @ A_inv:\n{A @ A_inv}")   # Should be identity

# Determinant
det = np.linalg.det(A)
print(f"Determinant: {det}")

# Trace (sum of diagonal elements)
trace = np.trace(A)
print(f"Trace: {trace}")            # 1 + 4 = 5
```

### Tensor

An n-dimensional array.

```python
import numpy as np

# Tensor (3D array)
tensor_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])

print(f"Shape: {tensor_3d.shape}")  # (3, 2, 2)
print(f"Dimensions: {tensor_3d.ndim}")  # 3

# 4D tensor (like batch of images)
# Shape: (batch_size, height, width, channels)
batch_images = np.random.randn(32, 28, 28, 3)  # 32 RGB images of 28x28
print(f"Image batch shape: {batch_images.shape}")

# Tensor in PyTorch
import torch
tensor_torch = torch.randn(3, 4, 5)
print(f"PyTorch tensor shape: {tensor_torch.shape}")

# Tensor operations
a = np.random.randn(2, 3, 4)
b = np.random.randn(2, 3, 4)

# Element-wise operations work on tensors
sum_tensor = a + b
product_tensor = a * b
```

**Tensor Hierarchy:**

```
Scalar (0D) → Vector (1D) → Matrix (2D) → Tensor (3D+)
    5           [1,2,3]       [[1,2],      [[[1,2],
                               [3,4]]        [3,4]],
                                            [[5,6],
                                             [7,8]]]
```

---

## Vector Operations in Detail

### Norms (Vector Length)

```python
import numpy as np

v = np.array([3, 4])

# L1 Norm (Manhattan distance)
l1_norm = np.linalg.norm(v, ord=1)  # |3| + |4| = 7
print(f"L1 Norm: {l1_norm}")

# L2 Norm (Euclidean distance)
l2_norm = np.linalg.norm(v, ord=2)  # √(3² + 4²) = 5
print(f"L2 Norm: {l2_norm}")

# L∞ Norm (Max norm)
linf_norm = np.linalg.norm(v, ord=np.inf)  # max(|3|, |4|) = 4
print(f"L∞ Norm: {linf_norm}")

# In ML: L1 (Lasso), L2 (Ridge) regularization
```

### Dot Product Applications

```python
import numpy as np

# Dot product formula: a·b = |a||b|cos(θ)

a = np.array([1, 0])
b = np.array([1, 1])

# Dot product
dot = np.dot(a, b)

# Angle between vectors
cos_theta = dot / (np.linalg.norm(a) * np.linalg.norm(b))
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

print(f"Dot product: {dot}")
print(f"Angle: {angle_deg:.2f} degrees")

# Projection of b onto a
# proj_a(b) = (a·b / |a|²) * a
proj = (np.dot(a, b) / np.dot(a, a)) * a
print(f"Projection of b onto a: {proj}")

# Orthogonality check (dot product = 0)
orthogonal_1 = np.array([1, 0])
orthogonal_2 = np.array([0, 1])
print(f"Orthogonal? {np.dot(orthogonal_1, orthogonal_2) == 0}")
```

### Cross Product (3D)

```python
import numpy as np

a = np.array([1, 0, 0])
b = np.array([0, 1, 0])

cross = np.cross(a, b)
print(f"Cross product: {cross}")  # [0, 0, 1]

# Cross product gives vector perpendicular to both
# Magnitude = area of parallelogram
```

---

## Matrix Operations in Detail

### Matrix Multiplication Rules

```python
import numpy as np

# (m x n) @ (n x p) = (m x p)
A = np.random.randn(2, 3)  # 2x3
B = np.random.randn(3, 4)  # 3x4
C = A @ B                   # 2x4

print(f"A shape: {A.shape}")
print(f"B shape: {B.shape}")
print(f"C shape: {C.shape}")

# Note: AB ≠ BA in general
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"AB:\n{A @ B}")
print(f"BA:\n{B @ A}")
```

### Eigenvalues and Eigenvectors

```python
import numpy as np

A = np.array([[4, 2],
              [1, 3]])

# Eigenvalue equation: Av = λv
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

# Verify: Av = λv
v1 = eigenvectors[:, 0]
lambda1 = eigenvalues[0]
print(f"\nAv: {A @ v1}")
print(f"λv: {lambda1 * v1}")

# Applications in ML:
# - PCA uses eigenvectors of covariance matrix
# - PageRank algorithm
# - Spectral clustering
```

### Singular Value Decomposition (SVD)

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# SVD: A = U @ Σ @ V^T
U, s, Vt = np.linalg.svd(A)

print(f"U (left singular vectors):\n{U}")
print(f"Singular values: {s}")
print(f"V^T (right singular vectors):\n{Vt}")

# Reconstruct matrix
S = np.zeros(A.shape)
np.fill_diagonal(S, s)
A_reconstructed = U @ S @ Vt
print(f"\nReconstructed:\n{A_reconstructed}")

# Low-rank approximation (dimensionality reduction)
k = 2  # Keep top k singular values
U_k = U[:, :k]
S_k = np.diag(s[:k])
Vt_k = Vt[:k, :]
A_approx = U_k @ S_k @ Vt_k
print(f"\nRank-{k} approximation:\n{A_approx}")

# Applications:
# - Dimensionality reduction
# - Image compression
# - Recommendation systems
# - Latent Semantic Analysis
```

---

## Matrix Decompositions

```python
import numpy as np
from scipy import linalg

A = np.array([[4, 2, 1],
              [2, 5, 3],
              [1, 3, 6]])

# Cholesky Decomposition (for positive definite matrices)
# A = L @ L^T
L = np.linalg.cholesky(A)
print(f"Cholesky L:\n{L}")
print(f"L @ L^T:\n{L @ L.T}")

# LU Decomposition
# A = P @ L @ U
P, L, U = linalg.lu(A)
print(f"\nLU Decomposition:")
print(f"P @ L @ U:\n{P @ L @ U}")

# QR Decomposition
# A = Q @ R (Q orthogonal, R upper triangular)
Q, R = np.linalg.qr(A)
print(f"\nQR Decomposition:")
print(f"Q @ R:\n{Q @ R}")
print(f"Q is orthogonal: {np.allclose(Q @ Q.T, np.eye(3))}")
```

---

## Broadcasting in NumPy

```python
import numpy as np

# Broadcasting allows operations on arrays of different shapes

# Scalar and array
a = np.array([1, 2, 3])
print(f"a + 10: {a + 10}")  # [11, 12, 13]

# Array and array (different shapes)
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # (2, 3)
b = np.array([10, 20, 30])  # (3,)

print(f"A + b:\n{A + b}")   # b is broadcast to each row

# Column vector broadcasting
c = np.array([[100], [200]])  # (2, 1)
print(f"A + c:\n{A + c}")     # c is broadcast to each column

# Broadcasting rules:
# 1. If dimensions differ, prepend 1s to smaller shape
# 2. Dimensions are compatible if they're equal or one is 1
# 3. Expand dimension of size 1 to match other array
```

---

# Part 4: Calculus for ML

## Derivatives

### Basic Derivatives

```python
import numpy as np
from scipy.misc import derivative

# Function: f(x) = x²
def f(x):
    return x ** 2

# Derivative: f'(x) = 2x
def f_prime(x):
    return 2 * x

# Numerical derivative
x = 3
numerical_derivative = derivative(f, x, dx=1e-6)
analytical_derivative = f_prime(x)

print(f"Numerical derivative at x=3: {numerical_derivative:.4f}")
print(f"Analytical derivative at x=3: {analytical_derivative}")

# Common derivatives:
# d/dx(x^n) = n*x^(n-1)
# d/dx(e^x) = e^x
# d/dx(ln(x)) = 1/x
# d/dx(sin(x)) = cos(x)
# d/dx(cos(x)) = -sin(x)
```

### Chain Rule

```python
# Chain Rule: d/dx[f(g(x))] = f'(g(x)) * g'(x)

# Example: f(x) = (3x + 1)²
# Let g(x) = 3x + 1, h(g) = g²
# f'(x) = 2(3x + 1) * 3 = 6(3x + 1)

def f(x):
    return (3*x + 1) ** 2

def f_prime_chain(x):
    return 6 * (3*x + 1)

x = 2
print(f"Numerical: {derivative(f, x, dx=1e-6):.4f}")
print(f"Chain rule: {f_prime_chain(x)}")
```

### Partial Derivatives

```python
import numpy as np

# f(x, y) = x² + xy + y²
def f(x, y):
    return x**2 + x*y + y**2

# Partial derivatives
# ∂f/∂x = 2x + y
# ∂f/∂y = x + 2y

def df_dx(x, y):
    return 2*x + y

def df_dy(x, y):
    return x + 2*y

x, y = 1, 2
print(f"∂f/∂x at (1,2): {df_dx(x, y)}")  # 4
print(f"∂f/∂y at (1,2): {df_dy(x, y)}")  # 5
```

### Gradient

```python
import numpy as np

# Gradient: vector of partial derivatives
# ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]

# f(x, y) = x² + y²
def f(params):
    x, y = params
    return x**2 + y**2

def gradient(params):
    x, y = params
    return np.array([2*x, 2*y])

point = np.array([3.0, 4.0])
grad = gradient(point)
print(f"Gradient at (3,4): {grad}")  # [6, 8]

# Gradient points in direction of steepest ascent
# Negative gradient points to steepest descent (used in optimization)
```

### Jacobian Matrix

```python
import numpy as np
from scipy.optimize import approx_fprime

# For vector-valued functions f: Rⁿ → Rᵐ
# Jacobian is the matrix of all partial derivatives

# f(x, y) = [x² + y, x + y²]
def f(params):
    x, y = params
    return np.array([x**2 + y, x + y**2])

# Jacobian:
# J = [[∂f₁/∂x, ∂f₁/∂y],
#      [∂f₂/∂x, ∂f₂/∂y]]
# J = [[2x, 1],
#      [1, 2y]]

def jacobian(params):
    x, y = params
    return np.array([[2*x, 1],
                     [1, 2*y]])

point = np.array([1.0, 2.0])
print(f"Jacobian at (1,2):\n{jacobian(point)}")
```

### Hessian Matrix

```python
import numpy as np

# Second-order partial derivatives
# H = [[∂²f/∂x², ∂²f/∂x∂y],
#      [∂²f/∂y∂x, ∂²f/∂y²]]

# f(x, y) = x³ + xy² + y³
def hessian(params):
    x, y = params
    return np.array([[6*x, 2*y],
                     [2*y, 2*x + 6*y]])

point = np.array([1.0, 1.0])
H = hessian(point)
print(f"Hessian at (1,1):\n{H}")

# Eigenvalues of Hessian determine curvature
eigenvalues = np.linalg.eigvals(H)
print(f"Eigenvalues: {eigenvalues}")

# If all positive: local minimum
# If all negative: local maximum
# Mixed signs: saddle point
```

---

## Integrals

```python
import numpy as np
from scipy import integrate

# Definite integral: ∫₀¹ x² dx = 1/3
def f(x):
    return x ** 2

result, error = integrate.quad(f, 0, 1)
print(f"∫₀¹ x² dx = {result:.4f}")

# Double integral: ∫∫ xy dA over [0,1] x [0,1]
def f2d(y, x):  # Note: order is (y, x) for dblquad
    return x * y

result, error = integrate.dblquad(f2d, 0, 1, 0, 1)
print(f"∫∫ xy dA = {result:.4f}")  # 0.25
```

---

# Part 5: Optimization

## Gradient Descent

```python
import numpy as np
import matplotlib.pyplot as plt

# Minimize f(x) = x²
def f(x):
    return x ** 2

def gradient(x):
    return 2 * x

# Gradient Descent
def gradient_descent(start, learning_rate, n_iterations):
    x = start
    history = [x]

    for _ in range(n_iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        history.append(x)

    return x, history

# Run optimization
x_final, history = gradient_descent(start=5.0, learning_rate=0.1, n_iterations=50)
print(f"Final x: {x_final:.6f}")
print(f"Final f(x): {f(x_final):.6f}")

# Visualize
x_vals = np.linspace(-6, 6, 100)
plt.plot(x_vals, [f(x) for x in x_vals], label='f(x)')
plt.scatter(history, [f(x) for x in history], c='red', s=20, label='GD path')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Gradient Descent on f(x) = x²')
plt.show()
```

### Gradient Descent Variants

```python
import numpy as np

class GradientDescentVariants:
    def __init__(self, learning_rate=0.01):
        self.lr = learning_rate

    def vanilla_gd(self, gradient, params, n_iter=100):
        """Standard gradient descent"""
        for _ in range(n_iter):
            params = params - self.lr * gradient(params)
        return params

    def momentum_gd(self, gradient, params, n_iter=100, beta=0.9):
        """Gradient descent with momentum"""
        velocity = np.zeros_like(params)
        for _ in range(n_iter):
            velocity = beta * velocity + (1 - beta) * gradient(params)
            params = params - self.lr * velocity
        return params

    def rmsprop(self, gradient, params, n_iter=100, beta=0.9, epsilon=1e-8):
        """RMSprop optimizer"""
        cache = np.zeros_like(params)
        for _ in range(n_iter):
            grad = gradient(params)
            cache = beta * cache + (1 - beta) * grad**2
            params = params - self.lr * grad / (np.sqrt(cache) + epsilon)
        return params

    def adam(self, gradient, params, n_iter=100, beta1=0.9, beta2=0.999, epsilon=1e-8):
        """Adam optimizer"""
        m = np.zeros_like(params)  # First moment
        v = np.zeros_like(params)  # Second moment

        for t in range(1, n_iter + 1):
            grad = gradient(params)
            m = beta1 * m + (1 - beta1) * grad
            v = beta2 * v + (1 - beta2) * grad**2

            # Bias correction
            m_hat = m / (1 - beta1**t)
            v_hat = v / (1 - beta2**t)

            params = params - self.lr * m_hat / (np.sqrt(v_hat) + epsilon)

        return params

# Example usage
def gradient(x):
    return 2 * x

optimizer = GradientDescentVariants(learning_rate=0.1)
result = optimizer.adam(gradient, params=np.array([5.0]), n_iter=100)
print(f"Adam result: {result}")
```

---

## Convexity

```python
import numpy as np
import matplotlib.pyplot as plt

# Convex function: f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)
# A line between any two points lies above the function

# Examples:
# Convex: x², e^x, |x|
# Non-convex: sin(x), x³

x = np.linspace(-3, 3, 100)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Convex
axes[0].plot(x, x**2, label='x² (convex)')
axes[0].set_title('Convex Function')
axes[0].legend()

# Non-convex
axes[1].plot(x, np.sin(x), label='sin(x) (non-convex)')
axes[1].set_title('Non-convex Function')
axes[1].legend()

plt.show()

# For convex functions:
# - Local minimum = Global minimum
# - Gradient descent guaranteed to find optimal
```

---

## Lagrange Multipliers

```python
from scipy.optimize import minimize

# Constrained optimization:
# Minimize f(x, y) = x² + y²
# Subject to: x + y = 1

# Using scipy
def objective(params):
    x, y = params
    return x**2 + y**2

def constraint(params):
    x, y = params
    return x + y - 1

constraints = {'type': 'eq', 'fun': constraint}
result = minimize(objective, x0=[0, 0], constraints=constraints)

print(f"Optimal point: {result.x}")
print(f"Optimal value: {result.fun}")
```

---

# Part 6: Information Theory

## Entropy

```python
import numpy as np
from scipy.stats import entropy

# Entropy: measure of uncertainty/randomness
# H(X) = -Σ p(x) log₂ p(x)

# Fair coin (maximum entropy for 2 outcomes)
fair_coin = [0.5, 0.5]
entropy_fair = entropy(fair_coin, base=2)
print(f"Fair coin entropy: {entropy_fair:.4f} bits")  # 1.0

# Biased coin (lower entropy)
biased_coin = [0.9, 0.1]
entropy_biased = entropy(biased_coin, base=2)
print(f"Biased coin entropy: {entropy_biased:.4f} bits")  # 0.469

# Fair die (maximum entropy for 6 outcomes)
fair_die = [1/6] * 6
entropy_die = entropy(fair_die, base=2)
print(f"Fair die entropy: {entropy_die:.4f} bits")  # 2.585

# In ML:
# - Cross-entropy loss for classification
# - Information gain in decision trees
```

## Cross-Entropy

```python
import numpy as np

# Cross-entropy: H(p, q) = -Σ p(x) log q(x)
# Measures difference between true distribution p and predicted q

def cross_entropy(p, q):
    # Add small epsilon to avoid log(0)
    epsilon = 1e-15
    q = np.clip(q, epsilon, 1 - epsilon)
    return -np.sum(p * np.log(q))

# True labels (one-hot encoded)
y_true = np.array([1, 0, 0])  # Class 0

# Good prediction
y_pred_good = np.array([0.9, 0.05, 0.05])
ce_good = cross_entropy(y_true, y_pred_good)
print(f"Cross-entropy (good prediction): {ce_good:.4f}")

# Bad prediction
y_pred_bad = np.array([0.1, 0.8, 0.1])
ce_bad = cross_entropy(y_true, y_pred_bad)
print(f"Cross-entropy (bad prediction): {ce_bad:.4f}")

# Perfect prediction
y_pred_perfect = np.array([1.0, 0.0, 0.0])
ce_perfect = cross_entropy(y_true, y_pred_perfect)
print(f"Cross-entropy (perfect): {ce_perfect:.4f}")
```

## KL Divergence

```python
import numpy as np
from scipy.special import kl_div
from scipy.stats import entropy

# KL Divergence: D_KL(P || Q) = Σ P(x) log(P(x) / Q(x))
# Measures how much Q differs from P
# Not symmetric: D_KL(P||Q) ≠ D_KL(Q||P)

p = np.array([0.4, 0.3, 0.3])
q = np.array([0.33, 0.33, 0.34])

# Using scipy
kl_pq = entropy(p, q)
kl_qp = entropy(q, p)

print(f"KL(P || Q): {kl_pq:.4f}")
print(f"KL(Q || P): {kl_qp:.4f}")

# Manual calculation
def kl_divergence(p, q):
    epsilon = 1e-15
    p = np.clip(p, epsilon, 1)
    q = np.clip(q, epsilon, 1)
    return np.sum(p * np.log(p / q))

print(f"KL(P || Q) manual: {kl_divergence(p, q):.4f}")

# In ML:
# - VAE loss function
# - Comparing probability distributions
```

## Mutual Information

```python
from sklearn.metrics import mutual_info_score
import numpy as np

# Mutual Information: I(X; Y) = H(X) + H(Y) - H(X, Y)
# Measures shared information between variables

# Example: correlation between features
x = np.array([0, 0, 1, 1, 2, 2])
y = np.array([0, 1, 0, 1, 0, 1])

mi = mutual_info_score(x, y)
print(f"Mutual Information: {mi:.4f}")

# In ML:
# - Feature selection
# - Measuring variable dependence
```

---

## Quick Reference Formulas

### Statistics

```
Mean: μ = Σxᵢ / n
Variance: σ² = Σ(xᵢ - μ)² / n
Std Dev: σ = √variance
Covariance: Cov(X,Y) = Σ(xᵢ - μₓ)(yᵢ - μᵧ) / n
Correlation: ρ = Cov(X,Y) / (σₓ * σᵧ)
Z-score: z = (x - μ) / σ
```

### Linear Algebra

```
Dot Product: a·b = Σaᵢbᵢ = |a||b|cos(θ)
Matrix Multiply: (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ
L2 Norm: ||x||₂ = √(Σxᵢ²)
L1 Norm: ||x||₁ = Σ|xᵢ|
Eigenvalue: Av = λv
```

### Calculus

```
Power Rule: d/dx(xⁿ) = nxⁿ⁻¹
Chain Rule: d/dx[f(g(x))] = f'(g(x)) · g'(x)
Gradient: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]
```

### Information Theory

```
Entropy: H(X) = -Σ p(x) log p(x)
Cross-Entropy: H(p,q) = -Σ p(x) log q(x)
KL Divergence: D_KL(P||Q) = Σ P(x) log(P(x)/Q(x))
```

---

## Python Libraries Reference

```python
# NumPy - Arrays and linear algebra
import numpy as np

# SciPy - Scientific computing
from scipy import stats, linalg, optimize, integrate

# Statistics
from scipy.stats import norm, binom, poisson  # Distributions
from scipy.stats import pearsonr, spearmanr   # Correlations
from scipy.stats import skew, kurtosis        # Moments

# Linear Algebra
np.dot(a, b)           # Dot product
np.matmul(A, B)        # Matrix multiplication
np.linalg.norm(v)      # Vector norm
np.linalg.inv(A)       # Matrix inverse
np.linalg.det(A)       # Determinant
np.linalg.eig(A)       # Eigenvalues/vectors
np.linalg.svd(A)       # SVD

# Optimization
from scipy.optimize import minimize, minimize_scalar

# Symbolic Math (for derivatives)
import sympy as sp
```

---

_Last updated: 2025_
