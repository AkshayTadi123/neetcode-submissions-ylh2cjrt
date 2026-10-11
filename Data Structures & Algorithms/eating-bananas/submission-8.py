class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        min_speed = 1
        def canFinish(speed):
            temp = 0
            for pile in piles:
                temp += (pile + speed - 1) // speed
            
            return True if temp <= h else False

        while min_speed<max_speed:
            mid = (min_speed+max_speed)//2
            if canFinish(mid):
                max_speed = mid
            else:
                min_speed = mid+1
        
        return min_speed


    
