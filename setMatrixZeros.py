def setZeros(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print(matrix[i][j])
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            for j in range(len(matrix)):
                matrix[j][i] = 0
    return matrix
# print(setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))