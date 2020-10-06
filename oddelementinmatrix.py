n=2
m=3
indices = [[1,1], [0, 1]]
matrix = [[0 for x in range(m)] for x in range(n)]

for k in indices:
    for i in range(0, m):
        matrix[k[0]][i] = matrix[k[0]][i] +1
    for j in range(0, n):
        matrix[j][k[1]] = matrix[j][k[1]] +1
count = 0

for i in range(0, n):
    for j in range(0, m):
        if(matrix[i][j] %2 ==1):
            count = count +1
