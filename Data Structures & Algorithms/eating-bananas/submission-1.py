class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles)/h)  # lowest amount koko can eat
        r = max(piles) # absolute max
        res = r
        while l <= r:
            k = (l + r) // 2
            minHours = self.minHours(k,piles)
            if minHours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return int(res)

    def minHours(self, k: int, piles: List[int]) -> int:
        h = 0
        for p in piles:
            h += math.ceil(p / k)
        return h
        