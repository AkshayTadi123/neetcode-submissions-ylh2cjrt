class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        req_list = []
        def helper(total, index):
            if index == len(nums):
                return total

            return helper(total ^ nums[index], index+1) + helper(total, index+1)
        
        return helper(0,0)