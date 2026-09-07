class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result=[]
        data = []
        distances = []

        def distance(point):
            x1, y1 = point[0], point[1]
            return (x1**2 + y1**2) ** 0.5
        
        
        heapq.heapify(data)
        for i in range(len(points)):
            heapq.heappush(data, (distance(points[i]), points[i]))

        for i in range(k):
            bla, req_point = heapq.heappop(data)
            result.append(req_point)
        
        return result