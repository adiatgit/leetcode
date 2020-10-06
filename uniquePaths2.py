def uniquePaths(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [['None'] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i][j] == 0 and dp[i][j - 1] != 0:
                    dp[i][j] = 1
                elif dp[i][j - 1] == 0:
                    dp[i][j] = 0
            elif j == 0:
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i][j] == 0 and dp[i - 1][j] != 0:
                    dp[i][j] = 1
                elif dp[i - 1][j] == 0:
                    dp[i][j] = 0
            elif obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
print(uniquePaths([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))