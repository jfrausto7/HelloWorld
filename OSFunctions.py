"""This is a header block comment
This script has a bunch of OS functions and stuff i wanted to try out
Lol
"""

"""Below is an example of document manipulation.
It uses the docx module
Remember to install the 'python-docx' one, not the other one.
This was a pain to get to work.
"""

# import the docx module first
import docx

# now assign a variable for it
doc = docx.Document("./testdoc.docx")

for para in doc.paragraphs:
    print(para.text)
