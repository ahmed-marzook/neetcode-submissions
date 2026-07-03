class Item {
    int val;
    Item next;
    Item prev;

    public Item(int val) {
        this.val = val;
    }
}

class Deque {
    Item head;
    Item tail;
    int size;

    public Deque() {
        this.head = null;
        this.tail = this.head;
        this.size = 0;
    }

    public boolean isEmpty() {
        if(this.size == 0) {
            return true;
        }
        return false;
    }

    public void append(int value) {
       Item newItem = new Item(value);
       if(isEmpty()) {
        this.head = newItem;
        this.tail = newItem;
        this.size +=1;
        return;
       }
       newItem.prev = this.tail;
       this.tail.next = newItem;
       this.tail = newItem;
       this.size +=1;
    }

    public void appendleft(int value) {
        Item newItem = new Item(value);
        if(isEmpty()) {
            this.head = newItem;
            this.tail = newItem;
            this.size +=1;
            return;
        }
        newItem.next = this.head;
        this.head.prev = newItem;
        this.head = newItem;
        this.size += 1;
    }

    public int pop() {
        if(isEmpty()) {
            return -1;
        }
        Item returnVal = this.tail;
        if(size == 1) {
            this.size -= 1;
            this.head = null;
            this.tail = null;
            return returnVal.val;
        }
        this.tail = this.tail.prev;
        this.tail.next = null;
        this.size -= 1;
        return returnVal.val;
    }

    public int popleft() {
        if(isEmpty()) {
            return -1;
        }
        Item returnVal = this.head;
        if(size == 1) {
            this.size -= 1;
            this.head = null;
            this.tail = null;
            return returnVal.val;
        }
        this.head = this.head.next;
        this.head.prev = null;
        this.size -= 1;
        return returnVal.val;
    }
}
