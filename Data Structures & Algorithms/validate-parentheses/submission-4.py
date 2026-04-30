class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "{", "["]
        close =[")", "}", "]"]

        for c in s:
            if c in open:
                stack.append(c)
            else:
                if(len(stack) == 0):
                    return False
                x = stack.pop()
                if c == "}" and x != "{":
                    return False
                elif c == "]" and x != "[":
                    return False
                elif c == ")" and x != "(":
                    return False
        
        return len(stack)==0
                