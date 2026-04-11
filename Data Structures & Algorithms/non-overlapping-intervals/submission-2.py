class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        for i in range(len(intervals)-1):
            if(intervals[i][1]<=intervals[i+1][0]):
                continue
            else:
                temp1 = intervals[i][1]
                temp2 = intervals[i+1][1]
                if temp2>=temp1:
                    intervals[i+1] = intervals[i]
                count += 1
        return count