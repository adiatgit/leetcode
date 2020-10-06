def minCostClimbingStairs(cost):
    total_cost = 0
    # for i in range(1, len(cost)):
    costLen = len(cost)-1
    i =1
    while (i < costLen):
        if cost[i - 1] < cost[i]:
            print(i)
            total_cost += cost[i - 1]
            i = i+2
        else:
            print("-", i)
            total_cost += cost[i]
            i = i + 1
        k = cost[i]
    return total_cost
# minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])

#finding minimum cost climinbing stairs by  recursion without dp

def findMin(cost, i):
    if i < len(cost):
        return min((cost[i]+ findMin(cost, i+1), cost[i]+ findMin(cost, i+2)), (cost[i+1] + findMin(cost, i+2), cost[i+1]+ findMin(cost, i+2)))
    return 0
print(findMin([5, 15, 20, 22], 0))
