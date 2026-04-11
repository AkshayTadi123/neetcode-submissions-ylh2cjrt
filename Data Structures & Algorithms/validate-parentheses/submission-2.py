class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if(char == '(' or char == "{" or char == "["):
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False

                if(char == ")" and stack[-1]!= "("):
                    return False
                elif(char == "}" and stack[-1]!= "{"):
                    return False
                elif(char == "]" and stack[-1]!= "["):
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False