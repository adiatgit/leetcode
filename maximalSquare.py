from math import sqrt
def maximalSquare(matrix):
    maxVal = -1
    for i in range(1,len(matrix)):
        for j in range(1, len(matrix[0])):
            if(matrix[i-1][j] != "0" and  matrix[i-1][j-1] !="0" and matrix[i][j-1] !="0" and matrix[i][j] != "0"):
                t = sqrt(float(matrix[i-1][j-1]))
                matrix[i][j] = 1+min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1]))
                if matrix[i][j] > maxVal:
                    maxVal = matrix[i][j]
    return maxVal**2
maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])