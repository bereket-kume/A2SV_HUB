# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        que = deque()
        d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        ans = [[-1 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    que.append((i, j))

        while que:
            x, y = que.popleft()

            for i, j in d:
                ni, nj = x + i, y + j
                if 0 <= ni < n and 0 <= nj < m and ans[ni][nj] == -1:
                    ans[ni][nj] = ans[x][y] + 1
                    que.append((ni, nj))
        return ans