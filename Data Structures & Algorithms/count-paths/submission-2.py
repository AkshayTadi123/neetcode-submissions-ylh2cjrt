class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def helper(x, y):
            if x>=m or y>=n:
                return 0

            if x==m-1 and y==n-1:
                return 1
            
            if (x,y) in dp:
                return dp[(x,y)]

            dp[(x,y)] = helper(x+1, y) + helper(x, y+1)
            return dp[(x,y)]
        
        return helper(0, 0)


            

                
            
