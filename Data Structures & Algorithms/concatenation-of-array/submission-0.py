class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        print(length)
        for i in range(length):
            ans.insert(i, nums[i])
            ans.insert(i + length, nums[i])
        return ans