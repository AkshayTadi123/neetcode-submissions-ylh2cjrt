class Solution:
    dp = {}
    def numDecodings(self, s: str) -> int:
        if(len(s) == 0 or s[0] == "0"):
            return 0
        self.dp = {}
        self.dp[len(s)] = 1
        return self.dfs(0, s)

    def dfs(self, i: int, s: str) -> int:
        if(i in self.dp):
            return self.dp[i]
        if(i == len(s)):
            return 1
        if(s[i] == '0'):
            return 0
        
        res = self.dfs(i+1, s)
        if(i < len(s)-1):
            if ("10" <= s[i:i+2] <= "26"):
                res += self.dfs(i+2, s)
        self.dp[i] = res
        return res
            
