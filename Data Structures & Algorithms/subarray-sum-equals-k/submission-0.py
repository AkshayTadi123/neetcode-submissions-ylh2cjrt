class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        running = 0
        count = 0
        for p in nums:
            running += p
            count += seen[running - k]
            seen[running] += 1
        return count