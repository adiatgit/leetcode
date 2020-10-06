def checkSum(givenList,S):
    sum = 0
    for i in givenList:
        sum=sum+i
    if sum ==  S:
        return True
    return False
def getCombinations(n,k):
    for i in range(k+1):
