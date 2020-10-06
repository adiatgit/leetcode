import math
n=12
dp = ['None'] * (n+1)
dp[0]= 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n + 1):
    temp = []
    for j in range(1, int(math.sqrt(i))+1):
        if (i - j * j >= 0):
            temp.append(dp[i - j * j]+1)
        else:
            break
    dp[i] = min(temp)
print(dp[n])