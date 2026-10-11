class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = defaultdict(int)
        for i in range(len(nums)):
            mapp[nums[i]] += 1
        
        heap = []
        for key, val in mapp.items():
            heap.append((-val, key))
        
        heapq.heapify(heap)

        result = []
        for i in range(k):
            x, y = heapq.heappop(heap)
            result.append(y)
        
        return result



            
