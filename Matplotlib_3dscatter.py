# imports
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D

x = np.random.randn(200)
y = np.random.randn(200)
z = np.random.randn(200)

fig = plt.figure()
chart = fig.add_subplot(1,1,1,projection="3d")

colors=np.random.randn(200)
size=200*np.random.randn(200)

chart.scatter(x,y,z,c = colors, s = size)
plt.show()