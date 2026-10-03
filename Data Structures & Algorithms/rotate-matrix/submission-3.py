class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0, len(matrix)-1

        while r>=l:
            for i in range(r-l):
                t, b = l, r
                w = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = w
            l+=1
            r-=1
                

