

matrix1 = [[1,2,3], [4,5,6]]

matrix2 = [[7,8,9], [10,11,12]]


for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        sum = matrix1[i][j] + matrix2[i][j]
        print(f"Sum of row {i}, collumn {j} is: {sum}")