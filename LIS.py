def lengthOfLIS(nums):
    dp = [None for _ in range(len(nums))]
    dp[0] = 1
    globalMax = 0
    for i in range(1, len(nums)):
        localMax = 0
        for j in range(0, i):
            if nums[j] < nums[i]:
                localMax = max(localMax, dp[j])
        dp[i] = localMax +1
        globalMax = max(globalMax, dp[i])
    return globalMax
lengthOfLIS([1,3,5,4,7])