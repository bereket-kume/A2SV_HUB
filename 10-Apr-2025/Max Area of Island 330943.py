# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 0

            area = 1
            d = [(0, -1), (-1, 0), (1, 0), (0, 1)]
            grid[row][col] = 0

            for x, y in d:
                area += dfs(row + x, col + y)
            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area