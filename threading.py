# imports
import threading
import time

# hello function
def hello():
    time.sleep(5)
    print('Hello World')


# single thread example
print('this is the beginning of the single thread')
hello()
print("this is the end of the single thread")

# pause between examples
time.sleep(3)
# multi thread example
print('this is the beginning of the multi thread')

#thread object
threadObj = threading.Thread(target = hello)
# actual threading
threadObj.start()

print('this is the end of the multi thread')