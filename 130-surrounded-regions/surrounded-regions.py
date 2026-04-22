from collections import defaultdict
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return
            board[row][col] = 'S'   

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                dfs(new_row, new_col)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

