# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        ispre = [[False] * numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            q = deque([i])

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if not ispre[i][nei]:
                        ispre[i][nei] = True
                        q.append(nei)
        ans = []
        for a, b in queries:
            ans.append(ispre[a][b])
        return ans