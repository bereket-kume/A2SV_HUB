# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        def dfs(current, target, product, visited):
            if current == target:
                return product
            visited.add(current)

            for nei, val in graph[current]:
                if nei in visited:
                    continue
                result = dfs(nei, target, product * val, visited)
                if result != -1.0:
                    return result
            return -1.0
        result = []

        for start, end in queries:
            if start not in graph or end not in graph:
                result.append(-1.0)
            elif start == end:
                result.append(1.0)
            else:
                result.append(dfs(start, end, 1.0, set()))
        return result