infinity = 1000
def floydWarshall(A):
    n = len(A[0])
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                x, y = A[j][k], A[j][i]+ A[i][k]
                A[j][k] = min(x,y)
    return A
floydWarshall([[0,3,infinity,7], [8,0,2, infinity], [5, infinity, 0, 1], [2, infinity, infinity, 0]])
#time complexity is bigO(n3)
#space complexity is bigO(1) since no extra space is used.