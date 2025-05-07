# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
    

n, m = map(int, input().split())
graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a-1, b-1, c))
graph.sort(key=lambda x : x[2])
uf = UnionFind(n)
ans = 0
for u, v, w in graph:
    if uf.find(u) != uf.find(v):
        ans += w
        uf.union(u, v)
print(ans)