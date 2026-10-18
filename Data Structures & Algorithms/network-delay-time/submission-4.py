class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        for source, target, time in times:
            adj_list[source].append([target, time])

        completed = set()
        heap = [[0,k]]
        result = [float('inf')]*n
        result[k-1] = 0

        while heap:
            x,y = heapq.heappop(heap)
            if y in completed:
                continue
            completed.add(y)

            for node, time in adj_list[y]:
                if x+time < result[node-1]:
                    result[node-1] = x+time
                    heapq.heappush(heap, [x+time, node])

        return max(result) if float('inf') not in result else -1
            