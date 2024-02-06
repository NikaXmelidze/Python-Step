


with(open("test2.txt", "w")) as test_file:
    for i in range(20):
        if i == 1 or i==7 or i==9 or i ==  12 or i == 16:
            test_file.write("line " + str(i+1) + "\n")
        else:
            test_file.write("\n")


with open("test2.txt", "r") as read_file:
    print(read_file.readlines())