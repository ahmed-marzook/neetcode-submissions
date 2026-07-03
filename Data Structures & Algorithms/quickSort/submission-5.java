// Definition for a pair.
// class Pair {
//     int key;
//     String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> quickSort(List<Pair> pairs) {
        if(pairs.size() <= 1) {
            return pairs;
        } else {
            return quickSortHelper(pairs, 0, pairs.size() - 1);
        }
    }

    public List<Pair> quickSortHelper(List<Pair> array, int start, int end) {
        if(start >= end) {
            return array;
        }

        int pivot = partition(array, start, end);
        quickSortHelper(array,start, pivot - 1);
        quickSortHelper(array,pivot + 1, end);
        return array;
    }

    public int partition(List<Pair> array, int start, int end) {
        int pivot = array.get(end).key;
        int i = start - 1;

        for(int j = start; j < end; j++){
            if(array.get(j).key < pivot) {
                i++;
                Pair temp = array.get(i);
                array.set(i, array.get(j));
                array.set(j, temp);
            }
        }
        i++;
        Pair temp = array.get(i);
        array.set(i, array.get(end));
        array.set(end, temp);
        return i;
    }
}
