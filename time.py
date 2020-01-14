# imports
import time

# calculation function
def calculate():
    for i in range(0,10000):
        pass

# function that calculates how long the calculation function takes
def timeFunc():
    startTime = time.time()
    calculate()
    endTime = time.time()
    print(endTime-startTime)

timeFunc()