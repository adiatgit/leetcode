import math
matrix = [[1,2,3],[4,5,6],[7,8,9]]

#making upside down
def invertClockWise(matrix):
    for i in range(int(len(matrix[0])/2)):
        temp = matrix[len(matrix[0])-i-1]
        matrix[len(matrix[0])-i-1] = matrix[i]
        matrix[i] = temp
    for i in range(len(matrix[0])):
        for j in range(i+1,len(matrix[0])):
            temp=matrix[i][j]
            matrix[i][j] =matrix[j][i]
            matrix[j][i]= temp
    return matrix
print(invertClockWise(matrix))