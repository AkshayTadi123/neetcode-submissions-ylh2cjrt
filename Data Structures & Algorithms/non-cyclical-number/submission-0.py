class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n!=1:
            if n in visited:
                return False

            visited.add(n)
            a = n
            b = 0
            while a:
                b += (a%10)**2
                a = a//10

            n = b
        return True