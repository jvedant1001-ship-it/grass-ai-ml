# can you give me a quick one shot of numpy

# Here's a quick NumPy "one-shot" cheat sheet that covers the essentials.

# What is NumPy?

# NumPy is Python's core library for fast numerical computing. Its main object is the ndarray (N-dimensional array).

# import numpy as np
# Creating Arrays
# a = np.array([1, 2, 3])

# zeros = np.zeros((2, 3))
# ones = np.ones((2, 3))
# identity = np.eye(3)

# range_arr = np.arange(0, 10, 2)      # [0 2 4 6 8]
# linspace = np.linspace(0, 1, 5)      # 5 evenly spaced values
# Array Basics
# a = np.array([10, 20, 30])

# a.shape      # (3,)
# a.ndim       # 1
# a.size       # 3
# a.dtype      # int64 (usually)
# Indexing & Slicing
# a = np.array([10, 20, 30, 40, 50])

# a[0]         # 10
# a[-1]        # 50
# a[1:4]       # [20 30 40]

# 2D arrays:

# m = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# m[0, 1]      # 2
# m[:, 1]      # [2 5]
# m[1, :]      # [4 5 6]
# Vectorized Operations

# No loops needed.

# a = np.array([1, 2, 3])

# a + 10       # [11 12 13]
# a * 2        # [2 4 6]
# a ** 2       # [1 4 9]

# Array-to-array:

# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])

# x + y        # [5 7 9]
# x * y        # [4 10 18]
# Useful Math Functions
# a = np.array([1, 4, 9])

# np.sqrt(a)
# np.log(a)
# np.exp(a)
# np.sin(a)

# Aggregations:

# a.sum()
# a.mean()
# a.max()
# a.min()
# a.std()
# Reshaping
# a = np.arange(12)

# a.reshape(3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Flatten:

# a.flatten()
# Broadcasting

# NumPy automatically expands dimensions when possible.

# m = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# m + 10

# Result:

# [[11 12 13]
#  [14 15 16]]
# Boolean Filtering
# a = np.array([1, 2, 3, 4, 5])

# a > 3
# # [False False False True True]

# a[a > 3]
# # [4 5]
# Matrix Operations
# A = np.array([[1, 2],
#               [3, 4]])

# B = np.array([[5, 6],
#               [7, 8]])

# Matrix multiplication:

# A @ B
# # or
# np.matmul(A, B)

# Transpose:

# A.T
# Random Numbers
# np.random.seed(42)

# np.random.rand(3)        # uniform [0,1)
# np.random.randn(3)       # normal distribution
# np.random.randint(1, 10, size=5)
# The 80/20 NumPy Toolkit

# If you remember only these:

# np.array()
# np.arange()
# np.linspace()
# .reshape()

# arr.shape
# arr.mean()
# arr.sum()
# arr.max()

# arr + 5
# arr * 2
# arr[arr > x]

# A @ B

# Those few operations are enough for most data science, machine learning, and scientific computing workflows





