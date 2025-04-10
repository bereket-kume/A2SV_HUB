# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, j in enumerate(manager):
            if j != -1:
                graph[j].append(i)

        def dfs(m_id):
            max_time = 0
            for nei in graph[m_id]:
                max_time = max(max_time, dfs(nei)+informTime[m_id])
            return max_time
        return dfs(headID)