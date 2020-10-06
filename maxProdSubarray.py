def maxProdSub(nums):
    meh = 1
    mpf = 0
    for i in nums:
        meh = meh * i
        if(meh == 0):
            meh =1
        if(mpf < meh and meh !=1):
            mpf = meh
    return mpf
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_dp = [0]*len(nums)
    min_dp = [0]*len(nums)
    max_dp[0], min_dp[0] = nums[0], nums[0]
    for i in range(1, len(nums)):
        max_dp[i] = max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
        min_dp[i] = min(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
    return max(max_dp)

print(maxProduct([2,3,-2,4]))