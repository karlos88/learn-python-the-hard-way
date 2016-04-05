name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 180 # lbs
weight_kg = weight * 0.454
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight))


print("Printing a string - %s" % "test")
print("Printing an int - %d" % 10)
print("Printing a float with 3 points decimal precision- %.3f" % 10)
print("Printing a HEX 10 - %X" % 10)

# python format characters
# d 	Signed integer decimal
# i 	Signed integer decimal
# o 	Unsigned octal
# u 	Unsigned decimal
# x 	Unsigned hexadecimal (lowercase)
# X 	Unsigned hexadecimal (uppercase)
# e 	Floating point exponential format (lowercase)
# E 	Floating point exponential format (uppercase)
# f 	Floating point decimal format
# F 	Floating point decimal format
# g 	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise
# G 	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise
# c 	Single character (accepts integer or single character string)
# r 	String (converts any python object using repr())
# s 	String (converts any python object using str())
# % 	No argument is converted, results in a "%" character in the result