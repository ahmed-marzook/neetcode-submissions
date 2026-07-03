class Node {
    int val;
    Node next;

    public Node(int val){
        this.val = val;
        this.next = null;
    }
}
class LinkedList {
    private Node head;
    private Node tail;
    private int size;

    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public int get(int index) {
        if(index >= this.size || index < 0){
            return -1;
        }
        Node curr = this.head;
        int i = 0;
        while(curr != null && i < index) {
            curr = curr.next;
            i++;
        }
        return curr.val;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        if(this.size == 0) {
            this.head = newNode;
            this.tail = this.head;
            this.size++;
            return;
        }
        newNode.next = this.head;
        this.head = newNode;
        this.size++;
        System.out.println(getValues());
        return;
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);
        if(this.size == 0) {
            this.head = newNode;
            this.tail = this.head;
            this.size++;
            return;
        }
        this.tail.next = newNode;
        this.tail = newNode;
        this.size++;
        System.out.println(getValues());
        return;
    }

    public boolean remove(int index) {
        if(index >= this.size || index < 0){
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
        int i = 0;
        while(curr != null && i < index - 1) {
            System.out.println(curr.val);
            curr = curr.next;
            i++;
        }
        curr.next = curr.next.next;
        if(curr.next == null){
            this.tail = curr;
        }
        this.size--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> results = new ArrayList();
        Node curr = this.head;
        while(curr != null) {
            results.add(curr.val);
            curr = curr.next;
        }
        return results;
    }
}
