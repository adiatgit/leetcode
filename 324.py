def wiggleSort(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    lenOfList = int(len(nums) / 2)
    for i in range(lenOfList):
        temp = nums.pop(lenOfList + i)
        nums.insert(2 * i + 1, temp)
    return nums
wiggleSort([1, 3, 2, 2, 3, 1])