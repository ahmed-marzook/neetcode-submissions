class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        sortedPoints = self.quickSortHelper(points, 0, len(points) - 1)

        return sortedPoints[:k]
        
    
    def quickSortHelper(self, points: List[List[int]], s:int, e:int) -> List[List[int]]:
        if(e - s + 1 <= 1):
            return points
        
        pivot = points[e]
        left = s

        for i in range(s,e):
            if (points[i][0] ** 2 + points[i][1] ** 2) < pivot[0] ** 2 + pivot[1] ** 2:
                tmp = points[left]
                points[left] = points[i]
                points[i] = tmp
                left += 1
        
        points[e] = points[left]
        points[left] = pivot

        self.quickSortHelper(points, s , left - 1)
        self.quickSortHelper(points, left + 1, e)

        return points


