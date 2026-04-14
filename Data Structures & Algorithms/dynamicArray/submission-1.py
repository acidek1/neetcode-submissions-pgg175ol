class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if (n < self.capacity):
            self.arr[self.capacity-1] = self.arr[n]

    def popback(self) -> int:
        return self.arr[self.capacity]

    def resize(self) -> None:
        self.capacity*2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.capacity
