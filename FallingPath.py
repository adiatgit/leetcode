def minFallingPath(A):
    dp = [[0] * len(A) for i in range(len(A))]
    dp[0] = A[0]
    for i in range(1, len(A)):
        for j in range(len(A)):
            if j == 0:
                dp[i][j] = A[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
            elif j == len(A) - 1:
                dp[i][j] = A[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = A[i][j] + min(dp[i - 1][j], dp[i - 1][j-1], dp[i - 1][j + 1])
    return min(dp[-1])
minFallingPath([[1,2,3],[4,5,6],[9,8,9]])