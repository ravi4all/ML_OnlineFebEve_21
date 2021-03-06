import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd

fig = plt.figure()
axes = fig.add_subplot(projection='3d')

df = pd.read_csv('student.csv')
x = df.iloc[:, 0]
y = df.iloc[:, 1]
z = df.iloc[:, 2]

axes.scatter(x,y,z)

axes.set_xlabel('x axis')
axes.set_ylabel('y axis')
axes.set_zlabel('z axis')
plt.show()




