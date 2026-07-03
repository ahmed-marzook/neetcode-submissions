# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        length = len(pairs)
        output = []
        if length <=  1: return pairs

        middle = length // 2

        left_array = pairs[:middle]
        right_array = pairs[middle:]

        self.mergeSort(left_array)
        self.mergeSort(right_array)

        self.merge(left_array, right_array, pairs)
        
        return pairs
    
    def merge(self, left_array: list[Pair], right_array: list[Pair], array: list[Pair]):
        r = 0
        l = 0
        a = 0

        while l < len(left_array) and r < len(right_array):
            if left_array[l].key <= right_array[r].key:
                array[a] = left_array[l]
                l += 1
            else:
                array[a] = right_array[r]
                r += 1
            a +=1
        
        while l < len(left_array):
            array[a] = left_array[l]
            l += 1
            a += 1

        while r < len(right_array):
            array[a] = right_array[r]
            r += 1
            a += 1
