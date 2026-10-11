class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.mapp = {}
        self.capacity = capacity
        self.curr_cap = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, key: int) -> int:
        if key in self.mapp:
            x = self.mapp[key]
            self.remove(x)
            self.add(x)
            return x.val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mapp:
            self.remove(self.mapp[key])
            self.mapp[key] = Node(key, value)
            self.add(self.mapp[key])
        else:
            if self.curr_cap + 1 > self.capacity:
                del self.mapp[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            self.mapp[key] = Node(key, value)
            self.add(self.mapp[key])
            self.curr_cap += 1
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        x = self.tail.prev
        x.next = node
        node.prev, node.next = x, self.tail
        self.tail.prev = node
