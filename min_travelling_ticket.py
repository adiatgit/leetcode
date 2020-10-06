import sys
def minTravel(tickets,days):
    dp = [sys.maxsize]*(max(days)+1)
    dp[0] =0
    x = [1,7,30]
    for i in range(1,len(dp)):
        for j in range(1,len(tickets)+1):
            if i <=7:
                dp[i] = min(dp[i], dp[i-tickets[j-1]]+tickets[j-1],tickets[1])gm
            if i <= 30:
                dp[i] = min(dp[i], dp[i-tickets[j-1]]+tickets[j-1],tickets[2])
    return dp
minTravel([2,7,15], [1,2,3,4,5,6,7,8,9,10,30,31])