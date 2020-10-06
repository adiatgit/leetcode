def isLongPressedName(name: str, typed: str):
    j = 0
    for i in range(len(name)):
        while (True):
            if (typed[j] == name[i]):
                j += 1
                break
            elif(i > 0 and  typed[j] == name[i - 1]):
                j+=1
            else:
                return False
    return True
isLongPressedName("zlexya", "aazlllllllllllllleexxxxxxxxxxxxxxxya")