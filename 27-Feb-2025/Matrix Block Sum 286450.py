# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        prefix = [[0] * (col+1) for _ in range(row+1)]
        

        for i in range(1, row+1):
            for j in range(1, col+1):

                val = (
                    mat[i-1][j-1] +
                    prefix[i-1][j] + 
                    prefix[i][j-1] -
                    prefix[i-1][j-1]
                )
                prefix[i][j] = val
        ans = [[0]* col for i in range(row)]
        for i in range(row):
            for j in range(col):
                r1 = max(0, i - k)
                c1 = max(0, j- k)
                r2 = min(row-1, i + k)
                c2 = min(col-1, j + k)
                ans[i][j] = (
                    prefix[r2 + 1][c2 + 1] -
                    prefix[r1][c2 + 1] -
                    prefix[r2 + 1][c1] +
                    prefix[r1][c1]
                )
        return ans