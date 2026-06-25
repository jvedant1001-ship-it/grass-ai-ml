# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["A", "B"],
#     "Age": [20, 21]
# })

# print(df)

# import sys
# print(sys.executable)

# csv jason excel



# import pandas as pd

# data = {
#     "emp id": [101, 102, 103, 104, 105, 106],
#     "name": ["amit", "riya", "raj", "sara", "john", "neha"],
#     "department": [50000, 45000, 60000, 55000, 48000, 52000],
#     "experience": [2, 3, 5, 4, 1, 3]
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.head())
# print(df.head(3))
# print(df.tail())
# print(df.tail(-3))
# print(df.tail(5))
# print(df.info)
# print(df.describe())

import pandas as pd
d = {
    "name":["vishal","virat","vineet"], # 3 rows
    "salary":[100,200,300] # 3 rows
}
df = pd.DataFrame(data=d)
# df["marks"] = [10,20,30]
df["marks"] = df["salary"] / 2
print(df)

import pandas as pd
df = pd.read_json("https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json")
df["marks"] = [10,20,30,40,50]
df["salary"]= [ 100,200,300,400,500]
df["marks"] = df["salary"] / 2
# print(df)
df["Increment"] = df["salary"]* 1.10
# print(df)
 
# column name change
df.rename(columns={"Increment":"salary_increment"},inplace=True)
print(df)