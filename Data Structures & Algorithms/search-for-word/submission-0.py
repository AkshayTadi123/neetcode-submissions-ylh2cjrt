class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(board)
        width = len(board[0])
        hashset = set()

        def helper(x: int, y: int, index: int, visited: set[tuple[int, int]]):
            if(index==len(word)):
                return True
            if(x<0 or y<0 or x>=width or y>=length):
                return False
            if(y,x) in visited:
                return False
            if(board[y][x] != word[index]):
                return False
                
            visited.add((y,x))
            found = (
                helper(x+1, y, index+1, visited) or
                helper(x-1, y, index+1, visited) or
                helper(x, y+1, index+1, visited) or
                helper(x, y-1, index+1, visited)
            )
            visited.remove((y, x))
            
            return found
        
        for r in range(length):
            for c in range(width):
                if helper(c, r, 0, set()):
                    return True

        return False
