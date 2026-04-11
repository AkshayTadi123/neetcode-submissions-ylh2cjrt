class MedianFinder:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.copy = self.heap[:]


    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        heapq.heappush(self.copy, num)

    def findMedian(self) -> float:
        if(len(self.heap)%2 == 0):
            for i in range((len(self.heap)-1)//2):
                heapq.heappop(self.copy)
            result1 = heapq.heappop(self.copy)
            result2 = heapq.heappop(self.copy)
            self.copy = self.heap[:]
            return (result1+result2)/2
        else:
            for i in range(len(self.heap)//2):
                heapq.heappop(self.copy)
            result = heapq.heappop(self.copy)
            self.copy = self.heap[:]
            return result
        