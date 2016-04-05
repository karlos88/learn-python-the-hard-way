# Assigning cars variable
cars = 100

# Assigning space_in_car variable
space_in_car = 4.0

# Assigning drivers variable
drivers = 30

# Assigning passengers variable
passengers = 90

# Assigning cars_not_driven variable
cars_not_driven = cars - drivers

# Assigning cars_driven variable
cars_driven = drivers

# Assigning carpool_capacity variable
carpool_capacity = cars_driven * space_in_car

# Assigning average_passengers_in_car variable
average_passengers_in_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_in_car, "in each car.")

# Study drills:
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
#
# Caused by invalid variable name, should be carpool_capacity.


# I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# 4.0 is used to convert to float. Even in case of using Python2 it is not necessary.
# We use space_in_car for multipication, not for division - it would be needed then.
# (for Python3 it's not necessary for both operations)

# Write comments above each of the variable assignments.
# Done.


# Make sure you know what = is called (equals) and that it's making names for things.
# Assignment

# Remember that _ is an underscore character.
# Yup

# Try running python from the Terminal as a calculator like you did before and use variable names
# to do your calculations. Popular variable names are also i, x, and j.
# >>> x = 40
# >>> y = 2.5
# >>> z = 5
# >>> y * x / z + z
# 25.0




