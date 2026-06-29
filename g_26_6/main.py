#project using mysql and joblib and SLR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# mysql connector
!pip install pymysql cryptography
import pymysql
conn = pymysql.connect(host="13.220.156.88",user="mluser",database="ml_db",password="mlpass123")
print(conn)
query = "select avg_income,house_age,num_rooms,price from houses"
df = pd.read_sql(query,conn)
print(df)


# mysql connector
# !pip install mysql.connector
import mysql.connector
conn = mysql.connector.connect(host="13.220.156.88",user="mluser",database="ml_db",password="mlpass123")
query = "select avg_income,house_age,num_rooms,price from houses"
df = pd.read_sql(query,conn)
print(df)

data = {
    "name":['vedant','alibaba','kamra','samay'],
    "avg_income":[1000,800,850,9500],
    "house_age":[10.2,2.5,3.0,4.0],
    "num_rooms":[3,4,5,1],
    "price":[10000,7000,5000,11000],
}

# data frame
df = pd.DataFrame(data)

#handle missing value

#future scaling
scaler = StandardScaler()
df[['avg_income' , 'house_age', 'num_rooms']] = scaler.fit_transform(df[['avg_income','house_age','num_rooms']])
print(df)

# split data
x = df[['avg_income' , 'house_age', 'num_rooms']] 
y = df['price']

# train test split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=2
)

# model train

model = LinearRegression()
model.fit(x_train,y_train)

# prediction

new_data = pd.DataFrame({
     "avg_income":[900],
    "house_age":[8],
    "num_rooms":[5],
    })

new_data=scaler.transform(new_data)


prediction = model.predict(new_data)
print(prediction)

#model dump
# pip install joblib

import joblib
joblib.dump(model,"house_prediction.joblib")

