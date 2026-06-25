# # # import pandas as pd 
# # # d={
# # #     "name":["vishal","virat","vineet"],
# # #     "salary":[100,200,300]
# # # }


# # # df= pd.DataFrame(data=d)

# # # df = pd.DataFrame(data=d)

# # # df["holidays"] = df["salary"] / 100

# # # df["decrement"] = [10,20,30]


# # # delete column
# # # df.drop(["salary","name"],axis=1,inplace=True)


# # # print(df)
# # # print(df.loc[2,"name"])
# # # print(df.iloc[2,0])


# # #gets single  row using loc
# # # print(df.loc[1])


# # # get muktiple rows
# # # print(df.iloc[0:3])
# # # print(df.loc[0:3])


# # #getting sub data

# # # print(df.iloc[0])      # first row
# # # print(df.loc[0])       # row with label 0

# # # print(df.iloc[:, 1])   # second column
# # # print(df.loc[:, "salary"])  # salary column




# # import pandas as pd

# # data = {
# #     "emp id": [101, 102, 103, 104, 105, 106],
# #     "name": ["amit", "riya", "raj", "sara", "john", "neha"],
# #     "department": [50000, 45000, 60000, 55000, 48000, 52000],
# #     "experience": [2, 3, 5, 4, 1, 3]
# # }

# # df = pd.DataFrame(data)
# # print(df)

# # # delete column
# # # df.drop(["salary","name"],axis=1,inplace=True)


# # print(df)
# # print(df.loc[2,"name"])
# # print(df.iloc[2,0])


# # # gets single  row using loc
# # print(df.loc[1])


# # # get muktiple rows
# # print(df.iloc[0:3])
# # print(df.loc[0:3])


# # # getting sub data

# # print(df.iloc[0])      # first row
# # print(df.loc[0])       # row with label 0

# # print(df.iloc[:, 1])   # second column
# # print(df.loc[:, "salary"])  # salary column

# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
# df = pd.read_json(url)
# # filter 1
# # df[df["english"] == 95]
 
# # filter 2
# print(df[df["maths"] < 60])