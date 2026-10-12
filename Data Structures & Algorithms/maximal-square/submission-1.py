class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = [[0]*(n+1) for _ in range(m+1)]
        best = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    result[i][j] = 1+min(result[i-1][j-1], result[i][j-1], result[i-1][j])
                best = max(best, result[i][j])

        return best*best


            
        