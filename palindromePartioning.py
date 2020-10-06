output = []
def isPalindrome(string):
    return string == string[::-1]

def findPartition(s, temp):
    if not s:
        output.append(temp[:])
        return
    for i in range(1, len(s) + 1):
        if isPalindrome(s[:i]):
            temp.append(s[:i])
            findPartition(s[i:], temp)
            temp.pop()



findPartition("aab", [])
print(output)
