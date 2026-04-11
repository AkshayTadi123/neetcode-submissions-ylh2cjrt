class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        result = []


        def helper(row, col, visited, prevHeight):
            if ((row, col) in visited or row<0 or col<0 or row>=rows or col>=cols or heights[row][col]<prevHeight):
                return
            visited.add((row, col))
            helper(row+1, col, visited, heights[row][col])
            helper(row-1, col, visited, heights[row][col])
            helper(row, col+1, visited, heights[row][col])
            helper(row, col-1, visited, heights[row][col])
          
        for c in range(cols):
            helper(0, c, pacific, heights[0][c]) 
            helper(rows-1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            helper(r, 0, pacific, heights[r][0]) 
            helper(r, cols-1, atlantic, heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if(r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        
        return result





