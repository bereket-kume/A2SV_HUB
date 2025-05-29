# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self,n):
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        accIdx = {}

        for idx, a in enumerate(accounts):
            for em in a[1:]:
                if em in accIdx:
                    uf.union(accIdx[em], idx)
                else:
                    accIdx[em] = idx
        
        group = defaultdict(list)

        for em, idx in accIdx.items():
            leader = uf.find(idx)
            group[leader].append(em)
        ans = []

        for idx, em in group.items():
            name = accounts[idx][0]
            ans.append([name] + sorted(group[idx]))

        return ans