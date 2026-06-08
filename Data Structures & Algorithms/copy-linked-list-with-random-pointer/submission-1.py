"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copy = {}

        if not head:
            return None
        
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        
        for (key, val) in copy.items():
            if key.next:
                val.next = copy[key.next]

            if key.random:
                val.random = copy[key.random]

        return copy[head]
