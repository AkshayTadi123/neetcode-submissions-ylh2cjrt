# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        size = 0
        i = 0
        while(current):
            size+=1
            current = current.next
        current = head

        if(size==0):
            return None
        pointer = size-n
        if(pointer==0):
            return head.next
        while(i!=pointer):
            temp = current
            current = current.next
            i = i+1
        temp.next = current.next
        current.next = None
        return head
        



