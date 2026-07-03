# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        else:
            return self.quick_sort_helper(pairs, 0, len(pairs) -1)
    
    def quick_sort_helper(self, array: List[Pair], start: int, end: 0) -> List[Pair]:

        if start >= end:
            return
        
        pivot = self.partition(array,start,end)
        self.quick_sort_helper(array, start, pivot - 1)
        self.quick_sort_helper(array, pivot + 1, end)
        return array

    def partition(self,array,start,end) -> int:
        pivot = array[end].key
        index = start

        for j in range(start, end):
            if array[j].key < pivot:
                temp = array[index]
                array[index] = array[j]
                array[j] = temp
                index +=1
        temp = array[index]
        array[index] = array[end]
        array[end] = temp
        return index