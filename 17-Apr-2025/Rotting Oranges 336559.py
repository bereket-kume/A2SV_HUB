# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        n, m = len(grid), len(grid[0])
        time = 0
        d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    que.append([i, j, 0])

        while que:
            r, c, t = que.popleft()
            time = max(time, t)

            for x, y in d:
                nr, nc = r + x, y + c
                if 0 <= nr  < n and 0 <= nc < m:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        que.append([nr, nc, t + 1])
        for row in grid:
            if 1 in row:
                return -1
        return time