class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = Counter(nums)
        for i, j in table.items():
            if j > len(nums)//2:
                return i

        