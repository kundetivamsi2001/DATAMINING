import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#reading a dataset
df=pd.read_csv('D:\Data Analytics\stud_dataset.csv')
x=np.array(df['Attendence_rate(%)']).reshape(-1,1)
y=np.array(df['Marks_rate(%)'])
print(x,y)
#Creating an object for LinearRegression class
model=LinearRegression()
model.fit(x,y)
result=model.score(x,y)
print('score is:',result)
y_prct=model.predict(x)
print('actual values of y:',y)
print('pridicted values of y:',y_prct)
plt.plot(x,y_prct,color='blue',marker='o')
plt.scatter(x,y,color='green',marker='*')
plt.title('LINEAR REGRESSION')
plt.xlabel('Attendence rate in(%)')
plt.ylabel('Marks_rate in (%)')
plt.show()

