class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def helper(i, total):
            if(i == len(nums)):
                return 1 if total == target else 0
            else:
                return(helper(i+1, total + nums[i]) + helper(i+1, total - nums[i]))
            
        return helper(0, 0)
        
