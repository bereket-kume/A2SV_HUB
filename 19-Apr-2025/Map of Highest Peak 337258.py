# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que = deque()
        n, m = len(isWater), len(isWater[0])
        height = [[-1 for i in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    que.append([i, j])
                    height[i][j] = 0
        
        d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        def inbound(x, y):
            return 0 <= x < n and 0 <= y < m

        while que:
            i, j = que.popleft()
            for x, y in d:
                ni, nj = x + i, y + j
                if inbound(ni, nj) and height[ni][nj] == -1:
                    height[ni][nj] = height[i][j] + 1
                    que.append([ni, nj])
        return height