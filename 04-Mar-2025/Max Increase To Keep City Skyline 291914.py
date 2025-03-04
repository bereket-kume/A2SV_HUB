# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = []
        
        max_col = []

        for row in grid:
            max_val = max(row)
            max_row.append(max_val)

        for i in range(n):
            max_val = 0
            for j in range(n):
                max_val = max(max_val, grid[j][i])
            max_col.append(max_val)

        ans=0
        for i in range(n):
            for j in range(n):
                ans += (min(max_row[i], max_col[j]) - grid[i][j])
                
        return ans





