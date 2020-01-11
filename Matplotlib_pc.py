# imports
import matplotlib.pyplot as plt
import numpy as np

# figure setup
plt.figure(figsize=(5,5))

# initial data
labels = ["USA", "India", "China", "Italy", "Canada"]
values = [25,10,15,40,23]
explode = [.1, 0, .05, .05, 0]

plt.pie(values, labels=labels, autopct= "%.1f", explode=explode)

# show the pie chart
plt.show()