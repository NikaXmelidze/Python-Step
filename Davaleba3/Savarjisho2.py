

total_sum = 0


while True:
    numberAsString =  input("Enter number: ")
    if numberAsString == "Sum":
        print(total_sum)
        break
    else:
        number = int(numberAsString)
        total_sum += number
        print(f"The current number is {str(total_sum)}")