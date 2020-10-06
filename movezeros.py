def movezeros(nums):
    """

    :rtype: list
    """
    for i in range(len(nums)):
        went_inside =0
        if nums[i]==0:
            for j in range(i, len(nums)-i-1):
                nums[j] = nums[j+1]
                went_inside =1
            if(went_inside !=0):
                nums[len(nums)-i -1] = 0
    return nums
def movezeros2(nums):
    count = []
    for i in range(len(nums)):
        if nums[i] == 0:
            count.append(i)

    for k in reversed(count):
        nums.pop(k)
    for j in range(len(count)):
        nums.append(0)
    return nums

print(movezeros2([0,0,1]))
# movezeros([0,1,0,3,12])
