"""This script runs to go to facebook in a Safari browser.
Then it enters a fake email and password and clicks enter
"""
# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# initial setup of browser
browser = webdriver.Safari()

# go to facebook
browser.get("https://facebook.com")

# setup of variables
email = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")

# input text
email.send_keys("joe@email.com")
password.send_keys("password")

# pause for 3 seconds
time.sleep(3)

# hit enter key
password.send_keys(Keys.ENTER)

