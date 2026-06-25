import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)



import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df.loc[4,"marks"] = np.nan
print(df)


df["marks"] = df["marks"].astype(object)
df.loc[df["name"] == "anjali", "marks"] = None
print(df)


df["marks"] = df["marks"].astype(object)
df.loc[df["name"] == "anjali", "marks"] = 'Null'
print(df)

df["roll_no"] = df["roll_no"].fillna(200)
df["marks"] = df["marks"].fillna(100)
print(df)

df.fillna({"roll no": 200, "marks": 100}, inplace=True)

 
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df["marks"] = df["marks"].fillna(100)
df["roll no"] = df["roll no"].fillna(200)
 
print(df)

df = df.fillna({"roll no": 200,"marks": 100}, inplace=True)
 
print(df)

nh = df["marks"].mean()
print(nh)
df["roll no"] = df["roll no"].fillna(nh)
print(df)




#Null --> kisi bhi data type me use hota h 
# NaN--> generally  numeric columns me use hota 


# AGGREGRATION
import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [80, 90, 70, 85],
    'Age': [20, 21, 19, 22]
}

df = pd.DataFrame(data)

print(df)

# Basic Aggregations
# Mean
print(df['Marks'].mean())
# Sum
print(df['Marks'].sum())
Maximum
print(df['Marks'].max())
# Minimum
print(df['Marks'].min())
# Count
print(df['Marks'].count())
# Multiple Aggregations with agg()
print(df['Marks'].agg(['mean', 'sum', 'min', 'max']))
# GroupBy Aggregation
# Suppose:

data = {
    'Department': ['IT', 'IT', 'HR', 'HR'],
    'Salary': [50000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

# Average salary by department:

result = df.groupby('Department')['Salary'].mean()

print(result)

# Multiple aggregations:

result = df.groupby('Department')['Salary'].agg(
    ['count', 'sum', 'mean', 'min', 'max']
)

print(result)
# Concatenate Rows (one DataFrame below another)
import pandas as pd

df1 = pd.DataFrame({
    'Name': ['A', 'B'],
    'Marks': [80, 90]
})

df2 = pd.DataFrame({
    'Name': ['C', 'D'],
    'Marks': [70, 85]
})

result = pd.concat([df1, df2])

print(result)