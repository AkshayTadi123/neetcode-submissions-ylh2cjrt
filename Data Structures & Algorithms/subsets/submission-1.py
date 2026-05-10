class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        temp = []
        def dfs(index):
            if index >= len(nums):
                res.append(temp.copy())
                return
            
            temp.append(nums[index])
            dfs(index+1)

            temp.pop()
            dfs(index+1)
        
        dfs(0)   
        return res

   