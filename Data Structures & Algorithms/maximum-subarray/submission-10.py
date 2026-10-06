class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        result = nums[0]

        for num in nums:
            if temp<0:
                temp = 0
            temp += num
            result = max(result, temp)

        return result
        
