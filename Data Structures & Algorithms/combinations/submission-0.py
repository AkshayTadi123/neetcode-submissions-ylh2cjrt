class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(num, subset):
            if len(subset) == k:
                result.append(subset)
                return
            
            if num == n+1:
                return
            
            helper(num+1, subset + [num])
            helper(num+1, subset)

        helper(1, [])
        return result