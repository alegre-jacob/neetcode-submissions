class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        y = len(matrix)
        x = len(matrix[0])
        r = x * y - 1
        while l <= r:
            m = (r + l) // 2
            my = m // x
            mx = m % x
            if matrix[my][mx] < target:
                l = m + 1
            elif matrix[my][mx] > target:
                r = m  - 1
            else:
                return True
        return False

