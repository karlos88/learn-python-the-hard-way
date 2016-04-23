i = 0
numbers = []

def loop_to_given_arg(loop_stop, increment = 1):
    j = 0
    numbers = []
    while j < loop_stop:
        numbers.append(j)
        j += increment

    print("The numbers from function: ")
    for num in numbers:
        print(num)



while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)


print("The numbers: ")

for num in numbers:
    print(num)

loop_to_given_arg(20, 3)