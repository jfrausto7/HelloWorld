# imports
from tkinter import *

# init root
root = Tk()

# frames
topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side = BOTTOM)

# labels
theLabel = Label(root, text="This is our Tkinter window")
theLabel.pack()
labelTwo = Label(root, text="This is our second sentence")
labelTwo.pack()

# buttons
theButton = Button(None, text="Click Here", fg="blue")
theButton.pack(fill = X)
buttonTwo = Button(None, text="Hello!", fg="red")
buttonTwo.pack(side=RIGHT, fill = Y)

# check button
cbutton = Checkbutton(root, text = "Remember name")
cbutton.pack()

# entry
entrySpace = Entry(root)
entrySpace.pack()

# mainloop function
root.mainloop()

