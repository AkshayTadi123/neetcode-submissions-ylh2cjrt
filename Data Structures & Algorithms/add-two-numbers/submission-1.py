# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits = []
        curr = l1
        while curr:
            digits.append(str(curr.val))
            curr = curr.next
        str_num1 = "".join(digits)


        digits = []
        curr = l2
        while curr:
            digits.append(str(curr.val))
            curr = curr.next
        str_num2 = "".join(digits)

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
        


        