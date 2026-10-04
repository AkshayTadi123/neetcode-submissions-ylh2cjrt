class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def helper(count):
            if count in dp:
                return dp[count]

            if count > amount:
                return float('inf')

            if count == amount:
                return 0

            x = float('inf')

            for coin in coins:
                x = min(x, 1 + helper(count + coin))

            dp[count] = x
            return x

        result = helper(0)

        if result == float('inf'):
            return -1

        return result
            
                



        
        