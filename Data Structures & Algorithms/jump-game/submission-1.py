class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def helper(nums: List[int], index: int):
            result = False
            if(index>=len(nums)):
                return False
            elif(index == len(nums)-1):
                return True
            else:
                if(nums[index] == 0):
                    return False
                for j in range(1, nums[index]+1):
                    result = result or helper(nums, index+j)
                return result


        return helper(nums, 0)
        
                




        