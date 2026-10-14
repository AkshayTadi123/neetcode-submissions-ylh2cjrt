class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        distance = defaultdict(lambda: float('inf'))
        distance[k] = 0
        heap = [(0, k)]
        
        while heap:
            x, y = heapq.heappop(heap)
            if x>distance[y]:
                continue
            
            for target, time in graph[y]:
                new_time = time + x
                if new_time < distance[target]:
                    distance[target] = new_time
                    heapq.heappush(heap, (new_time, target))

        
        return max(distance.values()) if len(distance) == n else -1

