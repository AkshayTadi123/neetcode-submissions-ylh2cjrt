class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if(len(heights)<2):
            return 0
        area = 0
        l = 0
        r = len(heights)-1
        while(l<r):
            area2 = min(heights[l],heights[r]) * (r-l)
            area = max(area2, area)
            if((min(heights[l]+1,heights[r])*(r-l))> area2):
                l += 1
            else:
                r -= 1

        return area


        