class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        res = list(map.items())
        res.sort(key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(res[i][0])
        return result
