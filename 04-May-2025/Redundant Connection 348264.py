# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

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
                self.parent[r_y] = r_x
                self.rank[r_x] += 1
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)

        for start, end in edges:
            if uf.find(start) == uf.find(end):
                return [start, end]
            else:
                uf.union(start, end)