class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)-1):
            x1, y1 = intervals[i]
            x2, y2 = intervals[i+1]

            if x2<=y1:
                intervals[i+1] = [x1, max(y1,y2)]
                continue
            result.append([x1, y1])

        result.append(intervals[-1])
        return result

