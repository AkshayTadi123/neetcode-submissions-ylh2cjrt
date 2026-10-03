class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,t = 0, 0
        r, b = len(matrix)-1, len(matrix)-1

        while b>=t:
            iterations = r-l
            for i in range(iterations):
                w = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = w
            l+=1
            r-=1
            b-=1
            t+=1
                

