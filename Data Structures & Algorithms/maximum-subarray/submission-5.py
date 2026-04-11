class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        result = 0
        for i in range(0, len(nums)):
            
            if(nums[i]<0):
                result = max(result, curSum)
            
            curSum += nums[i]
            if(curSum<0):
                curSum = 0
            
        result = max(curSum, result)
        if result == 0:
            return max(nums)
        return result