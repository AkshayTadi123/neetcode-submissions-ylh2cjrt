class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result = [False]*(len(nums))
        result[-1] = True
        for i in range(len(nums)-1, -1, -1):
            for j in range(1, nums[i]+1):
                if i+j < len(result) and result[i+j] == True:
                    result[i] = True
            
        return result[0]