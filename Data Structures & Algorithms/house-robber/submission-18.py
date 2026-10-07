class Solution:
    def rob(self, nums: List[int]) -> int:
        result = [0]*(len(nums)+2)
        for i in range(len(nums)-1, -1, -1):
            result[i] = max(result[i+1], nums[i]+result[i+2])
        
        return result[0]

        

        

