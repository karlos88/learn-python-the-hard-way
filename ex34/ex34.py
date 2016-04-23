animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
numbers = [3, 1, 3, 5, 2, 6, 4]

for i in numbers:
    print("The %d animal is at %d and is a %s." % (i, i - 1, animals[i - i]))
    print("The animal at %d is the %d animal and is a %s." % (i - 1, i, animals[i - 1]))