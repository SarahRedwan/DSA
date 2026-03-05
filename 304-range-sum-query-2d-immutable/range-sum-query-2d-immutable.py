class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return

        row=len(matrix)
        column=len(matrix[0])
        self.pre=[[0 for _ in range(column+1)] for rows in range(row+1)]

        for i in range(row):
            for j in range(column):
                self.pre[i+1][j+1]=matrix[i][j]+self.pre[i+1][j]+self.pre[i][j+1]-self.pre[i][j]
    def sumRegion(self, row1, col1, row2, col2):
        box=self.pre[row2+1][col2+1]
        upbox=self.pre[row1][col2+1]
        leftbox=self.pre[row2+1][col1]
        overlap=self.pre[row1][col1]

        return box-upbox-leftbox+overlap