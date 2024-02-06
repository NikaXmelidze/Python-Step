



def add_squares():
    tuple = ()

    for i in range(1,11):
        
        square_number = (i**2,)

        tuple = tuple + square_number

       

    return tuple



squared_numbers = add_squares()
print(squared_numbers)

