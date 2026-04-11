class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def helper(nums: List[int], comb: List[int], target: int, result: List[List[int]], index: int):
            if target == 0:
                result.append(comb[:])
                return
            elif target<0:
                return
            else:
                for i in range(index, len(nums)):
                    comb.append(nums[i])
                    helper(nums, comb, target-nums[i], result, i)
                    comb.pop()

        
        result = []
        helper(nums, [], target, result, 0)
        return result

        
        
        

    


        