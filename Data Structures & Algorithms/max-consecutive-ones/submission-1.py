class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0;
        array = [];
        for n in nums:
            if(n == 1):
                count += 1
            else:
                array.append(count)
                count = 0
        array.append(count)
        return max(array)