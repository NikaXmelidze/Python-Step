


with open("test.txt", "w") as test_file:
    for i in range(1000):
        test_file.write("Text" + str(i) + "\n")

with open("test.txt", "r") as read_file:
    lineCount = len(read_file.readlines())
    print("There are " + str(lineCount) + " lines in the file" )