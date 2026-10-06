class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        if(max(nums)<0):
            return max(nums)

        temp = 0
        if len(nums)==1:
            return nums[0]

        for i in range(len(nums)):
            if (temp + nums[i])<0:
                temp = 0
            else:
                temp += nums[i]
                result = max(result, temp)

        return result

        
