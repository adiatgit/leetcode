def getDiscount(arr):
    discount_amount = 0
    undiscount_item = []
    for i in range(0, len(arr)):
        flag = 0
        for j in arr[i+1:]:
            if(arr[i]>j):
                discount_amount = discount_amount + arr[i]-j
                flag =1
                break
        if(flag != 1):
            undiscount_item.append(i)
    return

getDiscount([5, 4, 5, 1, 3, 3, 8, 2])
