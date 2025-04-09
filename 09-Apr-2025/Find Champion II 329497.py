# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
        
        def dfs(node, visited):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited)
        
        champinons = []
        for i in range(n):
            visited = set()
            dfs(i, visited)
            if len(visited) == n - 1:
                champinons.append(i)
        
        return champinons[0] if len(champinons) == 1 else -1