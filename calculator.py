"""A simple calculator app with a Tkinter GUI"""

# imports
from tkinter import *

# init root
root = Tk()

equa = ""

equation = StringVar()

calculation = Label(root, textvariable = equation)

equation.set("Enter an equation")

calculation.grid(columnspan = 4)

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""

def clearPress():
    global equa
    equa = ""
    equation.set("")

Button0 = Button(root,text = "0", command = lambda: btnPress(0))
Button0.grid(row = 1, column = 0)
Button1 = Button(root,text = "1", command = lambda: btnPress(1))
Button1.grid(row = 1, column = 1)
Button2 = Button(root,text = "2", command = lambda: btnPress(2))
Button2.grid(row = 1, column = 2)
Button3 = Button(root,text = "3", command = lambda: btnPress(3))
Button3.grid(row = 2, column = 0)
Button4 = Button(root,text = "4", command = lambda: btnPress(4))
Button4.grid(row = 2, column = 1)
Button5 = Button(root,text = "5", command = lambda: btnPress(5))
Button5.grid(row = 2, column = 2)
Button6 = Button(root,text = "6", command = lambda: btnPress(6))
Button6.grid(row = 3, column = 0)
Button7 = Button(root,text = "7", command = lambda: btnPress(7))
Button7.grid(row = 3, column = 1)
Button8 = Button(root,text = "8", command = lambda: btnPress(8))
Button8.grid(row = 3, column = 2)
Button9 = Button(root,text = "9", command = lambda: btnPress(9))
Button9.grid(row = 4, column = 0)
plus = Button(root,text = "+", command = lambda: btnPress("+"))
plus.grid(row = 1, column = 3)
minus = Button(root,text = "-", command = lambda: btnPress("-"))
minus.grid(row = 2, column = 3)
multiply = Button(root,text = "*", command = lambda: btnPress("*"))
multiply.grid(row = 3, column = 3)
divide = Button(root,text = "/", command = lambda: btnPress("/"))
divide.grid(row = 4, column = 3)
equal = Button(root,text = "=", command = EqualPress)
equal.grid(row = 4, column = 1)
c = Button(root,text = "C", command = clearPress)
c.grid(row = 4, column = 2)




root.mainloop()