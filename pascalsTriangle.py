def fact(n):
    ans= 1
    for i in range(2,n+1):
        ans = ans * i
    return ans
def pascals(n):
    pt =[[1]]
    for i in range(1, n):
        t = []
        for j in range(i+1):
            if j == 0 or j == i:
                t.append(1)
            else:
                a = pt[i-1][j-1]
                b = pt[i-1][j]
                t.append(a+b)
        pt.append(t)
    return pt
print(pascals(1))