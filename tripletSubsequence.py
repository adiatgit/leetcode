def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    count = 0
    for i in range(1, len(nums)):
        if nums[i - 1] <= nums[i]:
            count += 1
        else:
            count = 0
        if count >= 2:
            return True
    return False
increasingTriplet([1,2,3,4,5])