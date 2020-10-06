m=2
n=2
dp = [['None'] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[m - 1][n - 1])