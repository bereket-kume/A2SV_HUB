# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        d = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def is_border(i, j):
            return i == 0 or i == rows - 1 or j == 0 or j == cols - 1

        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
                board[i][j] = '.'
                for u, v in d:
                    dfs(i + u, j + v)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and is_border(i, j):
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'