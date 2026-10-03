class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for i in range(1,target+1):
            dp[i] = 0
            for num in nums:
                if i>=num:
                    dp[i] += dp.get(i-num, 0)
        return dp[target]
