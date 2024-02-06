import random

list = []

for i in range(20):

    number = random.randrange(0, 1000)

    list.append(number)

print(list)

list.sort()

print(list)
print("Minimum value in list is: " + str(min(list)))
print("Maximum value in list is: " + str(max(list)))
