# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def dfs(node, c):
            colors[node] = c
            for x in graph[node]:
                if colors[x] == -1:
                    if not dfs(x, 1-c):
                        return False 
                elif colors[x] == c:
                    return False
            return True

        for node in range(n):
            if colors[node] == -1:
                if not dfs(node, 0):
                    return False
        return True