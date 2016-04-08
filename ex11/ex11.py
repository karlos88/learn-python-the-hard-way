print("How old are you?",)
age = input()
print("How tall are you?",)
height = input()
print("How much do you weigh?",)
weight = input()

print("So, you're %r old, %s tall and %r heavy." % (
    age, height, weight))

# Go online and find out what Python's raw_input does.
# raw_input() in Python2 prints out a prompt to stdout, and then waits for user input - reads a line from stdin,
# removes trailing character and converts it to a string.
# Python3 input() does the same.

# Can you find other ways to use it? Try some of the samples you find.
# Write another "form" like this to ask some other questions.
print("Whats your height in inches?")
in_height = int(input())
print(in_height*2.54)

# Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence.
# See how the single-quote needs to be escaped because otherwise it would end the string?
