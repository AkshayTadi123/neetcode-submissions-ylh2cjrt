class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxVal = max(prices)
        # index = prices.index(maxVal)
        # if(index == 0):
        #     return 0
        minIndex = 0
        maxIndex = 0
        maxDiff = 0

        for i in range(len(prices)):
            if(prices[i]<prices[minIndex]):
                minIndex = i
            if(prices[i]-prices[minIndex]>maxDiff):
                maxDiff = prices[i]-prices[minIndex]


        return maxDiff