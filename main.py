import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ("input.csv", sep=';', header=None)
data.columns = ["x", "y"]
data = data.drop(labels = [0,1])
print(data)
x = data.x
y = data.y
x = list(x)
y = list(y)
x = [w.replace(',', '.') for w in x]
y = [w.replace(',', '.') for w in y]
x = [float(i) for i in x]
y = [float(i) for i in y]

plt.scatter(x,y)
plt.title('Input data plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.xlim(0,1)
plt.ylim(0,1)
plt.grid()
plt.show()