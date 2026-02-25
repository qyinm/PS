class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # find row
        lo, hi = 0, m - 1
        row = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(matrix[mid][-1])
            if target < matrix[mid][0]:
                hi = mid - 1
            elif target > matrix[mid][-1]:
                lo = mid + 1
            else:
                row = mid
                break

        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False