# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        currentNode = dummy

        while(list1 != None and list2!=None):
            if(list1.val<list2.val):
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next

        if(list1 == None):
            currentNode.next = list2
        else:
            currentNode.next = list1
        
        return dummy.next
            
