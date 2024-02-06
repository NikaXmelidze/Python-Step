

list1 = [1, 5, 6, -2, 65, -123, 550, 100, -20]

def filterPositives(filterList):

    positiveList = filter(lambda a : a >= 0, filterList)
    return list(positiveList)

print(filterPositives(list1))