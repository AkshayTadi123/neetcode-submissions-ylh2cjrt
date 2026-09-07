class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(data)

        return [heapq.heappop(data)[1] for z in range(k)]