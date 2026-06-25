
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Product Data

products = ['Laptop'  , 'Phone' , 'Headphones' , 'Mouse' , 'Keyboard']
prices = np.array([50000, 20000 , 2000 , 500 , 1000])
qt_sold = np.array([10 , 15 , 25 , 30  , 20])

# Create DataFrame

df = pd.DataFrame({

    'Product': products,
    'Price': prices,
    'Quantity Sold': qt_sold

})

# Calculate Revenue

df['Revenue'] = df['Price'] * df['Quantity Sold']

# Display Data

print("\nE-Commerce Sales Data")
print(df)

# Total Revenue

total_rev = df['Revenue'].sum()
print("Total Revenue =", total_rev)

# Best Selling Product

best_product = df.loc[df['Quantity Sold'].idxmax()]
print("\nBest Selling Product =", best_product['Product'])

# Highest Revenue Product

highest_revenue = df.loc[df['Revenue'].idxmax()]
print("Highest Revenue Product =", highest_revenue['Product'])

# Revenue figure

plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Revenue'])
plt.title("E-Commerce Revenue Analysis")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.show()
