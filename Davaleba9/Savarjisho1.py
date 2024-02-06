
import random

list_For_Sort = []

for i in range(100):
    number = random.randrange(0,1000)

    list_For_Sort.append(number)

#sort() zrdadobit
def sortRandomListAscending(givenList):
    givenList.sort()
    return givenList

print(sortRandomListAscending(list_For_Sort))

#sort() klebadobit
def sortRandomListDescending(givenList):
    givenList.sort(reverse=True)
    return givenList

print(sortRandomListDescending(list_For_Sort))

#sorted() zrdadobit
def printSortedListAscending(givenList):
    sortedList = sorted(givenList)
    return sortedList

print(printSortedListAscending(list_For_Sort))

#sorted() klebadobit
def printSortedListDescending(givenList):
    sortedList = sorted(givenList, reverse=True)
    return sortedList

print(printSortedListDescending(list_For_Sort))