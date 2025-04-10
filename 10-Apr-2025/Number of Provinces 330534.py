# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        prov = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                prov += 1
        return prov