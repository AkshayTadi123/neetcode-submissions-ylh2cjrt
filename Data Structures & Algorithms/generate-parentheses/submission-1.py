class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        res = []

        def helper(open_num, closed_num):
            if open_num == closed_num == n:
                res.append("".join(temp))
                return

            if open_num < n:
                temp.append("(")
                helper(open_num + 1, closed_num)
                temp.pop()
            if closed_num < open_num:
                temp.append(")")
                helper(open_num, closed_num + 1)
                temp.pop()

        helper(0, 0)
        return res