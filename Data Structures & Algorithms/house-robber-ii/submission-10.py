class Solution:
    memo = {}
    def rob(self, nums: List[int]) -> int:
        self.memo= {}
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)

        first = nums[0] + self.helper(nums, 2, False)
        second = self.helper(nums, 1, True)
        return max(first, second)
    
    def helper(self, nums: List[int], index: int, last: bool) -> int:
        if ((index >= len(nums)) or (index == len(nums)-1 and not last)):
            return 0

        if (index, last) in self.memo:
            return self.memo[(index, last)]
        
        x = nums[index] + self.helper(nums, index+2, last)
        y = self.helper(nums, index + 1, last)
        self.memo[(index, last)] = max(x,y)
        return self.memo[(index, last)]
        




        

