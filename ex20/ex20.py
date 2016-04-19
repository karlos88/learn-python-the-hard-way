from sys import argv

# Get the arguments passed in the CLI into variables
script, input_file = argv


# Function which reads contents of file and prints it
def print_all(f):
    print(f.read())


# Function which goes to byte 0 (or rather goes to offset 0)
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file
current_file = open(input_file)

# Call function "print_all"
print("First let's print the whole file:\n")
print_all(current_file)

# Call function "rewind" to go back to beginning of file
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

# Call "print_a_line" to print 3 different lines from file, separately
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
