# imports
import matplotlib.pyplot as plt
import numpy as np

# random numbers following the normal model
x = np.random.randn(3000)
# creates histogram with x passed in
plt.hist(x, bins = 20, color = "g")
# show the histogram
plt.show()
