// Definition for a pair.
// class Pair {
//     public int key;
//     public String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> mergeSort(List<Pair> pairs) {
        int size = pairs.size();
        if(pairs.size() <= 1) {
            return pairs;
        }
        int center = size / 2;
        List<Pair> leftArray = new ArrayList<>(pairs.subList(0, center));
        List<Pair> rightArray = new ArrayList<>(pairs.subList(center, size));
        mergeSort(leftArray);
        mergeSort(rightArray);
        mergeHelper(leftArray, rightArray, pairs);
        return pairs;
    }

    public void mergeHelper(List<Pair> leftArray,List<Pair> rightArray , List<Pair> array){
        int l = 0;
        int r = 0;
        int a = 0;

        while(l < leftArray.size() && r < rightArray.size()) {
            if(leftArray.get(l).key <= rightArray.get(r).key) {
                array.set(a, leftArray.get(l));
                l++;
            } else {
                array.set(a, rightArray.get(r));
                r++;
            }
            a++;
        }

        while(l < leftArray.size()) {
            array.set(a, leftArray.get(l));
            l++;
            a++;
        }

        while(r < rightArray.size()) {
            array.set(a, rightArray.get(r));
            r++;
            a++;
        }
    }
}
