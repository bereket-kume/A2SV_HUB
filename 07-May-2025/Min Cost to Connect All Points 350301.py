# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)

        if r_x != r_y:
            if self.rank[r_x] > self.rank[r_y]:
                self.parent[r_y] = r_x
            elif self.rank[r_y] > self.rank[r_x]:
                self.parent[r_x] = r_y
            else:
                self.parent[r_x] = r_y
                self.rank[r_y] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        cost = []

        for i in range(n):
            for j  in range(i + 1, n):
                val = (abs(points[i][0] -points[j][0])) + abs((points[i][1] - points[j][1]))
                cost.append( (i, j , val))

        cost.sort(key=lambda x: x[2])
        ans = 0

        for u, v, w in cost:
            if uf.find(u) != uf.find(v):
                ans += w
                uf.union(u, v)
        return ans