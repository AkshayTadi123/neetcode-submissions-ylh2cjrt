class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        length = self.getLength()
        if index>=length:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val


    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            prev = None
            while curr:
                prev = curr
                curr = curr.next
            prev.next = Node(val)

    def remove(self, index: int) -> bool:
        length = self.getLength()
        if index>=length:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True

        i = 0
        curr = self.head
        prev = None
        while i!=index:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        return True


    def getValues(self) -> List[int]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
    
    def getLength(self) -> int:
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next
        return length

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None