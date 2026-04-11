class Solution:
    dic = {}

    def rob(self, nums: List[int]) -> int:
        self.dic = {}
        count1 = self.helper(nums, 0)
        return count1

    def helper(self, nums: List[int], index: int):
        if(index>=len(nums)):
            return 0
        else:
            if(index in self.dic):
                return self.dic[index]
            else:
                loot1 = nums[index] + self.helper(nums, index+2)
                loot2 = self.helper(nums, index+1)
                self.dic[index] = max(loot1, loot2)
                return self.dic[index]
        
        