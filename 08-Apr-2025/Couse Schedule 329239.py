# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0] * numCourses
        def dfs(node):
            if color[node] == 1:
                return False

            if color[node] == 2:
                return True
                
            color[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            color[node] = 2
            return True
    
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True