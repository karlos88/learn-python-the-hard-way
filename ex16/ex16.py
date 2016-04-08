from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

# Open file with 'w' flag - WRITE mode
print("Opening the file...")
target = open(filename, 'w')

# Truncate - not really needed, because 'w' flag causes script to overwrite the file
print("Truncating the file, goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to file")
# Basic form from book:
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# shorten 6 lines into 1 and use other string formatting - because why not?
target.write("{0}\n{1}\n{2}\n".format(line1, line2, line3))

print("And finally we close it.")
target.close()
