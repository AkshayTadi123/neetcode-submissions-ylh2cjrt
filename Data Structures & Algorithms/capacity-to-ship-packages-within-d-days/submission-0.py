class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(C):
            days, load = 1, 0
            for p in weights:
                if load + p > C:
                    days += 1
                    load = 0
                load += p
            return days

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if days_needed(mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo