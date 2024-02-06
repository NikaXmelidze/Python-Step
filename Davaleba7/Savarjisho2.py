



def sumDigits(number):
    if number == 0:
        return number
    else:
        return(number % 10) + sumDigits(number//10)

print(sumDigits(12345))
