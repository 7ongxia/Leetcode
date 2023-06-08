class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row_index = 0

        # Base Case
        if rows == 1 and cols == 1:
            if target == matrix[0][0]:
                return True
            else:
                return False

        # find row first using binary search
        r_s, r_m, r_e = 0, (rows - 1) // 2, rows - 1
        while r_s < r_e:
            if (r_s + 1) == r_e:
                row_index = r_e if matrix[r_e][0] <= target else r_s
                break
            if matrix[r_m][0] == target:
                return True
            elif matrix[r_m][0] > target:
                r_e = r_m
            else:
                r_s = r_m
            r_m = ((r_s + r_e) // 2)

        # find col using binary search
        c_s, c_m, c_e = 0, (cols - 1) // 2, cols - 1
        while c_s <= c_e:
            if matrix[row_index][c_m] == target:
                return True
            elif matrix[row_index][c_m] > target:
                c_e = c_m - 1
            else:
                c_s = c_m + 1
            c_m = ((c_s + c_e) // 2)
        else:
            return False
