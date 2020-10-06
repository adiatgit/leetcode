def wordBreak(s, wordDict):
    n = len(s)
    dp = [False for i in range(n + 1)]
    dp[0] = True
    list1 = []
    for i in range(n + 1):
        if dp[i]:
            another_list = []
            for j in wordDict:
                l = len(j)
                if (j == s[i:i + l]) and l + i <= n:
                    dp[i + l] = True
                    another_list.append(j)
            list1.append(another_list)
    sentences = []
    for each_list in list1:
        for word in each_list:

    return dp[n]
wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
