import sys
def coinChange(coins, amount):
    dp = [sys.maxsize] * (amount + 1)
    dp[0] = 0
    for i in range(amount + 1):
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[-1]
coinChange([1,4,5], 14)