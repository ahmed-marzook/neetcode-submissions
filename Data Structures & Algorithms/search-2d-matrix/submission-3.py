class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1

        while L <= R:
            mid = (L + R) // 2
            if target > matrix[mid][-1]:
                L = mid + 1
            elif target < matrix[mid][0]:
                R = mid - 1
            else:
                break
        else:
            return False

        L, R = 0, len(matrix[mid]) - 1

        while L <= R:
            innermid = (L + R) // 2
            if target > matrix[mid][innermid]:
                L = innermid + 1
            elif target < matrix[mid][innermid]:
                R = innermid - 1
            else:
                return True

        return False