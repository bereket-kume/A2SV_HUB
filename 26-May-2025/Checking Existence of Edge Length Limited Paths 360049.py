# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]* n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[py] > self.rank[px]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        idx_queries = sorted([(i, *q) for i , q in enumerate(queries)], key=lambda x: x[3])

        uf = UnionFind(n)
        answer = [False]* len(queries)
        i = 0
        for idx, x, y, z in idx_queries:
            while i < len(edgeList) and edgeList[i][2] < z:
                a, b, _ = edgeList[i]
                uf.union(a, b)
                i += 1
            
            if uf.find(x) == uf.find(y):
                answer[idx] = True

        return answer