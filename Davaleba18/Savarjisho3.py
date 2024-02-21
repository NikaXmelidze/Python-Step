
def decorator(func):
    def wrapper(*args):
        balance = args[0]
        amount = args[1] 
        commision = 1
        if balance - amount - commision< 0:
            print("The funds on your account are not enough to complete this transaction")
        else:
            func(balance, amount)
    return wrapper


@decorator
def transaction(balance, amount):

    print(f"Current balance: {balance}")
    balance -= amount
    print(f"{amount} has been transferred. New balance after commision {balance-1}")



transaction(5000, 4999)
transaction(5000, 5000)