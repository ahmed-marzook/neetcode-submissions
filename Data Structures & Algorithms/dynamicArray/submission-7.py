class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if (self.size + 1) > self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        val = self.array[self.size]
        self.array[self.size] = 0
        return val

    def resize(self) -> None:
        self.capacity *= 2
        newArray = [0] * (self.capacity)

        for i in range(len(self.array)):
            newArray[i] = self.array[i]
        
        self.array = newArray

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity