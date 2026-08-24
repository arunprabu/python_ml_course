# NumPy - Numerical Python

## What is NumPy?

NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides:

- **High-performance multidimensional array objects** (ndarray) - The core data structure
- **Broadcasting capabilities** - Automatic array operations with different shapes
- **Linear algebra, Fourier transform, and random number capabilities**
- **Tools for integrating C/C++ and Fortran code**
- **Universal functions (ufuncs)** for fast element-wise operations

NumPy serves as the foundation for most scientific computing libraries in Python, including pandas, scikit-learn, TensorFlow, and many others.

## Key Features

### ndarray - The Core Data Structure

```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])
```

### Key Attributes

- **shape**: Dimensions of the array
- **dtype**: Data type of elements
- **ndim**: Number of dimensions
- **size**: Total number of elements
- **itemsize**: Size in bytes of each element

## Key Use Cases

### 1. Scientific Computing

NumPy enables efficient mathematical operations on large datasets, making it ideal for:

- Physics simulations
- Engineering calculations
- Statistical analysis
- Signal processing

### 2. Data Analysis Foundation

NumPy arrays are the building blocks for pandas DataFrames and most data analysis workflows.

### 3. Machine Learning

All major ML libraries use NumPy arrays as their primary data structure:

- Input features and labels
- Weight matrices
- Image data (reshaped into arrays)

### 4. Image Processing

Images can be represented as multi-dimensional arrays:

```python
# RGB image: (height, width, channels)
image = np.zeros((256, 256, 3), dtype=np.uint8)
```

### 5. Financial Modeling

Time series analysis, risk calculations, and portfolio optimization.

### 6. Signal Processing

Audio processing, Fourier transforms, and digital signal processing.

## Installation

### Using pip

```bash
pip install numpy
```

### Using conda

```bash
conda install numpy
```

### Verify Installation

```python
import numpy as np
print("NumPy version:", np.__version__)
```

## How to Use NumPy

### 1. Array Creation

#### From Python Lists

```python
import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5])

# 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
```

#### Built-in Functions

```python
# Zeros
zeros = np.zeros((3, 3))

# Ones
ones = np.ones((2, 4))

# Identity matrix
identity = np.eye(3)

# Range of numbers
range_arr = np.arange(10)

# Evenly spaced numbers
linspace_arr = np.linspace(0, 1, 5)

# Random arrays
random_arr = np.random.rand(3, 3)
```

### 2. Array Operations

#### Element-wise Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Arithmetic
print(a + b)  # [5, 7, 9]
print(a * b)  # [4, 10, 18]
print(a ** 2) # [1, 4, 9]

# Trigonometric
print(np.sin(a))
print(np.sqrt(a))
```

#### Broadcasting

```python
# Arrays with different shapes can be operated on
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])            # Shape: (3,)

result = a + b  # Broadcasting adds b to each row of a
print(result)
```

### 3. Indexing and Slicing

#### Basic Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])    # 10
print(arr[1:4])  # [20, 30, 40]
print(arr[-1])   # 50
```

#### 2D Array Indexing

```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[0, 0])  # 1
print(matrix[1, :])   # [4, 5, 6] - entire row
print(matrix[:, 1])   # [2, 5, 8] - entire column
```

#### Boolean Indexing

```python
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
print(arr[mask])  # [30, 40, 50]
```

### 4. Reshaping Arrays

```python
arr = np.arange(12)  # [0, 1, 2, ..., 11]

# Reshape to 3x4 matrix
reshaped = arr.reshape(3, 4)

# Transpose
transposed = reshaped.T

# Flatten
flat = reshaped.flatten()

# Ravel (similar to flatten but may return view)
raveled = reshaped.ravel()
```

### 5. Mathematical Functions

```python
arr = np.array([1, 2, 3, 4, 5])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Median:", np.median(arr))
```

### 6. Linear Algebra

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
dot_product = np.dot(a, b)
matrix_mult = a @ b

# Transpose
a_T = a.T

# Inverse
a_inv = np.linalg.inv(a)

# Eigenvalues and eigenvectors
eigenvals, eigenvecs = np.linalg.eig(a)

# Solve linear system Ax = b
x = np.linalg.solve(a, np.array([9, 11]))
```

### 7. Random Number Generation

```python
# Set seed for reproducibility
np.random.seed(42)

# Uniform random numbers [0, 1)
uniform = np.random.rand(5)

# Random integers
integers = np.random.randint(0, 10, 5)

# Normal distribution
normal = np.random.normal(0, 1, 5)

# Choice from array
choices = np.random.choice([1, 2, 3, 4, 5], 3, replace=False)
```

## Best Practices

### 1. Vectorization Over Loops

```python
# Good: Vectorized
arr = np.arange(1000000)
result = arr * 2

# Bad: Python loop (slow)
result = []
for x in arr:
    result.append(x * 2)
```

### 2. Use Appropriate Data Types

```python
# Use specific dtypes to save memory
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
arr_float32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)
```

### 3. Avoid Unnecessary Copies

```python
# Use views when possible
arr = np.arange(10)
view = arr[::2]  # Creates a view, not a copy

# Use copy() when you need a separate array
copy_arr = arr.copy()
```

### 4. Pre-allocate Arrays

```python
# Pre-allocate for better performance
result = np.zeros(1000)

# Instead of growing arrays in loops
# result = []
# for i in range(1000):
#     result.append(computation(i))
```

### 5. Use Broadcasting Wisely

```python
# Good broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b  # b is broadcasted to each row

# Avoid unnecessary broadcasting that creates large temporary arrays
```

### 6. Memory Management

```python
# Use del to free memory
large_array = np.zeros((1000, 1000))
# ... use array ...
del large_array  # Free memory
```

### 7. Error Handling

```python
try:
    # Operations that might fail
    result = np.linalg.inv(singular_matrix)
except np.linalg.LinAlgError:
    print("Matrix is singular")
```

### 8. Documentation and Comments

```python
def process_data(data: np.ndarray) -> np.ndarray:
    """
    Process numerical data using vectorized operations.

    Parameters:
    data (np.ndarray): Input array

    Returns:
    np.ndarray: Processed array
    """
    # Vectorized operations are preferred
    return data * 2 + 1
```

## Common Pitfalls to Avoid

### 1. Modifying Views

```python
arr = np.arange(10)
view = arr[::2]  # View of even indices
view[0] = 999    # This modifies the original array!
print(arr)       # [999, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 2. Integer Division

```python
# In Python 2, this would be integer division
result = np.array([5, 6, 7]) / 2  # Always float division in Python 3
```

### 3. Floating Point Precision

```python
# Be aware of floating point limitations
a = np.array([0.1, 0.2, 0.3])
print(a.sum())  # Might not be exactly 0.6 due to floating point errors
```

### 4. Copy vs View Confusion

```python
arr = np.arange(10)
slice_copy = arr[2:5]  # This is a view, not a copy!
slice_copy[0] = 999    # Modifies original array
```

## Performance Tips

### 1. Use Built-in Functions

NumPy's built-in functions are optimized and often faster than custom implementations.

### 2. Avoid Python Loops

Whenever possible, replace Python loops with vectorized NumPy operations.

### 3. Use Appropriate Array Shapes

Consider memory layout (C-order vs Fortran-order) for optimal performance.

### 4. Profile Your Code

Use tools like `timeit` or `cProfile` to identify bottlenecks.

### 5. Consider Memory Usage

Large arrays can consume significant memory. Use `dtype` appropriately.

## Integration with Other Libraries

### Pandas

```python
import pandas as pd

# NumPy arrays can be converted to pandas
df = pd.DataFrame(np.random.rand(10, 3), columns=['A', 'B', 'C'])
```

### Matplotlib

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
```

### Scikit-learn

```python
from sklearn.linear_model import LinearRegression

# Features and targets as NumPy arrays
X = np.random.rand(100, 2)
y = X @ np.array([2, 3]) + np.random.normal(0, 0.1, 100)

model = LinearRegression()
model.fit(X, y)
```

## Conclusion

NumPy is an essential library for scientific computing in Python. Its efficient array operations and mathematical functions make it indispensable for data analysis, machine learning, and scientific computing. By following best practices and understanding NumPy's core concepts, you can write efficient, readable, and maintainable code.

Remember: **Vectorize when possible, avoid Python loops for numerical computations, and leverage NumPy's broadcasting capabilities for concise and efficient code.**
