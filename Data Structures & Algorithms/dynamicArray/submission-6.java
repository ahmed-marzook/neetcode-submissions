class DynamicArray {

    private int[] userArray;
    private int size;
    private int capacity;

    public DynamicArray(int capacity) {
        this.userArray = new int[capacity];
        this.size = 0;
        this.capacity = capacity;
    }

    public int get(int i) {
        return this.userArray[i];
    }

    public void set(int i, int n) {
        this.userArray[i] = n;
    }

    public void pushback(int n) {
        if(this.size == this.capacity) {
            resize();
        }
        this.userArray[this.size] = n;
        this.size += 1;
    }

    public int popback() {
        if(this.size > 0){
            this.size -= 1;
        }
        return this.userArray[this.size];
    }

    private void resize() {
        this.capacity *= 2;
        int[] newArray = new int[this.capacity];
        for(int i = 0; i < this.userArray.length; i++){
            newArray[i] = this.userArray[i];
        }
        this.userArray = newArray;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
