
# Think of Pandas as the tool that turns Python from a programming language into something you can use to work with spreadsheets, databases, CSV files, and real-world datasets.

# If you're heading into AI/ML, Pandas is one of the first libraries you should become comfortable with because 80% of ML work is cleaning and preparing data, not training models.

# What is Pandas?

# Pandas lets you:

# Read CSV/Excel files
# Filter rows
# Select columns
# Clean missing data
# Calculate statistics
# Group data
# Merge datasets
# Prepare data for machine learning

# Imagine you have this CSV:

# Name	Age	Salary
# Alice	25	50000
# Bob	30	60000
# Charlie	28	55000

# Without Pandas, handling thousands of rows is painful.

# With Pandas:

# import pandas as pd

# df = pd.read_csv("employees.csv")
# print(df)

# Boom. Entire spreadsheet becomes a Python object.

# The Most Important Object: DataFrame

# Everything revolves around a DataFrame.

# Think:

# Excel Sheet = DataFrame
# SQL Table = DataFrame

# Example:

# import pandas as pd

# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 28]
# }

# df = pd.DataFrame(data)

# print(df)

# Output:

#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   28

# The variable df is your DataFrame.

# Viewing Data
# First few rows
# df.head()

# Output:

# Name     Age
# Alice    25
# Bob      30
# ...

# Default is first 5 rows.

# Last rows
# df.tail()
# Information about dataset
# df.info()

# Shows:

# Number of rows
# Number of columns
# Data types
# Missing values

# This is one of the first commands data scientists run.

# Selecting Columns

# Suppose:

# df
# Name	Age	Salary
# Alice	25	50000
# Bob	30	60000

# Get one column:

# df["Name"]

# Output:

# Alice
# Bob

# Multiple columns:

# df[["Name", "Salary"]]
# Filtering Rows

# Very important.

# Get people older than 25:

# df[df["Age"] > 25]

# Output:

# Bob
# Charlie

# Salary greater than 50000:

# df[df["Salary"] > 50000]

# Multiple conditions:

# df[(df["Age"] > 25) & (df["Salary"] > 50000)]
# Adding Columns

# Create new column:

# df["Bonus"] = df["Salary"] * 0.10

# Now:

# Name	Salary	Bonus
# Alice	50000	5000
# Statistics

# Average:

# df["Salary"].mean()

# Maximum:

# df["Salary"].max()

# Minimum:

# df["Salary"].min()

# Everything at once:

# df.describe()

# Shows:

# mean
# std
# min
# max
# quartiles

# Very common in ML projects.

# Handling Missing Data

# Real datasets are messy.

# Example:

# Name	Age
# Alice	25
# Bob	NaN
# Charlie	28

# Find missing values:

# df.isnull().sum()

# Remove rows with missing values:

# df.dropna()

# Fill missing values:

# df["Age"].fillna(df["Age"].mean())

# Common ML preprocessing step.

# Sorting Data

# Sort by age:

# df.sort_values("Age")

# Descending:

# df.sort_values("Age", ascending=False)
# Group By (Super Important)

# Imagine sales data:

# Product	Sales
# Phone	100
# Laptop	200
# Phone	150

# Group:

# df.groupby("Product")["Sales"].sum()

# Output:

# Phone     250
# Laptop    200

# This is used constantly in analytics.

# Reading Files

# CSV:

# df = pd.read_csv("data.csv")

# Save CSV:

# df.to_csv("output.csv")

# Excel:

# df = pd.read_excel("data.xlsx")
# Combining DataFrames

# Dataset 1:

# ID	Name
# 1	Alice

# Dataset 2:

# ID	Salary
# 1	50000

# Merge:

# pd.merge(df1, df2, on="ID")

# Result:

# ID	Name	Salary
# 1	Alice	50000

# This is basically SQL JOINs inside Python.

# Pandas + Machine Learning Workflow

# A typical ML project looks like:

# import pandas as pd

# # Read data
# df = pd.read_csv("data.csv")

# # Explore
# df.head()

# # Clean
# df.dropna()

# # Create features
# df["new_column"] = ...

# # Select inputs
# X = df[["age", "salary"]]

# # Select target
# y = df["price"]

# # Train model