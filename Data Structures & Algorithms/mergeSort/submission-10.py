# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        size = len(pairs)
        if size <= 1:
            return pairs
        m = size // 2
        leftArray = pairs[:m]
        rightArray = pairs[m:]
        self.mergeSort(leftArray)
        self.mergeSort(rightArray)

        self.merge(leftArray, rightArray, pairs)

        return pairs

    def merge(self, leftArray: List[Pair], rightArray: List[Pair], array: List[Pair]):
        l = 0
        r = 0
        i = 0

        while l < len(leftArray) and r < len(rightArray):
            if leftArray[l].key <= rightArray[r].key:
                array[i] = leftArray[l]
                l += 1
            else:
                array[i] = rightArray[r]
                r += 1
            i += 1
        
        while l < len(leftArray):
            array[i] = leftArray[l]
            l += 1
            i += 1

        while r < len(rightArray):
            array[i] = rightArray[r]
            r += 1
            i += 1
