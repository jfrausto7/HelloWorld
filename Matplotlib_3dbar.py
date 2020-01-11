# imports
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import axis3d, Axes3D

fig = plt.figure()
chart = fig.add_subplot(1,1,1,projection="3d")

# positions
x = [1,2,3,4,5]
y = [2,4,5,2,4]
z = [0,0,0,0,0]

# width length and height
dx = [1,1,1,1,1]
dy = np.ones(5)
dz = [1,6,3,1,5]


chart.bar3d(x,y,z,dx,dy,dz)

# labels
chart.set_xlabel("X Label")
chart.set_ylabel("Y Label")
chart.set_zlabel("Z Label")

plt.show()
