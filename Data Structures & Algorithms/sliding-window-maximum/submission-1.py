class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        maxHeap = []
        for i in range(k):
            maxHeap.append((-nums[i], i))
        heapq.heapify(maxHeap)
        result.append(-maxHeap[0][0])

        for j in range(k, len(nums)):
            new_tuple = (-nums[j], j)
            heapq.heappush(maxHeap, new_tuple)
            max_index = maxHeap[0][1]
            if max_index> j-k:
                result.append(-maxHeap[0][0])
            else:
                while maxHeap[0][1] < j - k + 1:
                    heapq.heappop(maxHeap)
                result.append(-maxHeap[0][0])
        return result
