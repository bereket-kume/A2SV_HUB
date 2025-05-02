# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = [(enq, pro, idx) for idx, (enq, pro) in enumerate(tasks)]
        tasks.sort()
        heap = []
        i = 0
        ans = []
        time = 0
        while i < n or heap:
            while i < n and tasks[i][0] <= time:
                enq, pro, idx = tasks[i]
                heapq.heappush(heap, (pro, idx))
                i += 1
            if heap:
                pro, idx = heapq.heappop(heap)
                time += pro
                ans.append(idx)
            else:
                time = tasks[i][0]
        return ans