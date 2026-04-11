class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            x = (n>>i)&1
            result += x<<(31-i)
            
        return result


            
            