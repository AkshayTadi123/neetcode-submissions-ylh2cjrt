class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                distance = abs(x1-x2)+abs(y1-y2)
                adj_list[i].append([distance, j])
                adj_list[j].append([distance, i])

        result = 0
        visited = set()
        min_heap = [(0, 0)]
        heapq.heapify(min_heap)

        while len(visited)<len(points):
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            result += cost
            for neiCost, j in adj_list[i]:
                if j not in visited:
                    heapq.heappush(min_heap, (neiCost, j))

        return result