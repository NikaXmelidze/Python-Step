

import functools

firstList = [1,2,3]
secondList = ['a', 'b', 'c']

def mergeLists(list1, list2):
   
    mergedList = zip(list1, list2)
    return list(mergedList)



print(mergeLists(firstList, secondList))




