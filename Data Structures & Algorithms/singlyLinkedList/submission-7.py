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
        i = 0
        cur = self.head
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = self.head
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
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = self.head
            return True
        
        i = 0
        cur = self.head
        while cur:
            if i == index - 1:
                break
            cur = cur.next
            i += 1
            

        if cur.next:
            cur.next = cur.next.next
            self.size -= 1
            if self.size == 1:
                self.tail = self.head
            return True
        else:
            cur.next = None
            self.size -= 1
            if self.size == 1:
                self.tail = self.head
            return True

    def getValues(self) -> list[int]:
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values