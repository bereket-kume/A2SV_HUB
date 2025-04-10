# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        ans = [[]  for _ in range(n)]
        visit = [set()  for _ in range(n)]

        def dfs(node, parent):
            for nei in adj[node]:
                if parent not in visit[nei]:
                    visit[nei].add(parent)
                    ans[nei].append(parent)
                    dfs(nei, parent)
        for i in range(n):
            dfs(i, i)
        return ans
        