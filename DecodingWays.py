def numDecodings(s: str) -> int:
    dp = [None] * len(s)
    if s[-1] != '0':
        dp[-1] = 1
    else:
        dp[-1] = 0
    if '00' in s:
        return 0
    for i in range(len(s) - 2, -1, -1):
        if len(str(int(s[i] + s[i + 1]))) != 2:
            dp[i] = dp[i + 1] - 1
        elif int(s[i] + s[i + 1]) <= 26 and int(s[i] + s[i + 1]) > 0:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = dp[i + 1]
    return dp[0]
# numDecodings("1010")

def numDecoding2(s):
    first =1
    second = 0 if s[0] =='0' else 1
    for i in range(2,len(s)):
        one_digit = int(s[i-1:i])
        two_digit = int(s[i-2:i])
        ans = 0
        if one_digit >=1:
            ans += second
        if two_digit >= 10 and two_digit <= 26:
            ans += first
        first = second
        second = ans
    return second

numDecoding2("1231")