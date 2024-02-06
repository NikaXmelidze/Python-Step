with open("CombinedFile.txt", "w") as combined_file:
    with open("combofile1.txt", "r") as combo_file1:
        with open("combofile2.txt", "r") as combo_file2:
            combined_file.write(combo_file1.read())
            combined_file.write(combo_file2.read())


file = open("CombinedFile.txt", "r")

for i in file.readlines():
    print(i)

file.close()