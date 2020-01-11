# imports
import matplotlib.pyplot as plt
import numpy as np

# random data
x = np.random.randn(100)
y = np.random.randn(100)

# size and color
size = 50*np.random.randn(100)
colors = np.random.randn(100)

# actual scatterplot itself
plt.scatter(x,y, s=size, c =colors, marker= "s")

plt.show()