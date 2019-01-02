#! usr/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of lines

import sys, pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
print(lines)
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
print(lines)

text = '\n'.join(lines)
pyperclip.copy(text)

# problem with the book: he writes the example as 'Lists of stuff\nLists of dogs\nLists of stuff" etc but you have to actually copy 3 separate lines of text