class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        x = self.array[self.size-1]
        self.size -= 1
        return x

    def resize(self) -> None:
        x = [None] * (2 * self.capacity)
    
        for i in range(self.size):
            x[i] = self.array[i]
    
        self.array = x
        self.capacity *= 2
        
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity