# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if(not(head.next == None or head.next.next== None)):
            # finding the size of the sll
            size = 0
            current1 = head
            while(current1):
                size+=1
                current1 = current1.next
        
            #resetting current1 to point to head
            current1 = head
            current2 = head
            reqCurrent = current2
            #finding the middle node
            for i in range(0,size//2):
                reqCurrent = current2
                current2 = current2.next
            reqCurrent.next = None
            #reversing the second half of the sll. current2 is the head of this list rn
            prev = None
            temp = None
            while(current2):
                temp = current2.next
                current2.next = prev
                prev = current2
                current2 = temp

            #prev holds the head of the reversed linked list
            temp1 = current1.next
            temp2 = prev.next
            while(temp1 and temp2):
                current1.next = prev
                prev.next = temp1
                prev = temp2
                current1 = temp1
                temp1 = current1.next
                temp2 = prev.next
                
            current1.next = prev

            





        
        

