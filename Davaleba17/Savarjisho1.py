


class Person:

    def __init__(self, name):

        self.name = name
        self.deposit = 1000
        self.loan = 0

    def __str__(self):

        return f"Name: {self.name}, deposit: {self.deposit}, loan: {self.loan}"
        

class House:
    
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "Can be sold"

    def sell_house(self, buyer, loan_amount):
        if loan_amount is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Sold"
            print(f"House has been sold. New owner: {self.owner.name}, new status: {self.status}")
        elif isinstance(loan_amount, (int, float)):
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Sold with loan"
            buyer.loan += loan_amount
            print(f"House has been sold. New owner: {self.owner.name}, new status: {self.status}")

    
    def __str__(self):
        return f"House id: {self.ID} House owner: {self.owner.name}, house status: {self.status}"
        
        



house_owner = Person("Nika")
house_buyer = Person("Luka")
home = House(1, 50000, house_owner)
home2 = House(2, 30000, house_buyer)
print(home)
home.sell_house(house_buyer, 50000)
print(home)

print(house_owner)
print(house_buyer)

print(home2)
home2.sell_house(house_owner)
print(home2)

print(house_buyer)
print(house_owner)

        