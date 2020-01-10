# the imports first of course
import requests
from bs4 import BeautifulSoup

# get the data html
data = requests.get("https://google.com")
# now make the soup
soup = BeautifulSoup(data.text, "html.parser")

# find div with image in it
soup.find_all("div", {"id":"lga"})
