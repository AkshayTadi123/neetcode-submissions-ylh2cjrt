class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def helper(index, max_num):
            if (index, max_num) in dp:
                return dp[(index, max_num)]

            if index >= len(nums):
                return 0
            
            if nums[index] > max_num:
                x =  max(1+helper(index+1, nums[index]), helper(index+1, max_num))
            else:
                x = helper(index+1, max_num)

            dp[(index, max_num)] = x
            return dp[(index, max_num)]

        return helper(0, float('-inf'))
            



