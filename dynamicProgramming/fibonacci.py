
def fib(n, arr):
    print(arr)
    if n<=1:
        return n
    else:
        if arr[n-1] != -1 and arr[n-2] !=-1:
            arr[n] = arr[n-1] + arr[n-2]
            return arr[n]
        else:
            arr[n] = fib(n - 2, arr) + fib(n - 1, arr)
    return arr[n]

arr = [-1]*6
arr[0], arr[1] = 0,1
print(fib(5,arr))
# print(arr)
def fibRecursive(n):
    arr = [-1]*(n+1)
    arr[0], arr[1] = 0,1
    for i in range(2, n+1):
        arr[i] = arr[i-2]+ arr[i-1]
    print(arr)
    return arr[n]
print(fibRecursive(5))


def fibG4G(n, arr):
    print(arr)
    if n<=1:
        return n
    else:
        if arr[n-1] == 0:
            arr[n-1] = fib(n-1, arr)

        if arr[n-2] ==0:
            arr[n-2] = fib(n-2,arr)

    arr[n] = fib(n-2, arr) + fib(n-1, arr)
    return arr[n]