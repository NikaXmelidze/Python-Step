import random

def createRandomList():

    list_For_Sort = []

    for i in range(100):
        number = random.randrange(0,1000)

        list_For_Sort.append(number)

    return list_For_Sort   


#klebadobit
def selectionSort(givenList):
    
    for i in range(len(givenList)):
        min = i
        
        for j in range(i+1, len(givenList)):
            if givenList[j] > givenList[min]:
                min = j

        givenList[i],  givenList[min] = givenList[min], givenList[i]

list1 = createRandomList()
selectionSort(list1)
print(list1)

#zrdadobit
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

list2 = createRandomList()
sortedList2 = quickSort(list2)
print(sortedList2)



    