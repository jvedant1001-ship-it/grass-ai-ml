# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]    #X CORD
# y = [1, 4, 9, 16]    #Y CORD

# plt.plot(x, y)
# plt.title("My First Plot")  #TITLE
# plt.xlabel("X")    #LINE GRAPH
# plt.ylabel("Y")  #LINE GRAPH
# plt.show()  #GRAPH SHOWS



# Matplotlib is a large library, so "everything" would fill a book. A practical way to learn it is to start with the 20% that covers 80% of common plotting tasks.

# What Matplotlib Is

# Matplotlib is Python's most widely used plotting library. It can create:

# Line charts
# Bar charts
# Histograms
# Scatter plots
# Pie charts
# Subplots (multiple graphs)
# Heatmaps
# 3D plots
# Scientific visualizations

# Most people use:

# import matplotlib.pyplot as plt

# pyplot is the main plotting interface.

# The Basic Structure

# Almost every plot follows this pattern:

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x, y)

# plt.title("Graph Title")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")

# plt.show()

# Think of it as:

# Create data
# Draw plot
# Add labels
# Display
# Line Plot

# Most common graph.

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 15, 30]

# plt.plot(x, y)

# plt.show()
# Customize Line Plot
# plt.plot(
#     x,
#     y,
#     color="red",
#     linestyle="--",
#     linewidth=3,
#     marker="o"
# )

# Common colors:

# "red"
# "blue"
# "green"
# "black"
# "yellow"

# Common line styles:

# "-"
# "--"
# ":"
# "-."

# Markers:

# "o"
# "s"
# "^"
# "*"
# "x"
# Titles and Labels
# plt.title("Sales Report")
# plt.xlabel("Months")
# plt.ylabel("Revenue")
# Grid
# plt.grid(True)
# Figure Size
# plt.figure(figsize=(8, 5))

# Width = 8

# Height = 5

# Bar Chart
# import matplotlib.pyplot as plt

# subjects = ["Math", "Science", "English"]
# marks = [85, 90, 78]

# plt.bar(subjects, marks)

# plt.show()

# Horizontal bar:

# plt.barh(subjects, marks)
# Histogram

# Shows data distribution.

# import matplotlib.pyplot as plt

# data = [10,12,15,15,16,18,20,22]

# plt.hist(data)

# plt.show()

# Bins:

# plt.hist(data, bins=5)
# Scatter Plot

# Relationship between two variables.

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [10,20,25,30,40]

# plt.scatter(x, y)

# plt.show()

# Customize:

# plt.scatter(
#     x,
#     y,
#     color="red",
#     s=100
# )

# s controls point size.

# Pie Chart
# import matplotlib.pyplot as plt

# sizes = [30, 40, 20, 10]
# labels = ["A", "B", "C", "D"]

# plt.pie(
#     sizes,
#     labels=labels,
#     autopct="%1.1f%%"
# )

# plt.show()
# Multiple Lines
# x = [1,2,3,4]

# y1 = [10,20,30,40]
# y2 = [15,25,35,45]

# plt.plot(x, y1, label="Team A")
# plt.plot(x, y2, label="Team B")

# plt.legend()

# plt.show()
# Legend
# plt.legend()

# Shows label descriptions.

# Subplots

# Multiple graphs in one figure.

# import matplotlib.pyplot as plt

# plt.subplot(1, 2, 1)
# plt.plot([1,2,3], [1,4,9])

# plt.subplot(1, 2, 2)
# plt.bar(["A","B","C"], [10,20,30])

# plt.show()

# Meaning:

# 1 row
# 2 columns
# 1st graph

# and

# 1 row
# 2 columns
# 2nd graph
# Object-Oriented Style (Professional Way)

# Instead of:

# plt.plot(...)

# Use:

# fig, ax = plt.subplots()

# ax.plot([1,2,3], [1,4,9])

# ax.set_title("Graph")

# plt.show()

# This is preferred for larger projects.

# Saving Charts
# plt.savefig("chart.png")

# High quality:

# plt.savefig(
#     "chart.png",
#     dpi=300
# )

# PDF:

# plt.savefig("chart.pdf")
# Working with NumPy

# You'll often combine Matplotlib with NumPy.

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 10, 0.1)

# y = x**2

# plt.plot(x, y)

# plt.show()
# Working with Pandas

# Often combined with pandas.

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("data.csv")

# plt.plot(df["Year"], df["Sales"])

# plt.show()
# Most Important Functions to Memorize
# plt.plot()
# plt.scatter()
# plt.bar()
# plt.barh()
# plt.hist()
# plt.pie()

# plt.title()
# plt.xlabel()
# plt.ylabel()

# plt.legend()
# plt.grid()

# plt.figure()

# plt.subplot()
# plt.subplots()

# plt.savefig()

# plt.show()
# Typical Data Science Workflow
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("sales.csv")

# plt.figure(figsize=(8,5))

# plt.plot(
#     df["Month"],
#     df["Sales"],
#     marker="o"
# )

# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.grid(True)

# plt.show()
# Learning Path
# Line plots
# Scatter plots
# Bar charts
# Histograms
# Pie charts
# Legends and labels
# Figure customization
# Subplots
# NumPy integration
# Pandas integration
# Object-oriented Matplotlib (fig, ax = plt.subplots())
# import matplotlib.pyplot as plt

# # X-axis values
# x = [1, 2, 3, 4, 5]

# # Y-axis values for two lines
# y1 = [10, 50, 80, 20, 100]
# y2 = [15, 85, 55, 25, 95]

# # First line (Blue)
# plt.plot(
#     x,
#     y1,
#     color="blue",
#     marker="o",
#     linewidth=2,
#     label="Team A"
# )

# # Second line (Red)
# plt.plot(
#     x,
#     y2,
#     color="red",
#     marker="s",
#     linewidth=2,
#     label="Team B"
# )

# # Title and labels
# plt.title("Comparison between REAL MADRID and FC BARCELONA ")
# plt.xlabel("REAL MADRID")
# plt.ylabel("FC BARCELONA")

# # Grid
# plt.grid(True)

# # Legend
# plt.legend()

# # Show graph
# plt.show()
# import matplotlib.pyplot as plt  #visualization
# x=[2010,2015,2020,2025] #x coordinate
# y1=[100,120,230,300]#y coordinate
 
# y2=[150,180,185,300]
# plt.plot(x,y1,label='jeans',color='green',marker='o',linestyle='dashed',linewidth=4,markersize=14)
 
# plt.plot(x,y2,label='shirt',color='red',marker='o',linestyle='-',linewidth=2,markersize=10)
 
# plt.ylabel("sales")
# plt.xlabel("years")
# plt.title("sales report")
# plt.legend()
# plt.show()
 
 # bar chart
import matplotlib.pyplot as plt
x = [2015,2020,2025,2030]
y = [100,150,200,290]
 
plt.bar(x,y)
# size
plt.figure(figsize=(6,2))
plt.show()