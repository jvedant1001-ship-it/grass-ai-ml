import pandas as pd 
url
df=pd.read_json(url)
#by default ascending
df.sort_values("english")


#descending

df.sort_values("english",ascending=False,inplace=True)
print(df)


#multiple cols sort 

df.sort_values(by=['english','maths'],)


# If you're learning Pandas, these are some of the most important commands you'll use regularly:

# 1. Import Pandas
import pandas as pd
# 2. Read Data
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
# 3. View Data
df.head()      # First 5 rows
df.tail()      # Last 5 rows
df.sample(5)   # Random 5 rows
# 4. Basic Information
df.shape       # Rows and columns
df.columns     # Column names
df.info()      # Data types and null counts
df.describe()  # Statistical summary
# 5. Select Data
df["name"]                 # Single column
df[["name", "age"]]        # Multiple columns
df.iloc[0]                 # First row by position
df.loc[0]                  # Row by label
# 6. Filter Rows
df[df["age"] > 25]
df[df["city"] == "Delhi"]
df[(df["age"] > 25) & (df["salary"] > 50000)]
# 7. Handle Missing Values
df.isnull().sum()          # Count missing values
df.dropna()                # Remove rows with nulls
df.fillna(0)               # Replace nulls with 0
# 8. Create or Modify Columns
df["bonus"] = df["salary"] * 0.1
df["name"] = df["name"].str.upper()
# 9. Sort Data
df.sort_values("salary")
df.sort_values("salary", ascending=False)
# 10. Group By
df.groupby("department")["salary"].mean()
df.groupby("department").agg({
    "salary": "mean",
    "age": "max"
})
# 11. Count Unique Values
df["city"].unique()
df["city"].nunique()
df["city"].value_counts()
# 12. Rename Columns
df.rename(columns={"old_name": "new_name"})
# 13. Drop Columns or Rows
df.drop("salary", axis=1)  # Drop column
df.drop(0, axis=0)         # Drop row
# 14. Merge DataFrames
pd.merge(df1, df2, on="id")
# 15. Save Data
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
# Top 10 Commands for Interviews
df.head()
df.info()
df.describe()
df.shape
df.columns
df.isnull().sum()
df.groupby()
df.sort_values()
df.value_counts()
pd.merge()
# These cover about 80% of real-world Pandas work in data analysis and data science interviews.

