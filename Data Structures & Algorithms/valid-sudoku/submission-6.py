class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row_map = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_map:
                        return False
                    row_map.append(board[i][j])


        for i in range(9):
            column_map = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in column_map:
                        return False
                    column_map.append(board[j][i])
        
        for i in range(3):
            for j in range(3):
                square_map = []
                for k in range(3):
                    for l in range(3):
                        if board[3*i + k][3*j + l] != ".":
                            if board[3*i + k][3*j + l] in square_map:
                                return False
                            square_map.append(board[3*i + k][3*j + l])

        return True



        