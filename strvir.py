def findpos(x, num):
    if len(num) == 0:
        return 0
    for i in range(len(num)):
        if num[i] >= x:
            return i
    return i+1
def minimumOperations(numbers):
    # Write your code here
    op_no = 0
    temp_list = []
    for i in numbers:
        pos = findpos(i,temp_list)
        if (pos <= len(temp_list) - pos):
            op_no += pos * 2 + 1
        else:
            op_no += (len(temp_list) - pos) * 2 + 1
        temp_list.insert(pos, i)
    return op_no
print(minimumOperations([10,2,19,10,1,6,13,6,6,15,12]))