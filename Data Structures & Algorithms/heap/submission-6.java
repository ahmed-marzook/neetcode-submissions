class MinHeap {
    List<Integer> heap;
    public MinHeap() {
        this.heap = new ArrayList<>(List.of(0));
    }

    public void push(int val) {
        this.heap.add(val);

        int i = this.heap.size() - 1;

        while(i > 1 && this.heap.get(i) < this.heap.get(i / 2)) {
            int tmp = this.heap.get(i);
            this.heap.set(i, this.heap.get(i / 2));
            this.heap.set(i / 2, tmp);
            i = i / 2;
        }
        System.out.println(this.heap.toString());
    }

    public Integer pop() {
        if(this.heap.size() == 1) {
            return -1;
        }
        if(this.heap.size() == 2) {
            return this.heap.remove(1);
        }

        int res = this.heap.get(1);

        this.heap.set(1, this.heap.remove(this.heap.size() - 1));
        int i = 1;

        while(2 * i < heap.size()) {
            if(2 * i + 1 < heap.size() &&
            heap.get(2 * i + 1) < heap.get(2 * i) &&
            heap.get(i) > heap.get(2 * i + 1)) {
                int tmp = heap.get(i);
                heap.set(i, heap.get(2 * i + 1));
                heap.set(2 * i + 1, tmp);
                i = 2 * i + 1;
            } else if (heap.get(i) > heap.get(2 * i)) {
                int tmp = heap.get(i);
                heap.set(i, heap.get(2 * i));
                heap.set(2 * i, tmp);
                i = 2 * i;
            } else {
                break;
            }
        }
        return res;
    }

    public Integer top() {
        if(this.heap.size() == 1) {
            return -1;
        }
        return this.heap.get(1);
    }

    public void heapify(List<Integer> nums) {
        this.heap = new ArrayList<>();
        this.heap.add(0);  // Placeholder for 0th index
        this.heap.addAll(nums);

        int curr = (this.heap.size() - 1) / 2;

        while(curr > 0) {
            int i = curr;
            while(2 * i < heap.size()) {
                if(2 * i + 1 < heap.size() &&
                heap.get(2 * i + 1) < heap.get(2 * i) &&
                heap.get(i) > heap.get(2 * i + 1)) {
                    int tmp = heap.get(i);
                    heap.set(i, heap.get(2 * i + 1));
                    heap.set(2 * i + 1, tmp);
                    i = 2 * i + 1;
                } else if (heap.get(i) > heap.get(2 * i)) {
                    int tmp = heap.get(i);
                    heap.set(i, heap.get(2 * i));
                    heap.set(2 * i, tmp);
                    i = 2 * i;
                } else {
                    break;
                }
            }
            curr--;
        }
    }
}
