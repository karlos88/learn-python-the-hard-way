people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

# Other boolean expressions
dogs += 5
if people != dogs:
    print("People are not dogs.")

if True:
    print("This is true")

if dogs > people and cats > people:
    print("People are less than dogs and less than cats.")

if dogs > cats or dogs > people:
    print("Dogs are greater than cats or people.")

if people < dogs < cats:
    print("Dogs are greater than people but less than cats.")

if cats != 0:
    print("There are some cats.")
