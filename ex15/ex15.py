# import sys module
from sys import argv

# assign values from CLI script execution arguments to variables 'script' and 'filename'
script, filename = argv

# open the file with name given in script arguments
txt = open(filename)

# print out message and file contents
# contents are retrieved using file.read() method, which takes a part of file (or all file contents as in here,
# because we don't have "size" argument for this function, and returns it as a string
print("Here's your file: %r" % filename)
print(txt.read())

# Get the file name again, this time using user to type in the file name and store it in different variable
print("Type the filename again:")
file_again = input("> ")

# similar as previous open
txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()