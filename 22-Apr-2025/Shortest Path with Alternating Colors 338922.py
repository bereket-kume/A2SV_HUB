# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dist in redEdges:
            red[src].append(dist)
        
        for src, dist in blueEdges:
            blue[src].append(dist)
        
        ans = [-1 for _ in range(n)]
        que = deque()
        que.append([0,0, None])
        visit = set()
        visit.add((0, None))


        while que:
            node, l, color = que.popleft()

            if ans[node] == -1:
                ans[node] = l

            if color != 'RED':
                for ni in red[node]:
                    if (ni, 'RED') not in visit:
                        visit.add((ni, 'RED'))
                        que.append([ni, l + 1, 'RED'])
            if color != 'BLUE':
                for ne in blue[node]:
                    if (ne, 'BLUE') not in visit:
                        visit.add((ne, 'BLUE'))
                        que.append([ne, l + 1, 'BLUE'])
        return ans
                