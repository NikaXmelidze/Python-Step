list1 = [100,20,30,50,5323,3321,22,56,700,90,10]




def sumList(list):
    sum = 0

    for i in range(len(list)):
        number = list[i]
        sum += number
    
    return sum


print(sumList(list1))