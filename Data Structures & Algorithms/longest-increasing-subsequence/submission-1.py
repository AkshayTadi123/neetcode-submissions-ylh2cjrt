class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def helper(i, j):
            if i == len(nums):
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            temp1 = 0

            if nums[i]>nums[j] or j==-1:
                temp1 = 1 + helper(i+1, i)

            temp2 = helper(i+1, j)
            dp[(i,j)] = max(temp1, temp2)
            return dp[(i,j)]

        return helper(0, -1)


