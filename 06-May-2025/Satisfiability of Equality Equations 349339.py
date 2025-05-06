# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, eq):
        if eq[1] == '=':
            idx1 = (ord(eq[0]) - ord('a'))
            idx2 = (ord(eq[3]) - ord('a'))

            self.parent[self.find(idx1)] = self.find(idx2)
        

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)

        for eq in equations:
            uf.union(eq)
        
        for eq in equations:
            if eq[1] == '!':
                idx1 = (ord(eq[0]) - ord('a'))
                idx2 = (ord(eq[3]) - ord('a'))

                if uf.find(idx1) == uf.find(idx2):
                    return False
        return True
