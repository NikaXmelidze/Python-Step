

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
operator = input("Enter operator: ")


def calculator(x, y, op):

    dict = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y,
        '//': lambda x, y: x//y,
        '**': lambda x, y: x**y,
        '%': lambda x, y: x%y,
    }

    result = dict.get(op)(x,y)
    return result



print(calculator(a,b,operator))