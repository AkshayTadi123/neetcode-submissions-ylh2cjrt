class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        self.dic1 = {}
        self.dic2 = {}

        loot1 = self.helper(nums, 0, n - 2, self.dic1)
        loot2 = self.helper(nums, 1, n - 1, self.dic2)

        return max(loot1, loot2)

    def helper(self, nums, index, end, memo):
        if index > end:
            return 0
        if index in memo:
            return memo[index]
        
        rob = nums[index] + self.helper(nums, index + 2, end, memo)
        skip = self.helper(nums, index + 1, end, memo)
        memo[index] = max(rob, skip)
        return memo[index]