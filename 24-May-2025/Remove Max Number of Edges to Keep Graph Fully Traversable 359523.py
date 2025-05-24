# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.component = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[py] > self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[px] += 1
        self.component -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        removed = 0

        for t, y, z in edges:
            if t == 3:
                b = bob.union(y, z)
                a = alice.union(y, z)
                if not a and not b:
                    removed += 1

        for t, y, z in edges:
            if t == 1:
                if not alice.union(y, z):
                    removed += 1

        for t, y, z in edges:
            if t == 2:
                if not bob.union(y, z):
                    removed += 1
        
        if alice.component != 1 or bob.component != 1:
            return -1
        return removed