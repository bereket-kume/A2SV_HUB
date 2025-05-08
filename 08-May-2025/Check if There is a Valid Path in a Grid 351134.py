# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        direction = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }

        opp = {
            (0, -1): (0,1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }

        visited = [[False] * n for _ in range(m)]

        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in direction[grid[x][y]]:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if opp[(dx, dy)] in direction[grid[nx][ny]]:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
        return False