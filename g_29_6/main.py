# polynomical regression
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# data
df = pd.DataFrame({
    "Experience":[1,2,3,4,5]
})
x = df
y = [10, 20, 50, 90, 150]
 
# poly feature
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
print(x_poly)
 
# model
model = LinearRegression()
model.fit(x_poly,y)
 
# prediction
input_data  = int(input('Enter the experience: '))
new_data = pd.DataFrame({
    "Experience":[input_data]
})
 
# convert new data to poly
u_new_data = poly.fit_transform(new_data)
predicted_data = model.predict(u_new_data)
print(predicted_data[0])
 
 # poly reg -> over fitting
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
 
df = pd.DataFrame({
    "label":[1,2,3,4,5]
})
x = df
y = [10, 20, 50, 90, 150]
 
# poly convert
poly  = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)
 
# model
model = LinearRegression()
model.fit(x_poly,y)
 
# predict
input_data = int(input('enter the label: '))
new_data = pd.DataFrame({
    "label":[input_data]
})
 
# input data to poy
u_new_data = poly.fit_transform(new_data)
 
# prediction
predicted_data = model.predict(u_new_data)
print(predicted_data[0])
 

 # classification  -> decision tree
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
 
df = pd.DataFrame({
    "Weight": [120, 140, 150, 170],
    "Size": [6, 7, 7, 8]
})
x = df
y = ["Apple", "Apple", "Orange", "Orange"]
 
# model
model = DecisionTreeClassifier()
model.fit(x,y)
 
#prediction data
input_weight = int(input('enter the weight: '))
input_size = int(input('enter the size: '))
new_data = pd.DataFrame({
    "Weight": [input_weight],
    "Size": [input_size]
})
 
# prediction
predicted_data = model.predict(new_data)
print(predicted_data[0])
 

 # pass 40 above -> pass | less than 40 fail
 
df = pd.DataFrame({
    "marks":[10,20,25,39,40,55,70,80],
    "result":['fail','fail','fail','fail','pass','pass','pass','pass']
})
x = df[['marks']]
y = df['result']
 
# model dec
model = DecisionTreeClassifier()
model.fit(x,y)
 
# prediction data
input_marks = int(input('enter the marks: '))
new_data = pd.DataFrame({
    "marks":[input_marks]
})
 
# prediction
model_predict = model.predict(new_data)
print(model_predict[0])
 # Logistic Regression
from sklearn.linear_model import LogisticRegression
import pandas as pd
 
X = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6]
})
 
y = [0, 0, 0, 1, 1, 1]
 
model = LogisticRegression()
 
model.fit(X, y)
# new data
new_data = pd.DataFrame({
    "Hours":[7]
})
 
print(model.predict(new_data))
 