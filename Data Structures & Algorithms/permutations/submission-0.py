class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        included = set()

        def helper(curr, included):
            if len(included) == len(nums):
                result.append(current.copy())
                return
            
            for i in range(len(nums)):
                if(nums[i] in included):
                    continue
                else:
                    included.add(nums[i])
                    curr.append(nums[i])
                    helper(curr, included)
                    curr.remove(nums[i])
                    included.remove(nums[i])

        helper(current, included)
        return result