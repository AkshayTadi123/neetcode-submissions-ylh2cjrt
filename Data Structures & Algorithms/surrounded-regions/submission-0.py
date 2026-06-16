class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        zero_cells = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    zero_cells.add((i,j))
        
        def dfs(i, j):
            if i<0 or j<0 or i==len(board) or j==len(board[0]) or board[i][j] == 'X' or (i,j) in visit:
                return

            visit.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(len(board)):
            dfs(i, 0)
        
        for i in range(len(board)):
            dfs(i, len(board[0])-1)
        
        for j in range(1, len(board[0])-1):
            dfs(0, j)
        
        for j in range(1, len(board[0])-1):
            dfs(len(board)-1, j)

        for (i, j) in zero_cells:
            if (i, j) not in visit:
                board[i][j] = 'X'
                

        

