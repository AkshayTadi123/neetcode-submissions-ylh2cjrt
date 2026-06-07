class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            while stack and stack[-1][0] < j:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([j, i])
        return res