class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def helper(i, j):
            temp1 = 0
            if i == len(nums):
                return 0
            if nums[i]>nums[j] or j==-1:
                temp1 = 1 + helper(i+1, i)
            temp2 = helper(i+1, j)
            return max(temp1, temp2)
        return helper(0, -1)


