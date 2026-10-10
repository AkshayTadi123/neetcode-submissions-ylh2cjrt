class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        coordinates = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j, visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in coordinates:
                x_coord, y_coord = x+i, y+j
                if x_coord>=0 and y_coord>=0 and x_coord<len(heights) and y_coord<len(heights[0]) and heights[x+i][y+j]>=heights[i][j]:
                    dfs(x+i, y+j, visited)

        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0])-1, atlantic)
        for i in range(len(heights[0])):
            dfs(0, i, pacific)
            dfs(len(heights)-1, i, atlantic)

        result = []
        for x in pacific:
            if x in atlantic:
                result.append(list(x))

        return result
            