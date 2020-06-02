#Author : Vicky
#For Full explaination of code go to #https://innovitronics.blogspot.com/2020/06/simple-and-multiple-linear-regression.html
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#For Full explaination of code go to #https://innovitronics.blogspot.com/2020/06/simple-and-multiple-linear-regression.html
df2= pd.read_csv('C://Users//Vicky//Downloads//Refactored_Py_DS_ML_Bootcamp-master//11-Linear-Regression//HousingData.csv')
print(df2.head())
print(df2.columns)
from sklearn.model_selection import train_test_split
X=df2[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Area Population']]
y=df2['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
regmod2 = LinearRegression()
regmod2.fit(X_train,y_train)
predicted_Price=model.predict(X_test)
print(predicted_Price)
#https://innovitronics.blogspot.com/2020/06/simple-and-multiple-linear-regression.html
