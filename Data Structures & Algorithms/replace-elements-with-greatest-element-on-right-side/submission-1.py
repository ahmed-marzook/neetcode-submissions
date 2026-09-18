class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        print(length)
        for i in range(len(arr)):
            j = i + 1
            great = 0
            while(j < len(arr)):
                great = max(great, arr[j]);
                j += 1;
            arr[i] = great;
        arr[len(arr) - 1] = -1
        return arr;
