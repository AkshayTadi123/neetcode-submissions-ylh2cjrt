class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minIndex = 0
        l = 1
        while l<len(prices):
            if(prices[l]<prices[minIndex]):
                minIndex = l

            if(prices[l]-prices[minIndex]>profit):
                profit = prices[l]-prices[minIndex]

            l += 1
        return profit
        