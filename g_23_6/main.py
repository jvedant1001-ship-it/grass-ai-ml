import pandas as pd
 
data = {
    'Name':['Ram','Kamal','Ajay'],
    'Age':[25,None,32],
    'Salary':[5000,6000,None]
}
df = pd.DataFrame(data)
print("Original Dataframe")
print(df)
 
# null findoud | fillna | dropna
print(df.isnull().sum()) # sum of null
 
df_drop = df.dropna()
print(df_drop)
 
# fillna
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)
 # handle missing values
import pandas as pd
 
data = {
    'Name':['Ram','Kamal','Ajay'],
    'Age':[25,None,32],
    'Salary':[5000,6000,None]
}
df = pd.DataFrame(data)
print("Original Dataframe")
print(df)
 
# null findoud | fillna | dropna
print(df.isnull().sum()) # sum of null
 
df_drop = df.dropna()
print(df_drop)
 
# fillna
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)
 # encoding
from sklearn.preprocessing import LabelEncoder
import pandas as pd
 
data = {
    'Name':['Ram','Kamal','Ajay','Neetu','Kavi','Sapu'],
    'Age':[25,None,32,20,21,22],
    'Salary':[5000,6000,None,7000,8000,9000],
    'Gender':['male','male','male',None,'female','female']
}
 
df = pd.DataFrame(data)
print("original dataframe")
print(df)
 # label encoding
from sklearn.preprocessing import LabelEncoder
import pandas as pd
 
data = {
    'Name':['Ram','Kamal','Ajay','Neetu','Kavi','Sapu'],
    'Age':[25,None,32,20,21,22],
    'Salary':[5000,6000,None,7000,8000,9000],
    'Gender':['male','male','male',None,'female','female']
}
df = pd.DataFrame(data)
print("original dataframe")
print(df)
# label encoder
le = LabelEncoder()
df_label = df.copy()
df_label['Gender'] = df['Gender'].fillna('unknown')
df_label['Gender_encoder'] = le.fit_transform(df_label['Gender'])
 
print("After label encoding:")
print(df_label)
 
 