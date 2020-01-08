def HelloWorld():
    print("Hello World")

#This is a comment. Wow! I know how to comment now.

"""
This is a block comment
So epic, that I can do this
Why is Python so similar to Java
Lol
"""
#Call a function below
HelloWorld()

#Function for greeting
def UserInput(name):
    print("Hi " + name)

UserInput("Jacob")

#function for adding two integers
def Add(num1, num2):
    return(num1+num2)

sum = Add(2,5)
print(sum)

#below is a example of a class

class Parent:
    def __init__(self):
        #the pass line is a filler that does nothing
        pass
    def parentFunc(self):
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        pass
    def childFunc(self):
        print("This is the child class")

c = Child()
c.parentFunc()
c.childFunc()