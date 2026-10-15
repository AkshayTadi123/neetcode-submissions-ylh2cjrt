class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in seen:
                result += seen[remainder]
            seen[remainder] += 1
        return result