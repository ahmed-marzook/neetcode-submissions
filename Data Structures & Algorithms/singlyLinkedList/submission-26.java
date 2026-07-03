class Node {
    int val;
    Node next;
    public Node(int val) {
        this.val = val;
    }
}

class LinkedList {
    int size;
    Node head;
    Node tail;

    public LinkedList() {
        this.size = 0;
        this.head = null;
        this.tail = null;
    }

    public int get(int index) {
        if(this.size == 0 || index < 0 || index > this.size - 1) {
            return -1;
        }
        Node curr = this.head;
        for(int i = 0; i < index; i++) {
            curr = curr.next;
        }
        return curr.val;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        if(this.size == 0) {
            this.head = newNode;
            this.tail = newNode;
            this.size++;
            return;
        }
        newNode.next = this.head;
        this.head = newNode;
        this.size++;
    }

    public void insertTail(int val) {
        if(this.size == 0) {
            insertHead(val);
            return;
        }
        Node newNode = new Node(val);
        this.tail.next = newNode;
        this.tail = newNode;
        this.size++;
    }

    public boolean remove(int index) {
        if(this.size == 0 || index < 0 || index > this.size - 1) {
            return false;
        }

        if(index == 0){
            this.head = this.head.next;
            if(this.head == null) {
                this.tail = null;
            }
            this.size--;
            return true;
        }
        Node curr = this.head;
        for(int i = 0; i < index - 1; i++) {
            curr = curr.next;
        }
        curr.next = curr.next.next;
        if(curr.next == null) {
            this.tail = curr;
        }
        this.size--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        Node curr = this.head;
        ArrayList<Integer> values = new ArrayList();
        while(curr != null) {
            values.add(curr.val);
            curr = curr.next;
        }
        return values;
    }
}
