import math
def countBits(num):
    aList = [0, 1, 1]
    latestCount = 2
    for i in range(3, num + 1):
        print(latestCount)
        t = math.log2(i) %2
        if t == 0.0:
            latestCount = i
            aList.append(1)
        else:
            aList.append(aList[i - latestCount] + aList[latestCount])
    return aList
print(countBits(5))