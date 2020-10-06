def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    setarr = set(arr)
    # temp = list(setarr)[0]
    countDict ={}
    for i in list(setarr):
        countDict[i] =  arr.count(i)
    if(len(countDict.values()) == len(set(countDict.values()))):
        return True
    return False    
arr =[26,2,16,16,5,5,26,2,5,20,20,5,2,20,2,2,20,2,16,20,16,17,16,2,16,20,26,16]

print uniqueOccurrences(arr)
