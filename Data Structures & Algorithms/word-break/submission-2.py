class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        n = len(s)
        def helper(index):
            if index == n:
                return True

            if index in dp:
                return dp[index]
            
            x = False
            for word in wordDict:
                k = len(word)
                if index+k <= n and s[index:index+k] == word:
                    x = x or helper(index+k)
                    if x:
                        dp[index] = True
                        return True
            
            dp[index] = False
            return False
        return helper(0)
                        

        
       
            
        
