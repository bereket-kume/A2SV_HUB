# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, nodes):
            visited[node] = True
            nodes.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, nodes)
        
        visited = [False] * n
        complete_com = 0

        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i, nodes)
                edge_count = 0

                for node in nodes:
                    edge_count += len(graph[node])
                
                edge_count //= 2
                k = len(nodes)

                if edge_count == k * (k - 1)//2:
                    complete_com += 1
        return complete_com