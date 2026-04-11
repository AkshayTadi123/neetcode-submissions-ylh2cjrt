class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)-1):
            if(intervals[i][1]<intervals[i+1][0]):
                result.append(intervals[i])
            if(intervals[i+1][0]<=intervals[i][1]):
                x =   min(intervals[i][0], intervals[i+1][0])
                y =   max(intervals[i][1], intervals[i+1][1])
                intervals[i+1] = [x,y]
        result.append(intervals[-1])
        return result