# imports
import schedule
import time

# hello world func
def helloWorld():
    print("Hello World")

# every day at 7:11 sharp
schedule.every().day.at("19:11").do(helloWorld)

while True:
    schedule.run_pending()
    time.sleep(1)
