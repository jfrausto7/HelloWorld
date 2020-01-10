# imports
import matplotlib.pyplot as plt
import numpy as np

# figures
fig = plt.figure(facecolor="green")
chart1 = fig.add_subplot(3,1,1)
chart2 = fig.add_subplot(3,1,2)
chart3 = fig.add_subplot(3,1,3,facecolor="black")

# range variable
x = np.arange(1,5)
# plot data
chart3.plot(x,x,x,x+1,x,x+2)
# you can also specify labels like this
chart2.plot(x-2,x*2,"-.","+",label="Stupid", color="purple")
chart1.plot(x+1,x+5,linestyle="-.",color="brown", label="stupid2",linewidth=3.0, marker="+")
# labels
plt.xlabel("This is the x-axis")
plt.ylabel("This is the y-axis")
# title
plt.title("This is the title of the graph")
# legend
plt.legend(["Slow", "Medium", "Fast","Stupid"], loc="upper left")
# axes
plt.axis([0,5,0,10])
# gridlines
plt.grid(True)
# show the graph
plt.show()
# save the graph
plt.savefig("firstgraph.png")
