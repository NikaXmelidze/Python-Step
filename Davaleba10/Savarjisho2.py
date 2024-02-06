
import random

def createRandomList():

    random_list = []

    for i in range(30):
        number = random.randrange(0,1000)

        random_list.append(number)

    return random_list  

lst = createRandomList()
print(lst)


lambda_for_filter = lambda a : a%3 == 0

def linear_search(list_for_search, value):

    for i in list_for_search:
        if i == value:
            return list_for_search.index(i)
        
    return -1


def filter_list_for_threes(list_for_filter, lambda_function):

    index_list = []
    filtered_list = list(filter(lambda_function, list_for_filter))
    number_index = 0
    for i in range(len(filtered_list)):
        for j in range(len(list_for_filter)):
            if filtered_list[i] == list_for_filter[j]:
                number_index = linear_search(list_for_filter, filtered_list[i])
                index_list.append(number_index)

    return index_list


print(list(filter_list_for_threes(lst, lambda_for_filter)))


