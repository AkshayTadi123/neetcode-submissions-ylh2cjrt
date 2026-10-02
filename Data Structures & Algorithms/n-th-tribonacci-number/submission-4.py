class Solution:
    def tribonacci(self, n: int) -> int:   
        result = [0, 1, 1]
        if n<3:
            return result[n]
            
        for i in range(3, n+1):
            result.append(result[i-3]+result[i-2]+result[i-1])
        return result[-1]
        
        