def targetSum(alist1, target_sum):
    def anotherFun(alist, target_sum1, t, index, dp):
        index -=1
        if sum(alist) < target_sum1:
            return 0
        if len(alist) == 0 and target_sum1 == 0:
            return 1
        if [index, target_sum1] in dp:
            return dp[alist1+[index]]
        if alist:
            x = alist[index]
            return anotherFun(alist[:index], target_sum1 -x, 0, index, dp) + anotherFun(alist[:index], target_sum1 +x, 1, index)
        dp.update({(index, target_sum1):})
        return 0
    count = anotherFun(alist1, target_sum,2, len(alist1))
    return count

print(targetSum([1,1,1,1,1], 3))