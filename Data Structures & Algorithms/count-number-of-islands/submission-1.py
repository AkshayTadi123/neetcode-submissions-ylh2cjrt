class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        coordinates = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def helper(i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return

            if (i,j) in visited or grid[i][j] == "0":
                return
            
            visited.add((i,j))
            for x,y in coordinates:
                helper(i+x, j+y)

        visited = set()
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    result += 1
                    helper(i,j)
                
        return result
