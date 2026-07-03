class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur.val
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.insertHead(val)
            return
        new_node = ListNode(val)
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            cur = self.head
            for _ in range(index -1):
                cur = cur.next
            cur.next = cur.next.next
            if not cur.next:
                self.tail = cur
        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values