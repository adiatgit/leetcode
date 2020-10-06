def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    for i in range(len(gas)):
        fuel = 0
        for j in list(range(i,len(gas)))+list(range(0,i)):
            fuel += gas[j]
            if(fuel < cost[j]):
                fuel -= cost[j]
                break
            fuel -= cost[j]

        if fuel >=0:
            return i
    return -1
def anotherSolution(gas,cost):
    total = 0
    start =0
    tank = 0
    for i in range(len(gas)):
        tank = tank + gas[i] - cost[i]
        if(tank<0):
            start = i+1
            total += tank
            tank = 0
    if (total + tank < 0):
        return -1
    else:
        return start

print(anotherSolution([1,2,3,4,5],[3,4,5,1,2]))