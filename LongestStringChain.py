def check(word1, word2):
    for i in range(len(word1)):
        if word2 == word1[:i] + word1[i + 1:]:
            return 1
    return 0


def longestStrChain(words):
    dp = [0] * len(words)
    for i in range(len(words)):
        for j in range(i-1, -1, -1):
            if len(words[j]) + 1 == len(words[i]):
                itr =check(words[i], words[j])
                if itr:
                    dp[i] = max(dp[i], dp[j] + itr)
                else:
                    dp[i] = 0
                break
    return max(dp) + 1

longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])