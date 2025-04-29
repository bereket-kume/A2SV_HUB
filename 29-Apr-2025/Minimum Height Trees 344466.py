# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        print(graph)
        leaves = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        rem_node = n

        while rem_node > 2:
            l = len(leaves)
            rem_node -= l

            for _ in range(l):
                leaf = leaves.popleft()
                nei  = graph[leaf].pop()
                graph[nei].remove(leaf)

                if len(graph[nei]) == 1:
                    leaves.append(nei)

        return list(leaves)
