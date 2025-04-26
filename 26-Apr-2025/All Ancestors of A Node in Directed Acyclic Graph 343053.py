# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ans = [set() for _ in range(n)]
        incoming = [0] * n
        for fr, to in edges:
            graph[fr].append(to)
            incoming[to] += 1

        que = deque(node for node, val in enumerate(incoming) if val == 0)

        while que:
            node = que.popleft()
            for nei in graph[node]:
                ans[nei].add(node)
                ans[nei].update(ans[node])
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    que.append(nei)
        
        return [sorted(list(val)) for val in ans]