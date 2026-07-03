class Node {
    int val;
    Node next;
    Node prev;

    public Node(int val) {
        this.val = val;
    }
}

class Deque {
     
    Node head;
    Node tail;
    int size;

    public Deque() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public void append(int value) {
        Node newNode = new Node(value);
        if(this.size == 0) {
            this.head = newNode;
            this.tail = newNode;
            this.size++;
            return;
        }
        this.tail.next = newNode;
        newNode.prev = this.tail;
        this.tail = newNode;
        this.size++;
    }

    public void appendleft(int value) {
        Node newNode = new Node(value);
        if(this.size == 0) {
            append(value);
            return;
        }
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
        this.size++;
        return;
    }

    public int pop() {
        if(this.size <= 0) {
            return -1;
        }
        int val = this.tail.val;
        if(this.size == 1) {
            this.tail = null;
            this.head = null;
            this.size--;
            return val;
        }
        this.tail = this.tail.prev;
        this.size--;
        return val;
    }

    public int popleft() {
        if(this.size <= 0) {
            return -1;
        }
        if(this.size == 1) {
            return pop();
        }
        int val = this.head.val;

        this.head = this.head.next;
        this.head.prev = null;
        this.size--;
        return val;
    }
}
