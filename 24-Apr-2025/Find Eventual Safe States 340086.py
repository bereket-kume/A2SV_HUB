# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj_list = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj_list[node].append(i)
                incoming[i] += 1
        
        que = deque()
        for node, val in enumerate(incoming):
            if val == 0:
                que.append(node)
        safe = [False] * n
        
        while que:
            node = que.popleft()
            safe[node] = True

            for nei in adj_list[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    que.append(nei)
    
        return [node for node, is_safe in enumerate(safe) if is_safe == True]