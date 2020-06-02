#Author : Vicky
#Full explaination on 
#https://innovitronics.blogspot.com/2020/05/a-quick-guide-to-imputation-python-data.html
import pandas as pd
import numpy as np
import sklearn
MyData = pd.read_csv('C://Users//Vicky//Downloads//MyData.txt')
from sklearn.impute import SimpleImputer
#https://innovitronics.blogspot.com/2020/05/a-quick-guide-to-imputation-python-data.html
imputer1 = SimpleImputer(missing_values=np.nan,strategy='median')
imputer1.fit(MyData.iloc[:,1:2])
MyData.iloc[:,1:2]=imputer1.transform(MyData.iloc[:,1:2])
imputer2 = SimpleImputer(missing_values=np.nan,strategy='mean')
MyData.iloc[:,2:]=imputer2.fit_transform(MyData.iloc[:,2:])
print(MyData)
#https://innovitronics.blogspot.com/2020/05/a-quick-guide-to-imputation-python-data.html
