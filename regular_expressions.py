# imports
import re

# sentence to search
sentence = "Mike's number is 801-242-5334"
# create regex variable
phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# create regex mathcing object to search using regex variable
mo = phoneRegex.search(sentence)

# use group function to print it out
stuff = mo.group()

# print it out
print(stuff)

