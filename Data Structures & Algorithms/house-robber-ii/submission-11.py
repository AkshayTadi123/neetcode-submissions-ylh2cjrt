class Solution:

    def rob(self, nums: List[int]) -> int:
        result = {}

        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        result = {}
        result[1] = nums[0]
        result[2] = max(nums[0], nums[1])

        for i in range(3, len(nums)+1):
            result[i] = max(result[i-1], result[i-2] + nums[i-1])

        return result[len(nums)]
        




        

