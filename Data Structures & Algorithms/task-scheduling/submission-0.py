class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                a = heapq.heappop(heap)
                if((a+1) != 0):
                    q.append((a+1, time + n))
            
            if q and time == q[0][1]:
                b = q.popleft()[0]
                heapq.heappush(heap, b)
        return time
            

