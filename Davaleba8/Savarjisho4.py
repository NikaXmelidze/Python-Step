import functools

list1 = ['asd', 'ara', 'tenet']

def filterPalindromes(filterList):

    palindromeList = filter(lambda a : a==a[::-1], filterList)
    return list(palindromeList)

print(filterPalindromes(list1))





