class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total//2
        dp = {}

        def helper(index, remaining):
            if (index, remaining) in dp:
                return dp[(index, remaining)]
            if remaining == 0:
                return True

            if index == len(nums):
                return False
            
            dp[(index, remaining)] = helper(index+1, remaining) or helper(index+1, remaining - nums[index])

            return dp[(index, remaining)]
        
        return helper(0, target)
