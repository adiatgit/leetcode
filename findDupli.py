def findDupli(nums):
    return (sum(nums) - sum(list(set(nums))))/(len(nums)-len(list(set(nums))))
