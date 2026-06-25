# what is the practica; use of numpy like in industry

# NumPy is one of the foundational libraries in Python, and its practical industry use comes from fast numerical computation and efficient handling of large datasets. Many higher-level tools are built on top of it, including Pandas, SciPy, scikit-learn, and TensorFlow.

# Here are some real-world examples:

# 1. Data Science & Analytics

# Companies analyze millions of records (sales, customer behavior, website traffic).

# Example:

# import numpy as np

# sales = np.array([120, 150, 180, 200])
# avg_sales = np.mean(sales)

# Industry use:

# Customer analytics
# Revenue forecasting
# A/B testing
# Business intelligence dashboards
# 2. Machine Learning & AI

# Almost every machine learning algorithm relies on matrix operations, which NumPy performs efficiently.

# Example:

# X = np.array([[1, 2], [3, 4]])
# weights = np.array([0.5, 0.8])

# prediction = X @ weights

# Industry use:

# Recommendation systems
# Fraud detection
# Computer vision
# Natural language processing

# Even when using frameworks like TensorFlow or PyTorch, data often starts as NumPy arrays.

# 3. Finance

# Banks, hedge funds, and fintech companies process huge amounts of numerical data.

# Examples:

# Risk calculations
# Portfolio optimization
# Option pricing
# Trading algorithms
# returns = np.array([0.02, -0.01, 0.03, 0.01])
# volatility = np.std(returns)
# 4. Engineering & Simulation

# Engineers perform simulations involving thousands or millions of calculations.

# Examples:

# Structural analysis
# Signal processing
# Fluid dynamics
# Electrical circuit simulation
# time = np.linspace(0, 10, 1000)
# signal = np.sin(time)
# 5. Image Processing

# Images are essentially large matrices of pixel values.

# image = np.random.randint(0, 255, (1080, 1920, 3))

# Industry use:

# Medical imaging
# Face recognition
# Quality inspection in factories
# Autonomous vehicles
# 6. Scientific Research

# Researchers use NumPy for:

# Physics simulations
# Genomics
# Astronomy
# Climate modeling

# A single satellite image or genome dataset may contain millions of values that NumPy can process efficiently.

# Why Companies Use NumPy Instead of Plain Python Lists

# Consider adding two lists:

# # Python list
# a = [1,2,3]
# b = [4,5,6]

# result = [x+y for x,y in zip(a,b)]

# With NumPy:

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# result = a + b

# Benefits:

# Much faster (implemented in optimized C code)
# Uses less memory
# Supports vectorized operations
# Handles multidimensional data naturally
# Typical Industry Workflow

# A data scientist might:

# Load data with Pandas.
# Convert columns to NumPy arrays.
# Perform calculations and transformations with NumPy.
# Train models using scikit-learn or TensorFlow.
# Deploy results to production systems.

# So in industry, people rarely use NumPy to solve textbook matrix problems. Instead, NumPy acts as the high-performance numerical engine underneath data science, machine learning, analytics, finance, engineering simulations, and image processing systems.

# all basic operation of numpy a begginer need to know

# If you're a beginner, you don't need to learn all of NumPy at once. About 80% of real-world usage comes from a small set of operations.

# 1. Import NumPy
# import numpy as np
# 2. Create Arrays
# 1D Array
# a = np.array([1, 2, 3, 4])
# 2D Array
# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# Special Arrays
# np.zeros((2,3))
# np.ones((2,3))
# np.arange(0,10,2)
# np.linspace(0,1,5)

# Output:

# [0 2 4 6 8]

# [0.   0.25 0.5  0.75 1. ]
# 3. Check Shape and Size
# arr = np.array([[1,2,3],[4,5,6]])

# arr.shape
# arr.ndim
# arr.size

# Output:

# (2,3)
# 2
# 6
# 4. Indexing
# a = np.array([10,20,30,40])

# a[0]
# a[-1]

# Output:

# 10
# 40

# For 2D arrays:

# b[0,1]

# Output:

# 2
# 5. Slicing
# a = np.array([1,2,3,4,5])

# a[1:4]

# Output:

# [2 3 4]

# 2D slicing:

# b[:,1]

# Output:

# [2 5]
# 6. Arithmetic Operations
# a = np.array([1,2,3])

# a + 5
# a - 1
# a * 2
# a / 2

# Output:

# [6 7 8]
# [0 1 2]
# [2 4 6]
# [0.5 1.0 1.5]
# 7. Array-to-Array Operations
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# a + b
# a * b

# Output:

# [5 7 9]

# [4 10 18]
# 8. Aggregation Functions
# a = np.array([1,2,3,4,5])

# np.sum(a)
# np.mean(a)
# np.max(a)
# np.min(a)
# np.std(a)

# Output:

# 15
# 3.0
# 5
# 1
# 1.414

# These are heavily used in data analysis.

# 9. Reshaping Arrays
# a = np.arange(12)

# a.reshape(3,4)

# Output:

# [[0 1 2 3]
#  [4 5 6 7]
#  [8 9 10 11]]
# 10. Flattening

# Convert 2D → 1D

# arr.flatten()
# 11. Transpose

# Rows become columns.

# arr.T

# Example:

# [[1 2]
#  [3 4]]

# becomes

# [[1 3]
#  [2 4]]
# 12. Boolean Filtering

# Very important in data science.

# a = np.array([10,20,30,40])

# a > 20

# Output:

# [False False True True]

# Filter values:

# a[a > 20]

# Output:

# [30 40]
# 13. Logical Conditions
# a[(a > 10) & (a < 40)]

# Output:

# [20 30]
# 14. Joining Arrays
# a = np.array([1,2])
# b = np.array([3,4])

# np.concatenate((a,b))

# Output:

# [1 2 3 4]
# 15. Splitting Arrays
# a = np.array([1,2,3,4])

# np.split(a,2)

# Output:

# [array([1,2]), array([3,4])]
# 16. Random Numbers

# Used in ML and simulations.

# np.random.rand(3)
# np.random.randint(1,10,5)

# Example:

# [4 8 1 6 3]
# 17. Matrix Multiplication

# Very important for ML.

# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])

# A @ B

# Output:

# [[19 22]
#  [43 50]]
# 18. Useful Functions
# np.sqrt(a)
# np.exp(a)
# np.log(a)
# np.abs(a)
# 19. Find Positions
# a = np.array([10,20,30,40])

# np.where(a > 20)

# Output:

# (array([2,3]),)
# 20. Sort Arrays
# a = np.array([5,2,8,1])

# np.sort(a)

# Output:

# [1 2 5 8]
# Beginner Roadmap

# Master these topics in order:

# Creating arrays
# Shape, size, dimensions
# Indexing and slicing
# Arithmetic operations
# Aggregations (sum, mean, max, min)
# Boolean filtering
# Reshape and transpose
# Concatenate and split
# Random numbers
# Matrix multiplication