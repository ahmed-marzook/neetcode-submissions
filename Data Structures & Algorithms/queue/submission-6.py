from typing import Optional

class Item:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def append(self, value: int) -> None:
        if self.isEmpty():
            self.appendleft(value)
        else:
            new_item = Item(value)
            self.tail.next = new_item
            new_item.prev = self.tail
            self.tail = new_item
            self.size +=1

    def appendleft(self, value: int) -> None:
        new_item = Item(value)
        if self.isEmpty():
            self.head = self.tail = new_item
        else:
            new_item.next = self.head
            self.head.prev = new_item
            self.head = new_item
        self.size +=1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.tail.val
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
        self.size -=1
        return val
    
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.head.val
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
        self.size -= 1
        return val