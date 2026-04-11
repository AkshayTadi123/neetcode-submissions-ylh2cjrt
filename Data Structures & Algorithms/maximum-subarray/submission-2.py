class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            if curSum>=0:
                if(nums[i] + curSum < curSum):
                    # curSum += num
                    result = max(result, curSum)
                    # curSum += num
            else:
                curSum = 0
            curSum+=nums[i]
        return max(result, curSum)


        