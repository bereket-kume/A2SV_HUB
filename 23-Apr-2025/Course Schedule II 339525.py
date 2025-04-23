# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [ 0 for i in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        que = deque()

        for node, indeg in enumerate(incoming):
            if indeg == 0:
                que.append(node)
        ans = []
        while que:
            node = que.popleft()
            ans.append(node)
            for nei in graph[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    que.append(nei)
        if len(ans)  != numCourses:
            return []

        return ans