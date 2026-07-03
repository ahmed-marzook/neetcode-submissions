class DynamicArray {
    
    private int capacity;
    private int size;
    private int[] array;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.array = new int[this.capacity];
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if(this.size + 1 > this.capacity) {
            resize();
        }
        this.array[this.size] = n;
        this.size++;
    }

    public int popback() {
        int value = this.array[this.size - 1];
        this.size--;
        return value;
    }

    private void resize() {
        this.capacity *= 2;
        int[] newArray = new int[this.capacity];

        for(int i = 0;i < this.size;i++){
            newArray[i] = this.array[i];
        }
        this.array = newArray;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
