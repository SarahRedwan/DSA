class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True

        # check first col
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        # mark zeros in first row/col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set zeros based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # fix first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # fix first col
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0