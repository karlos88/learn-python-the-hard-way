# "cheese_and_crackers" function definition with named arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Printing strings, first two using formatting and printing
    # values passed to local variables in function call
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# My own function
def push_and_pull(push_ups=0, pull_ups=0):
    print("Workout time!")
    print("You have to do %d push ups!" % push_ups)
    print("And %d pull ups!" % pull_ups)

# Print string & call the function with directly specified values for its arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Print string and assign values to variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Call function but pass values using global variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Again call function with directly specified values which are result of math operation
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Again call function with directly specified values which are result of math operation between
# value from variable and directly specified value
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Calling my own function in different ways; 6 at the moment, will add more later:)
push = 5
pull = 15
push_and_pull(10, 20)
push_and_pull(10 + 10, 20 + 20)
push_and_pull(push, pull)
push_and_pull(push * 2, pull * 10)
push_and_pull(10)
push_and_pull(int(input("Push-ups:")), int(input("Pull-ups:")))
