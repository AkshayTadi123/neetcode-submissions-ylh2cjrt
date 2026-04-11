class Solution:
    dict1 = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount == 0):
            return 0
        self.dict1 = {}
        return self.helper(coins, amount)
        
    def helper(self, coins: List[int], amount: int):
        if amount in self.dict1:
            return self.dict1[amount]
        
        if(amount<0):
            return -1
        elif amount == 0:
            return 0
        else:
            minCost = float('inf')
            for coin in coins:
                res = self.helper(coins, amount - coin)
                if res >= 0: 
                    minCost = min(minCost, 1 + res)

        if minCost == float('inf'):
            self.dict1[amount] = -1
            return -1 
        else:
            self.dict1[amount] = minCost
            return minCost
                


        
        