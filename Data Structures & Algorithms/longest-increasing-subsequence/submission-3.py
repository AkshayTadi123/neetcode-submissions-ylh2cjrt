class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[-1] = 1
        
        for i in range(len(nums)-2, -1, -1):
            x = 1
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    x = max(x, 1+dp[j])
            dp[i] = x
        
        return max(dp)
        

            



