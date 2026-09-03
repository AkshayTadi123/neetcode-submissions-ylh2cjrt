# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 0
        left1 = left
        curr = head
        prev = None
        before_left = curr
        tail = None
        while curr and left <= right:
            index+=1
            if index<left:
                prev,before_left = curr, curr
                curr = curr.next
            else:
                if not tail:
                    tail = curr
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                left += 1
        
        before_left.next = prev
        tail.next = curr
        if left1 == 1:
            return prev
        return head
