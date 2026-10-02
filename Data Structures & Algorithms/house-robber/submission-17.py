class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def helper(index):
            if index in dp:
                return dp[index]

            if index>=len(nums):
                return 0
            
            dp[index] = max(helper(index+1), nums[index]+ helper(index+2))
            return dp[index]

        return helper(0)

        

