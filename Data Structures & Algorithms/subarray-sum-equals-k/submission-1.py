class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum-k in seen:
                result += seen[prefix_sum-k]
            seen[prefix_sum] += 1
        return result