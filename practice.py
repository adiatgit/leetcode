def checkActivities(a, b):
    finish_time = []
    for i in range(0, len(a)):
        finish_time.append(a[i]+b[i])
    print finish_time
    finish_time.sort(reverse=True)
    count = 0
    for i in finish_time:
        for j in a:
            if i <= j:
                count =count+1
                break
    return count
print checkActivities([1,3,3,5,7], [2,2,1,2,1])
