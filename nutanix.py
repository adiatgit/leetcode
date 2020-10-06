def checkIfReversePossible(n, x):
    y = str(x)[::-1]
    y = int(y.rstrip('0'))
    if y <= n and y > x:
        return y
    else:
        return x+1
def minSteps(n, x):
    no_of_steps = 0
    x=1
    if(n == x):
        return 0
    if(n > x):
        return 100000
    if(int(str(x)[::-1]) <= n):
        return 1 + min(minSteps(n+1, x), minSteps(int(str(x)[::-1]), x))
        x = checkIfReversePossible(n, x)
        no_of_steps +=1
    return no_of_steps

minSteps(42)