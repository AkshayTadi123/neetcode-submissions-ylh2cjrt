class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stops = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stops[stop].append(i)
        
        seen_bus = set()
        seen_stop = set([source])
        result = 0
        q = deque([source])

        while q:
            for i in range(len(q)):
                stop = q.popleft()
                if stop == target:
                    return result
                for bus in stops[stop]:
                    if bus in seen_bus:
                        continue
                    seen_bus.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop in seen_stop:
                            continue
                        seen_stop.add(next_stop)
                        q.append(next_stop)
            result += 1
        
        return -1


            
        