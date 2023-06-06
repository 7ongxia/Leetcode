class Solution:
    def setZeroColumn(self, index: int) -> None:
        for i in range(len(self.matrix)):
            self.matrix[i][index] = 0

    def setZeroRow(self, index: int) -> None:
        for i in range(len(self.matrix[index])):
            self.matrix[index][i] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        zero_rows = set()
        zero_cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for row in zero_rows:
            self.setZeroRow(row)
        for col in zero_cols:
            self.setZeroColumn(col)
