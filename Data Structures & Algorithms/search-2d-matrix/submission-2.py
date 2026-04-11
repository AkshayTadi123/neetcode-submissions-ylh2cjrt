class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(array, target):
            l = 0
            r = len(array)-1
            while l<=r:
                m = (l+r)//2
                if target<array[m]:
                    r = m-1
                elif target>array[m]:
                    l = m+1
                else:
                    return True
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target in range(matrix[i][0], matrix[i][n-1]+1):
                return binary(matrix[i], target)
            
        return False