# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal_triangle(n, row=0, triangle=[]):
            if row == n:
                return triangle
            current_row = [1]
            if row > 0:
                prev_row = triangle[row - 1]
                for i in range(1, row):
                    current_row.append(prev_row[i] + prev_row[i - 1])
                current_row.append(1)
            triangle.append(current_row)
            return pascal_triangle(n, row + 1, triangle)
        ans = pascal_triangle(rowIndex+1)
        return ans[rowIndex]