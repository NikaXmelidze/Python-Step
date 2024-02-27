

import json


class Product():
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

def custom_encoder(obj):
    if isinstance(obj, Product):
        return {
            "Name": obj.name,
            "Price": obj.price,
            "Quantity": obj.quantity
        }
    return obj

def custom_deserialization(json_data):
    return Product(json_data['Name'], json_data['Price'], json_data['Quantity'])
    

lst = []

product1 = Product("Iphone 15 Pro Max", "4500", "400")
product2 = Product("Samsung Galaxy s24 Ultra", "3900",  "600")
product3 = Product("Playstation 5", "1400", "800")

lst.append(product1)
lst.append(product2)
lst.append(product3)

with open("Products_Data.json", "w") as json_file:
    json.dump(lst, json_file, default=custom_encoder, indent= 4)

with open("Products_Data.json", "r") as read_json:
    data = json.load(read_json, object_hook=custom_deserialization)

for product in data:
    print(product) 



