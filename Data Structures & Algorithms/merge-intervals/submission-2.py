class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for i in range(len(intervals)-1):
            x1, y1 = intervals[i][0], intervals[i][1]
            x2, y2 = intervals[i+1][0], intervals[i+1][1]
            if y1<x2:
                result.append(intervals[i])
            else:
                intervals[i+1] = [x1, max(y1, y2)]

        result.append(intervals[-1])
        return result
