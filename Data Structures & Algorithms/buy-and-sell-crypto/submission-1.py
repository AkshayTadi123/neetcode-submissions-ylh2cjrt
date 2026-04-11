class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minIndex = 0
        maxDiff = 0

        for i in range(len(prices)):
            if prices[i] < prices[minIndex]:
                minIndex = i
            if(prices[i] - prices[minIndex]>maxDiff):
                maxDiff = prices[i] - prices[minIndex]
        
        return maxDiff