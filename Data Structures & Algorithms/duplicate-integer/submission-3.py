class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ver = set(nums)
        return len(set_ver) != len(nums)