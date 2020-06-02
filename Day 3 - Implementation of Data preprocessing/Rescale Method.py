#Author : Vicky
#Find the full explanaitoin on
#https://innovitronics.blogspot.com/2020/05/a-quick-guide-to-imputation-python-data.html
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
MyData = pd.read_csv('C://Users//Vicky//Downloads//MyData.txt')
norm = MinMaxScaler()
normdata = norm.fit_transform(MyData.iloc[: , 1:3])
print(normdata)
