class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}

        def helper(i, remaining):
            if(i, remaining) in dp:
                return dp[(i, remaining)]

            if remaining == 0:
                return 1 
            if i == len(coins) or remaining < 0:
                return 0

            dp[(i, remaining)] = helper(i, remaining - coins[i]) + helper(i + 1, remaining)
            return dp[(i, remaining)]

        return helper(0, amount)
            

            