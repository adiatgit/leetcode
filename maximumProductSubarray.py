def prodSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    mp = nums[0] if nums[0] >0 else 1
    mn = nums[0] if nums[0] != 0 else 1
    for i in range(1, len(nums)):
        if nums[i] > 0:
            mp *= nums[i]
            mn *= nums[i]
            dp[i] = max(mn, mp, dp[i - 1])
        elif nums[i] == 0:
            dp[i] = max(dp[i - 1], 0)
            mn = mp = 1
        else:
            mn *= nums[i]
            dp[i] = max(mn, dp[i - 1])
            mp = 1
    return dp[-1]
# prodSubArray([2,-5,-2,-4,3])

def prodSubArray2(nums):
    dp = [0] * len(nums)
    for i in range(1, len(nums)):
        temp = []
        for j in range(i, 0, -1):
            temp1 = 1
            for k in nums[j-1:i]:
                temp1 *= k
            temp.append(temp1)
        dp[i] = max(max(temp), dp[i-1])
    return dp[-1]
# prodSubArray2([2,-5,-2,-4,3])


def prodSubArray3(nums):
    mp, mn, om = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x1 = mp* nums[i]
        x2 = mn* nums[i]
        mp = max(nums[i], max(x1, x2))
        mn = min(nums[i], min(x1, x2))
        om = max(mp, om)
    return om
print(prodSubArray3([2,-5,-2,-4,3]))

def prodSubArray4(nums):
    dp_pos = [0]*len(nums)
    dp_neg = [0] * len(nums)
    overall_max = nums[0]
    if nums[0]> 0:
        dp_pos[0] = nums[0]
    else:
        dp_neg[0] = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > 0:
            dp_pos[i] = max(nums[i], nums[i]* dp_pos[i-1])
            dp_neg[i] = dp_neg[i-1]*nums[i]
        else:
            dp_pos[i] = dp_neg[i-1]*nums[i]
            dp_neg[i] = min(nums[i], dp_pos[i-1]*nums[i])
        overall_max = max(overall_max, dp_pos[i])
    return overall_max