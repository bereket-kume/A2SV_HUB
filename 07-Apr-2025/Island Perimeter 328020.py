# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        count = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    if grid[i -1 ][j] == 0 or i ==  0:
                        count += 1

                    if i == row - 1 or grid[i+1][j] == 0:
                        count += 1
                    if grid[i][j-1] == 0 or j == 0:
                        count += 1
                
                    if j == column - 1 or grid[i][j+1] == 0:
                        count += 1
        return count