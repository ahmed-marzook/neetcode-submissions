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

    public List<Pair> quickSortHelper(List<Pair> pairs, int start, int end) {
        if(start >= end) {
            return pairs;
        };

        int pivot = partition(pairs, start, end);
        quickSortHelper(pairs, start, pivot - 1);
        quickSortHelper(pairs, pivot + 1, end);
        return pairs;
    }

    public int partition(List<Pair> pairs, int start, int end) {
        int pivot = pairs.get(end).key;
        int i = start -1;

        for(int j = start; j <= end; j++){
            if(pairs.get(j).key < pivot){
                i++;
                Pair temp = pairs.get(i);
                pairs.set(i, pairs.get(j));
                pairs.set(j, temp);
            }
        }
        i++;
        Pair temp = pairs.get(i);
        pairs.set(i, pairs.get(end));
        pairs.set(end, temp);
        return i;
    }
}
