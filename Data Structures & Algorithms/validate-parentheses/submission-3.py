class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {']':'[', '}':'{', ')':'('}
        for c in s:
            if(c in dict1):
                if(not stack or stack[-1] != dict1[c]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False