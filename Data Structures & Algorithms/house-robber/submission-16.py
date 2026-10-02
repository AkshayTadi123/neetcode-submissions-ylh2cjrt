class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def helper(index, cost):
            if (index, cost) in dp:
                return dp[(index, cost)]

            if index>=len(nums):
                return cost
            
            dp[(index, cost)] = max(helper(index+1, cost), helper(index+2,cost+nums[index]))
            return dp[(index, cost)]

        return helper(0, 0)

        

