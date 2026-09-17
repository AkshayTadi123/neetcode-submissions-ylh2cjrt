class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        result = 0
        def dfs(i, j):
            nonlocal result
            if (i,j) in visited:
                return
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return
            if grid[i][j] == 1:
                result+=4
                if((i+1)<len(grid) and grid[i+1][j]==1):
                    result-=1
                if((i-1)>=0 and grid[i-1][j]==1):
                    result-=1
                if((j+1)<len(grid[0]) and grid[i][j+1]==1):
                    result-=1
                if(((j-1)>=0) and grid[i][j-1]==1):
                    result-=1
            visited.add((i,j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        dfs(0,0)
        return result