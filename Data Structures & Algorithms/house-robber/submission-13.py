class Solution:
    def rob(self, nums: List[int]) -> int:
        result = nums + [0,0, 0]
        for i in range(len(nums)-1,-1,-1):
            result[i] = max(nums[i] + result[i+3], nums[i] + result[i+2])
        
        return max(result[0], result[1])

        

