# imports
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D

# initialize figure
fig = plt.figure()

# chart is 3D bc of three parameters
chart = fig.add_subplot(1,1,1, projection = "3d")
plt.plot([1,2,2,4,1],[3,4,4,1,2],[3,5,4,2,5])


# show the actual chart
plt.show()