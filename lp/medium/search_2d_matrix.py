class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search row
        a, b = 0, len(matrix) - 1

        x = -1

        while a <= b:
            m = (a + b) // 2
            print(m)

            if matrix[m][0] <= target <= matrix[m][-1]:
                x = m
                break
            elif matrix[m][-1] <= target:
                a = m + 1
            else:
                b = m - 1

        if x == -1:
            return False
        
        print(x)
        
        l, r = 0, len(matrix[x]) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[x][m] == target:
                return True
            if matrix[x][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False