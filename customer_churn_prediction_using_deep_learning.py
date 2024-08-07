

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df=pd.read_csv("/content/WA_Fn-UseC_-Telco-Customer-Churn.csv")

df.head()

df.drop("customerID",axis=1,inplace=True)

df.info()

pd.to_numeric(df.TotalCharges,errors='coerce').isnull()

df[pd.to_numeric(df.TotalCharges,errors='coerce').isnull()]

df.shape

df.iloc[488]

df1=df[df['TotalCharges']!=' ']

df1.shape

df1['TotalCharges']=pd.to_numeric(df1['TotalCharges'])

df1['TotalCharges'].dtypes

df1[df1['Churn']=='No']

tenure_churn_no=df1[df1.Churn=='No'].tenure

tenure_churn_yes=df1[df1.Churn=='Yes'].tenure

tenure_churn_yes

plt.xlabel('Tenure')
plt.ylabel("Number of Customers")
plt.title("Customer Churn Prediction Visualization")
plt.hist([tenure_churn_yes,tenure_churn_no],color=['green','red'],label=['Churn=Yes','Churn=No'])
plt.legend()

mc_churn_no=df1[df1["Churn"]=='No'].MonthlyCharges
mc_churn_yes=df1[df1["Churn"]=="Yes"].MonthlyCharges


plt.xlabel('MonthlyChararges')
plt.ylabel("Number of Customers")
plt.title("Customer Churn Prediction Visualization")
blood_sugar_men=[113,85,90,150,149,88,93,115,135,80,77,82,129]
blood_sugar_women=[67,98,89,120,133,150,84,69,89,79,120,112,100]
plt.hist([mc_churn_yes,mc_churn_no],color=['green','red'],label=['Churn=Yes','Churn=No'])
plt.legend()

def print_unique_col(df):
  for column in df:
    if df[column].dtypes=='object':
      print(f'{column}: {df[column].unique()}')

df1.replace('No internet service','No',inplace=True)
df1.replace('No phone service','No',inplace=True)

print_unique_col(df1)

yes_no_columns=['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','Churn']
for col in yes_no_columns:
  df1[col].replace({'Yes':1,'No':0},inplace=True)

for col in df1:
  print(f'{col}:{df1[col].unique()}')

df1['gender'].replace({'Female':1,'Male':0},inplace=True)

df1['gender'].unique()

df2=pd.get_dummies(data=df1,columns=['InternetService','Contract','PaymentMethod'])

df2.columns

df2.dtypes

cols_to_scale=['tenure','MonthlyCharges','TotalCharges']
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
df2[cols_to_scale]=scaler.fit_transform(df2[cols_to_scale])

df2.sample

X=df2.drop('Churn',axis='columns')
y=df2['Churn']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=5)

X_train.shape

X_test.shape

X_train[:10]

len(X_train.columns)

import tensorflow as tf
from tensorflow import keras

model=keras.Sequential([
    keras.layers.Dense(26,input_shape=(26,),activation='relu'),
    keras.layers.Dense(15,input_shape=(26,),activation='relu'),
    keras.layers.Dense(1,activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.fit(X_train,y_train,epochs=20)

model.evaluate(X_test,y_test)

yp=model.predict(X_test)
yp[:5]

y_test[:5]

y_pred=[]
for element in yp:
  if element>0.5:
    y_pred.append(1)
  else:
    y_pred.append(0)

y_pred[:5]

from sklearn.metrics import confusion_matrix,classification_report
print(classification_report(y_test,y_pred))

cm=tf.math.confusion_matrix(labels=y_test,predictions=y_pred)
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

