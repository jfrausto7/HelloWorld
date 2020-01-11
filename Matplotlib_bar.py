# imports
import matplotlib.pyplot as plt
import numpy as np

# set size
fig = plt.figure(figsize=(7,5))

# data
names = ["Scott", "Jacob", "Michael", "Brennan"]
scores = [88, 57, 92, 34]
# set positions based on length of scores array
positions = np.arange(len(scores))

# actual bar chart
plt.bar(positions, scores)
plt.xticks(positions, names)
# show bar chart
plt.show()