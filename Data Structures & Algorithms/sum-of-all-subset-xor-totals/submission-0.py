class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        req_list = []
        def helper(temp, index):
            if index == len(nums):
                req_list.append(temp)
                return

            helper(temp+ [nums[index]], index+1)
            helper(temp, index+1)
        
        helper([], 0)
        result = 0
        for x in req_list:
            temp2 = 0
            for y in x:
                temp2 ^= y
            result += temp2

        return result