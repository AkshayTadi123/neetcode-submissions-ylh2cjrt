class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
            
        m, n = len(matrix), len(matrix[0])

        def isSquare(r, c):
            size = 1
            while r + size < m and c + size < n:
                newRow, newCol = r + size, c + size
                bottomOk = all(matrix[newRow][c + k] == "1" for k in range(size + 1))
                rightOk = all(matrix[r + k][newCol] == "1" for k in range(size))

                if not (bottomOk and rightOk):
                    break
                size += 1
            return size

        result = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    result = max(result, isSquare(r, c))
        return result * result 