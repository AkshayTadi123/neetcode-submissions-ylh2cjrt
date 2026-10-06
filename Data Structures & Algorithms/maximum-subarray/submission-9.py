class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(max(nums)<0):
            return max(nums)
        if len(nums)==1:
            return nums[0]

        result = float('-inf')
        temp = 0
        for i in range(len(nums)):
            if (temp + nums[i])<0:
                temp = 0
            else:
                temp += nums[i]
                result = max(result, temp)

        return result

        
