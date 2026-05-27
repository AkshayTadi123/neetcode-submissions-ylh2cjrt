class Solution:
    res = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def helper(open_available, close_available, curr_res):
            if open_available == 0 and close_available == 0:
                self.res.append(curr_res)
            
            if open_available>close_available:
                return
            
            if(open_available > 0):
                helper(open_available-1, close_available, curr_res + "(")

            if(close_available > 0):  
                helper(open_available, close_available-1, curr_res + ")")


        helper(n, n, "")
        return self.res

        