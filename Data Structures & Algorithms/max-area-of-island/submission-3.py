class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or (i,j) in visited or grid[i][j]==0:
                return 0
            visited.add((i,j))
            temp = 1

            for x, y in coordinates:
                temp += dfs(i+x, j+y)
        
            return temp
        
        visited = set()
        coordinates = [(1,0), (-1,0), (0,1), (0,-1)]
        result = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    result = max(result, dfs(i,j))

        return result
        
        



            