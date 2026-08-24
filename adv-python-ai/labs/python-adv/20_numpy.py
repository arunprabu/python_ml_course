# 20_numpy.py

# Comprehensive NumPy Examples

import numpy as np

print("NumPy Key Concepts Examples")

# 1. Array Creation

print("\n1. Array Creation")

# From list
arr1 = np.array([1, 2, 3, 4, 5])
print("From list:", arr1)

# 2D array
arr2 = np.array([[1,2], [3,4]])
print("2D array:", arr2)

# Zeros, ones, empty
zeros = np.zeros((3,3))
ones = np.ones((2,4))
empty = np.empty((2,2))
print("Zeros:", zeros)
print("Ones:", ones)
print("Empty:", empty)

# Range
range_arr = np.arange(10)
print("Arange:", range_arr)

# Linspace
lin = np.linspace(0, 1, 5)
print("Linspace:", lin)

# Random
rand = np.random.rand(3,3)
print("Random:", rand)

# 2. Indexing and Slicing

print("\n2. Indexing and Slicing")

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Index 0:", arr[0])
print("Slice 1:3:", arr[1:3])

# 2D
arr2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("2D Array:", arr2d)
print("Element [1,2]:", arr2d[1,2])
print("Row 0:", arr2d[0])
print("Column 1:", arr2d[:,1])

# 3. Operations

print("\n3. Operations")

a = np.array([1,2,3])
b = np.array([4,5,6])
print("a:", a)
print("b:", b)
print("a + b:", a + b)
print("a * b:", a * b)
print("a ** 2:", a ** 2)

# 4. Broadcasting

print("\n4. Broadcasting")

a = np.array([[1,2,3], [4,5,6]])
b = np.array([10, 20, 30])
print("a:", a)
print("b:", b)
print("a + b:", a + b)

# 5. Functions

print("\n5. Functions")

arr = np.array([1,2,3,4,5])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Std:", np.std(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))

# 6. Reshaping

print("\n6. Reshaping")

arr = np.arange(12)
print("1D:", arr)
reshaped = arr.reshape(3,4)
print("Reshaped 3x4:", reshaped)

# 7. Stacking

print("\n7. Stacking")

a = np.array([1,2])
b = np.array([3,4])
print("a:", a)
print("b:", b)
print("vstack:", np.vstack((a,b)))
print("hstack:", np.hstack((a,b)))

# 8. Splitting

print("\n8. Splitting")

arr = np.arange(10)
print("Array:", arr)
print("Split into 2:", np.split(arr, 2))

# 9. Linear Algebra

print("\n9. Linear Algebra")

a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
print("a:", a)
print("b:", b)
print("Dot product:", np.dot(a,b))
print("Transpose a:", a.T)
print("Inverse a:", np.linalg.inv(a))

# 10. Random

print("\n10. Random")

print("Random int:", np.random.randint(0,10,5))
print("Normal:", np.random.normal(0,1,5))
print("Choice:", np.random.choice([1,2,3,4,5], 3))