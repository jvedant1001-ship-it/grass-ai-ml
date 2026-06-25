# import matplotlib.pyplot as plt


# # 1. Histogram

# data = [12, 15, 13, 17, 20, 22, 25, 18, 16, 14, 19, 21, 23, 24]

# plt.figure(figsize=(6, 4))
# plt.hist(data, bins=5, color='skyblue', edgecolor='black')
# plt.title("Histogram Example")
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.grid(True)
# plt.show()


# # 2. Pie Chart

# subjects = ["Python", "Java", "C++", "JavaScript"]
# students = [40, 25, 20, 15]

# plt.figure(figsize=(6, 6))
# plt.pie(
#     students,
#      labels=subjects,
#      autopct='%1.1f%%',
#      colors=['gold', 'lightgreen', 'lightcoral', 'lightskyblue'],
#      startangle=90
# )
# plt.title("Student Preference for Programming Languages")

# plt.show()


# # 3. Bar Chart

# products = ["Laptop", "Mobile", "Tablet", "Printer"]

# sales = [50, 80, 30, 20]

# plt.figure(figsize=(6, 4))
# plt.bar(products, sales, color='orange')
# plt.title("Product Sales")
# plt.xlabel("Products")
# plt.ylabel("Units Sold")
# plt.grid(axis='y')
# plt.show()

# Subplots in Matplotlib

# Subplots allow you to display multiple graphs in a single figure window. This is useful when comparing different charts side by side.

# import matplotlib.pyplot as plt

# # Data
# hist_data = [12, 15, 13, 17, 20, 22, 25, 18, 16, 14]
# subjects = ["Python", "Java", "C++", "JS"]
# students = [40, 25, 20, 15]
# products = ["Laptop", "Mobile", "Tablet", "Printer"]
# sales = [50, 80, 30, 20]

# # Create 1 row and 3 columns of subplots
# fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# # Histogram
# ax[0].hist(hist_data, bins=5, color='skyblue', edgecolor='black')
# ax[0].set_title("Histogram")
# ax[0].set_xlabel("Values")
# ax[0].set_ylabel("Frequency")

# # Pie Chart
# ax[1].pie(students, labels=subjects, autopct='%1.1f%%')
# ax[1].set_title("Pie Chart")

# # Bar Chart
# ax[2].bar(products, sales, color='orange')
# ax[2].set_title("Bar Chart")
# ax[2].set_xlabel("Products")
# ax[2].set_ylabel("Sales")

# plt.tight_layout()  # Adjust spacing automatically
# plt.show()

# mportant Subplot Functions
# Function	Purpose
# plt.subplots()	Create multiple plots
# figsize=(w,h)	Set figure size
# ax[i].plot()	Plot on a specific subplot
# ax[i].set_title()	Set subplot title
# ax[i].set_xlabel()	Set X-axis label
# ax[i].set_ylabel()	Set Y-axis label
# plt.tight_layout()	Prevent overlapping
# plt.suptitle()	Overall title for all subplots

# #subpolots2 3
# import matplotlib.pyplot as plt
# #graph 1
# year=[2010,2015,2020,2025]
# dairy=[100,520,630,400]

# #graph2
# farming=[300,200,250,100]

# # graph3
# college=[10,20,25,50]

# #graph 4
# transport=[50,75,100,150]


# fig,aux=plt.subplot(2,2)

# aux[0][0].plot(year,dairy)
# aux[0][0].set_xlabel("year")
# aux[0][0].set_ylabel("dairy")
# aux[0][0].set_title("dairy production")

import pandas as pd 
url=""
df = pd.read