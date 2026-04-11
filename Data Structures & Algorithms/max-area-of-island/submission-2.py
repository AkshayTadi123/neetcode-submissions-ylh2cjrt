class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visit = set()
        result = 0
        def dfs(i, j):
            if((i,j) in visit or i not in range(0,len(grid)) or j not in range(0, len(grid[0])) or grid[i][j] == 0):
                return 0

            visit.add((i,j))
            return 1+ dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i,j) not in visit:
                   result = max(result, dfs(i,j))
                    
        return result



            