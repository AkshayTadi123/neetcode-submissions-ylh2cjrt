class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}

        def helper(remaining, index):
            if (remaining, index) in memo:
                return memo[(remaining, index)]
            if remaining == 0:
                return 1
            if index == len(coins) or remaining<0:
                return 0

            skip = helper(remaining, index+1)
            use = helper(remaining-coins[index], index)
            
            memo[(remaining, index)] = skip+use
            return memo[(remaining, index)]
        
        return helper(amount, 0)
        


            