

# gdfd = "aleluiah"

# print(gdfd[-3:])

list1 = ['hello', 'world', 'coding', 'nod']

endString = input("Enter ending string: ")

def filterEndings(filterList, ending):
    endingLength = len(ending)

    filteredList = filter(lambda a: a[-endingLength:] == ending, list1)
    return list(filteredList)



print(filterEndings(list1, endString))