

my_llist = [43, '22', 12, 66, 210, ["hi"]]

#A

print("Index of 210 is: " + str(my_llist.index(210)))

#B

my_llist.append("hello")
print(my_llist)

#C

my_llist.pop(2)
print(my_llist)

#D

my_llist2 = my_llist
my_llist2.clear()

print(my_llist)
print(my_llist2)