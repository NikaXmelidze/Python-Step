
def decorator(func):
    def wrapper(number):
        if number < 0:
            error = ValueError("Only positive numbers are allowed")
            raise error
        else:
            func(number)
    return wrapper


@decorator
def print_number(number):
    print(number)

print_number(5)
print_number(-5)