class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                distance = abs(x1-x2)+abs(y1-y2)
                adj_list[(x1,y1)].append([distance, (x2,y2)])
                adj_list[(x2,y2)].append([distance, (x1,y1)])

        result = 0
        visited = set()
        min_heap = [(0, (points[0][0], points[0][1]))]
        heapq.heapify(min_heap)

        while len(visited)<len(points):
            cost, (x,y) = heapq.heappop(min_heap)
            if (x,y) in visited:
                continue
            visited.add((x, y))
            result += cost
            for neiCost, (nei_x, nei_y) in adj_list[(x,y)]:
                if (nei_x, nei_y) not in visited:
                    heapq.heappush(min_heap, (neiCost, (nei_x, nei_y)))

        return result