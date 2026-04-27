class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        result = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l = r
            result = max(result, prices[r]-prices[l])
            r += 1

        return result
            
