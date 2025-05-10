# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px
        
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            if s1 == s2:
                return True
            diff = [(a, b) for a, b in zip(s1, s2) if a != b]

            return len(diff) == 2 and diff[0] == diff[1][::-1]
        
        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)
        return len(set(uf.find(i) for i in range(n)))