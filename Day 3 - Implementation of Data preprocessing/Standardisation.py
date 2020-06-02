#Author : Vicky
#Find the full explanaitoin on
#https://innovitronics.blogspot.com/2020/05/a-quick-guide-to-imputation-python-data.html
import pandas as pd
import numpy as np
import sklearn
MyData = pd.read_csv('C://Users//Vicky//Downloads//MyData.txt')
from sklearn.preprocessing import StandardScaler
std=StandardScaler()
stddata=std.fit_transform(MyData.iloc[: , 1:3])
print(stddata)
#https://innovitronics.blogspot.com/2020/05/a-quick-guide-to-imputation-python-data.html
