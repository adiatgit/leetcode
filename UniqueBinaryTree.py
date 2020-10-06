class Solution:
    def numTrees(self, n: int) -> int:
        self.dp = [-1 for _ in range(2*n+1)]
        self.dp[0], self.dp[1] =1,1
        def fact(x):
            if self.dp[x]!=-1:
                return self.dp[x]
            for i in range(1, x+1):
                self.dp[x] = self.dp[x-1]*i 
            return self.dp[x]
        return (fact(2*n)/(fact(n+1)*fact(n)))-1

Sn = Solution()
Sn.numTrees(4)