class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_ver = set(nums)
        for num in nums:
            if num in set_ver:
                set_ver.remove(num)
            else:
                return num
        