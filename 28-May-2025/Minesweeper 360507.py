# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        di = [
            (1, 0), (0, 1), (-1, 0),
             (0, -1), (1, 1), (-1,-1),
            (-1, 1), (1, -1)
            ]
        
        def dfs(x, y):
            if board[x][y] != 'E':
                return 

            mine_count = 0
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == 'M':
                        mine_count += 1
            
            if mine_count > 0:
                board[x][y] = str(mine_count)
            else:
                board[x][y] = 'B'
                for dx, dy in di:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        dfs(nx, ny)
        dfs(r, c)
        return board
       