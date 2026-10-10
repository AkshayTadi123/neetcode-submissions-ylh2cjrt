class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]

        adj_list = defaultdict(list)
        for x,y,z in times:
            adj_list[x].append((y,z))
        
        min_distance = {}
        for i in range(1, n+1):
            if i == k:
                min_distance[k] = 0
            else:
                min_distance[i] = float('inf')

        covered = set()
        
        while heap:
            dist, node = heapq.heappop(heap)
            if node in covered:
                continue
            covered.add(node)

            for nei, nei_dist in adj_list[node]:
                if min_distance[nei] > min_distance[node] + nei_dist:
                    min_distance[nei] = min_distance[node] + nei_dist
                heapq.heappush(heap, (min_distance[node] + nei_dist, nei))

        if float('inf') in min_distance.values():
            return -1
        else:
            return max(min_distance.values())
