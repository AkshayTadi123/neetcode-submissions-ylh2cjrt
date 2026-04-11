# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str_num1 = ""
        str_num2 = ""

        curr = l1
        while curr:
            str_num1 += str(curr.val)
            curr = curr.next


        curr = l2
        while curr:
            str_num2 += str(curr.val)
            curr = curr.next

        num1 = int(str_num1[::-1])
        num2 = int(str_num2[::-1])
        res = num1+num2
        str_res = (str(num1+num2))[::-1]
        

        head = ListNode(int(str_res[0]))
        curr = head
        print(head.val)
        for i in range(1, len(str_res)):
            dummy = ListNode()
            curr.next = dummy
            curr = curr.next
            curr.val = int(str_res[i])
            print(curr.val)
        
        return head
        


        