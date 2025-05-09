# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        r_x, r_y = self.find(x), self.find(y)

        if r_x < r_y:
            self.parent[r_y] = r_x
        else:
            self.parent[r_x] = r_y
        
        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)):
            c_1, c_2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            uf.union(c_1, c_2)

        ans = []

        for i in baseStr:
            ch = ord(i) - ord('a')
            ans.append(chr(uf.find(ch) + ord('a')))

        return "".join(ans)