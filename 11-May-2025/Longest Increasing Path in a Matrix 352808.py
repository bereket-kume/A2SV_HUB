# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirc = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        @cache
        def dfs(i, j):
            res = 1
            for dx, dy in dirc:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[i][j] < matrix[nx][ny]:
                    res = max(res, 1+dfs(nx, ny))
            return res

        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))
        return ans