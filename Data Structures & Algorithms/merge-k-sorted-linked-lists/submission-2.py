# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            x = lists[i]
            if x:
                heap.append((x.val, i, x))
        heapq.heapify(heap)

        head = ListNode()
        curr = head

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next





        
