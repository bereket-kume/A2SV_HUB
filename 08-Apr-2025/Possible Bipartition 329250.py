# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        colors = [-1] * n

        def dfs(node, color):
            colors[node] = color

            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1-color):
                        return False
                elif colors[neighbor] == color:
                    return False
            return True
        
        for node in range(n):
            if colors[node] == -1:
                if not dfs(node, 0):
                    return False
        return True