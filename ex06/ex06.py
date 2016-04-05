# Assigning a string to variable x with formatting characters
x = "There are %d types of people." % 10

# Assigning strings to variables binary & do_not
binary = "binary"
do_not = "don't"

# Assigning a string to variable y with use of formatting chars to replace variables binary & do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints out strings assigned to variables x & y
print(x)
print(y)

# Prints out a string and uses formatting char to replace variables with strings
print("I said: %r." % x)
print("I also said: '%s'." % y)

# Assigning boolean False to variable
hilarious = False

# Assigning a string to variable with use of formatting chars. There is no variable to be replaced
# by formatting so it's not a good idea to print that string now. It would be printed as is - with %r.
joke_evaluation = "Isn't that joke so funny?! %r"

# More printing. Substitutes %r from joke_evaluation variable to string from hilarious variable
print(joke_evaluation % hilarious)


# Assign strings to variables and print out text using string concatenation
# (attach one string to another)
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)