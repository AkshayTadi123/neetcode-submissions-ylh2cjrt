class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dic1 = {}
        self.dic2 = {}
        loot1 = self.helper(nums, 0, False)
        loot2 = self.helper(nums, 1, True)
        return max(loot1, loot2)

    def helper(self, nums: List[int], index: int, considerLast: bool):
        if(index in self.dic1 and considerLast == False):
            return self.dic1[index]
        if(index in self.dic2 and considerLast):
            return self.dic2[index]
        if(index >= len(nums) or (index!= 0 and index==len(nums)-1 and considerLast==False)):
            return 0
        
        rob = nums[index] + self.helper(nums, index+2, considerLast)
        skip = self.helper(nums, index+1, considerLast)

        if(considerLast):
            self.dic2[index] = max(rob, skip)
        else:
            self.dic1[index] = max(rob, skip)

        return max(rob, skip)
        
        