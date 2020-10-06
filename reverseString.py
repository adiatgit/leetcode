def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    l = len(s)
    x = 0
    if l %2 == 0:
        rangel = l/2
    else:
        rangel = int(l/2)
    for i in range(rangel):
        temp = s[l - i - 1]
        # print(temp)
        s[l - i - 1] = s[i]
        s[i] = temp
        # print(s[i])
    return s
print(reverseString(["h","e", "l","l", "o"]))