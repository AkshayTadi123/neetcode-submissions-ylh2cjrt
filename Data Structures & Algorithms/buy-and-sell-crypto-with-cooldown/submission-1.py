class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def helper(index, hold):
            if index >= len(prices):
                return 0
            if(index, hold) in dp:
                return dp[(index,hold)]
            if(hold):
                profit = max(helper(index+1, True), prices[index] + helper(index+2, False))
            else:
                profit = max(helper(index+1, False), helper(index+1, True)-prices[index])
                
            dp[(index,hold)] = profit
            return profit
        
        return helper(0, False)

