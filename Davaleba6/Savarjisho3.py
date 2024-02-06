

fibonacciN = int(input("Enter number: "))



def printFibonacci(n):
    number1 = 0
    number2 = 1 
    print(number1, end= " ")
    print(number2, end=" ")
    newNumber = number1+number2

    for i in range(n-3):
        print(newNumber, end=" ")
        number1 = number2
        number2 = newNumber
        newNumber = number1 + number2
    
    return newNumber
        



print(printFibonacci(fibonacciN))