class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.user_array = [0] * capacity 

    def get(self, i: int) -> int:
        return self.user_array[i]

    def set(self, i: int, n: int) -> None:
        self.user_array[i] = n

    def pushback(self, n: int) -> None:
        if(self.length >= self.capacity):
            self.resize()
        self.user_array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        print("Array",self.user_array)
        if self.length > 0:
            self.length -= 1
        print("Array",self.user_array)
        return self.user_array[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(len(self.user_array)):
            new_array[i] = self.user_array[i]

        self.user_array = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity