def divisible(s, t):
    if len(s) == 0:
        return True
    if t in s:
        x = s.replace(t, "")
        divisible(x, t)
    return False


def findSmallestDivisor(s, t):
    # Write your code here
    if (divisible(s, t)):
        smallstr = ""
        for i in s:
            smallstr += i
            if (divisible(s, smallstr)):
                return len(smallstr)

    return -1
findSmallestDivisor("lrbb","lrbb")
