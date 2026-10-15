class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tempArray = nums1[:m]
        for num in nums2:
            tempArray.append(num)
        
        tempArray.sort()
        for i in range(len(nums1)):
            nums1[i] = tempArray[i]