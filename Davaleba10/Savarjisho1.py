
import random


searched_number = 20

def createRandomList():

    random_list = []

    for i in range(100):
        number = random.randrange(0,1000)

        random_list.append(number)

    return random_list  


#linear
def linear_search(list_for_search, value):

    for i in list_for_search:
        if i == value:
            return list_for_search.index(i)
        
    return -1

random_list = list(createRandomList())

print(random_list)
result = linear_search(random_list, searched_number)
print(f"Index of {searched_number} is {result}")


#binary

def binary_search(list_for_search, value):

    low = 0
    high = len(list_for_search) - 1

    while low <= high:

        mid = (low + high) // 2

        if list_for_search[mid] < value:
            low = mid + 1
        elif list_for_search[mid] > value:
            high = mid - 1
        else:
            return mid 
    return -1


def quickSort(givenList):
    lenght = len(givenList)

    if lenght <= 1:
        return  givenList
    else:
        pivot = givenList.pop()

    greater_numbers = []
    lower_numbers = []

    for i in givenList:
        if i > pivot:
            greater_numbers.append(i)
        else:
            lower_numbers.append(i)

    return quickSort(lower_numbers) + [pivot] + quickSort(greater_numbers)

sorted_list = quickSort(random_list)
print(sorted_list)
result = binary_search(sorted_list, searched_number)
print(f"Index of {searched_number} is {result}")