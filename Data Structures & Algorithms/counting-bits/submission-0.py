class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def counter(n: int):
            count = 0
            while n:
                count += n%2
                n = n>>1
            return count


        result = []
        for i in range(n+1):
            result.append(counter(i))
        return result

    
