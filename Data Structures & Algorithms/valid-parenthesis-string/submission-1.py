class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []
        
        for i, c in enumerate(s):
            if c == ")":
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif c == "(":
                open.append(i)
            else:
                star.append(i)

        while open and star:
            if open[-1] < star [-1]:
                open.pop()
                star.pop()
            else:
                return False
           
        
        
        return not open


        