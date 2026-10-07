class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(index):
            if index >= len(nums):
                return 0
        
            if index in memo:
                return memo[index]
            
            memo[index] = max(helper(index+1), nums[index]+helper(index+2))
            return memo[index]

        return helper(0)

        

        

