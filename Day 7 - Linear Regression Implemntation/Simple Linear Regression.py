#Author : Vicky
#For Full explaination of code go to #https://innovitronics.blogspot.com/2020/06/simple-and-multiple-linear-regression.html
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df= pd.read_csv('C://Users//Vicky//Downloads//MyLinearData.txt')
print(df)
#https://innovitronics.blogspot.com/2020/06/simple-and-multiple-linear-regression.html
plt.ylabel('SALARY')
plt.xlabel('AGE')
plt.scatter(df.Age,df.Salary,color='red')
plt.show()
regmod = LinearRegression()
regmod.fit(df[['Age']],df.Salary)plt.ylabel('SALARY')
plt.xlabel('AGE')
#https://innovitronics.blogspot.com/2020/06/simple-and-multiple-linear-regression.html
plt.scatter(df.Age,df.Salary,color='red')
plt.plot(df.Age,regmod.predict(df[['Age']]))
plt.show()
predicted_salary=regmod.predict(np.array([47]).reshape(1, 1))
print(predicted_salary)
r_sq = regmod.score(df[['Age']],df.Salary)
print(r_sq)
#https://innovitronics.blogspot.com/2020/06/simple-and-multiple-linear-regression.html
