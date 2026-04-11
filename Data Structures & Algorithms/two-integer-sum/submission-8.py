class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                current_sum = nums[i] + nums[j]
                if current_sum == target:
                    return [i, j]
                j += 1
            i += 1
