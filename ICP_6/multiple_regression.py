import numpy as np
import pandas as pd
from sklearn import linear_model,metrics
import matplotlib.pyplot as plt

dataset = pd.read_csv('weatherHistory.csv')
x_train = dataset.drop('Summary',axis=1)
y_train = dataset["Summary"]

nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending = False)[:25])

nulls.columns = ['Nullcount']
nulls.index.name = 'Feature'
#print(nulls)
# data = dataset.select_dtypes(include=[np.number]).interpolate().dropna()
# print(sum(data.isnull().sum()!=0))
#data = dataset.select_dtypes(exclude=[np.number])
#print(dataset.describe())
print(dataset.Temperature.value_counts(),'\n')




#x_test = dataset.copy()
#
# reg = linear_model.LinearRegression()
#
# reg.fit(x_train,y_train)
# print("Coefficients :\n" , reg.coef_)
#
# print('Varience Score :{}'.format(reg.score(x_test, y_train)))
#
# plt.style.use('fivethirtyeight')
# plt.scatter(reg.predict(x_train),reg.predict(x_train)-y_train,color = "blue", s =10, lable = 'test data')
#
# plt.hlines(y = 0, xmin = 0 ,xmax = 50, linewidth = 2)
# plt.legend(loc = 'upper right')
# plt.title("Resudial errors")
#
# plt.show()