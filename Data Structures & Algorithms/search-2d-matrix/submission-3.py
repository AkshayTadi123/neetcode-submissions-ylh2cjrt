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
        
        n = len(matrix)-1
        m = 0

        while(m<=n):
            o = (m+n)//2
            if target>matrix[o][-1]:
                m = o+1
            elif target<matrix[o][0]:
                n = o-1
            else:    
                return binary(matrix[o], target)

        return False
        
