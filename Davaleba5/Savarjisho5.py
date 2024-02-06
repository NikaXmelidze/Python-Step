
matrix = [[1,2,3], [4,5,6], [7,8,9]]

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
       result[j][i] = matrix[i][j]


for lst in range(len(matrix)):
    print(result[lst])