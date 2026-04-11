class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        def dfs(i):
            if i>=len(nums):
                result.append(temp.copy())
                return
            
            temp.append(nums[i])
            dfs(i+1)

            temp.pop()
            dfs(i+1)
        
        dfs(0)
        return result