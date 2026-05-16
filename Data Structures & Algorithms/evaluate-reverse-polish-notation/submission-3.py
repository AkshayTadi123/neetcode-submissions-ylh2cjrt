import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                result = ops[tokens[i]](stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)

        return stack[0]




