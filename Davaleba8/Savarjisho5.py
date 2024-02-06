import functools

list1 = [1,2,3,4,5]

def multiplyList(list):
    try:
        multipliedList = functools.reduce(lambda a, b : a*b, list)
        return multipliedList
    except TypeError:
        print("Only a list is permited")



print(multiplyList(list1))