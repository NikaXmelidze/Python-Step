

class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print(f"Balance on account number {self.account_number} is {self.balance}")

    def take_out(self, amount):
        if self.balance < amount:
            print(f"{self.account_holder}s account does not have enough funds for this operation")
        else:
            new_balance = self.balance - amount
            print(f"{amount} was taken out of the account, new balance is {new_balance}")
            self.balance -= amount

    def deposit(self, amount):
        new_balance = self.balance + amount
        print(f"{amount} was deposited into the account, new balance is {new_balance}")
        self.balance += amount



account1 = BankAccount(1, "Nika", 10000)
account2 = BankAccount(2, "Mariami", 2000)

account1.take_out(8000)

account1.check_balance()

account2.deposit(5000)

account2.take_out(8000)

account2.check_balance()