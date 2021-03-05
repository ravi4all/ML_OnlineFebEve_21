import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
axes = fig.add_subplot(projection='3d')

x = np.arange(1,11)
y = [2,3,5,7,9,23,4,20,6,10]
z = x ** 2

'''
axes.scatter(x,y,z)
'''

dx = np.ones(10) * 2
dy = np.ones(10) * 2
dz = np.arange(1,11)
axes.bar3d(x,y,z,dx,dy,dz)

axes.set_xlabel('x axis')
axes.set_ylabel('y axis')
axes.set_zlabel('z axis')
plt.show()




