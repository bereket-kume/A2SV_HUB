# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    found = dfs(i, visited)
                    if found:
                        return True
            return False

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        return dfs(source, visited)