class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        n = len(height)
        i = 0
        result = 0

        while i < n - 1:
            j = i + 1
            covered = 0
            max_right = j
            found_taller = False

            while j < n:
                if height[j] >= height[i]:
                    found_taller = True
                    break
    
                if height[j] > height[max_right]:
                    max_right = j
                covered += height[j]
                j += 1

            if found_taller:
                result += ((j - i - 1) * height[i]) - covered
                i = j 
            else:
                covered = 0
                for k in range(i + 1, max_right):
                    covered += height[k]
                result += ((max_right - i - 1) * height[max_right]) - covered
                i = max_right
        return result
