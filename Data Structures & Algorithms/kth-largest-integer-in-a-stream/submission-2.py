class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = [-num for num in nums]
        heapq.heapify(self.min_heap)
        self.k = k

    def add(self, val: int):
        heapq.heappush(self.min_heap, -val)
        bla = []
        for i in range(self.k):
            x = heapq.heappop(self.min_heap)
            bla.append(x)
        
        for num in bla:
            heapq.heappush(self.min_heap, num)
            

        return -x