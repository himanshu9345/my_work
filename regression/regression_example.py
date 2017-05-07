import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

data = pd.read_csv('data1.txt', sep=" ", header = None)
values_x=data[1]
values_y=data[2]
values_y=values_y.reshape(-1,1) #   converting it to single feature matrix
values_x=values_x.reshape(-1,1)
reg=linear_model.LinearRegression()
reg.fit(values_x,values_y)
differenct = reg.predict(values_x)-values_y
plt.scatter(values_x,values_y)
plt.plot(values_x,reg.predict(values_x))
plt.show()
