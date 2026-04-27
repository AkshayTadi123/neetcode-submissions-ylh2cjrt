class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            map[i] = num
            if target-num in nums[i+1:]:
                return [i, nums[i+1:].index(target-num)+i+1]
