class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0 
        l,r = 0, len(heights)-1 
        max_left, max_right = heights[l], heights[r] 
        while l<r: 
            area = min(heights[l], heights[r]) * (r-l) 
            result = max(result, area) 
            if max_left<max_right: 
                l += 1 
                max_left = max(max_left, heights[l]) 
            else: 
                r -= 1 
                max_right = max(max_right, heights[r]) 
        return result
        