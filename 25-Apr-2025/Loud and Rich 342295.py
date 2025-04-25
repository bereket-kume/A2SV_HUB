# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        incoming = [0] * n

        for a, b in richer:
            graph[a].append(b)
            incoming[b] += 1

        que = deque([i for i in range(n) if incoming[i] == 0])
        ans = list(range(len(quiet)))

        while que:
            node = que.popleft()

            for nei in graph[node]:
                if quiet[ans[node]] < quiet[ans[nei]]:
                    ans[nei] = ans[node]
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    que.append(nei)
        return ans