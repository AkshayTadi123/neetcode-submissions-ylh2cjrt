class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n)
        if n<2:
            return n
        dp[-1] = 1
        dp[-2] = 2
        
        for i in range(n-3, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        return dp[0]
        