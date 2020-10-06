def dailyTemperatures( T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    number_of_days = []
    for i in range(0, len(T)):
        count =0
        flag = 0
        for j in range(i+1, len(T)):
            count = count +1
            if(T[i] < T[j]):
                number_of_days.append(count)
                flag = 1
                break
        if(flag == 0):
            number_of_days.append(0)

    return number_of_days

print dailyTemperatures([73,74,75,71,69,72,76,73])

def anotherdailyTemperatures( T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    number_of_days = []
    temp = T[0]
    count = 0
    for i in range(1, len(T)):
        count = count +1
        if(temp < T[i]):
            number_of_days.append(count)
            temp = i
            
    return number_of_days
