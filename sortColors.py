def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for j in range(len(nums)):
        key = nums[j]
        i = j - 1
        while (i >= 0 and nums[i] > key):
            nums[i + 1] = nums[i]
            i = i - 1
        nums[i + 1] = key
    return nums
# sortColors([2,0,2,1,1,0])


'''

Using counting sort

'''
def sortColors2(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    rangeArr = [0, 1, 2]
    count = [0, 0, 0]

    for i in nums:
        if i == 0:
            count[0] += 1
        elif i == 1:
            count[1] += 1
        else:
            count[2] += 1

    for i in range(1,len(count)):
        count[i] = count[i] + count[i-1]
    output = ['None'] * (len(nums))
    for i in range(len(nums)):
        output[count[nums[i]]-1] = nums[i]
        count[nums[i]] -= 1
    return output
print(sortColors2([2,0,2,1,1,0]))