from sys import argv

# original script from book
# script, first, second, third = argv
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# Script with less args
# script, arg_1, arg_2 = argv
# print("Arguments used when running %s script: argument 1 - %r, argument 2 - %r" % (script, arg_1, arg_2))

# Script with more args
script, arg_1, arg_2, arg_3, arg_4 = argv
print("All of args: %r" % (" ".join([script, arg_1, arg_2, arg_3, arg_4])))

# and use of raw_input()/input()
print("Type your name:")
name = input()
print("All of args: %r plus your name: %r" % (" ".join([script, arg_1, arg_2, arg_3, arg_4]), name))
