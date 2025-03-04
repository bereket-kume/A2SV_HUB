# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        costs.sort(key=lambda x: x[1] - x[0])
        ans = 0
        count = 0  

        for i in range(n):
            if count < n//2:
                ans += costs[i][1]
            else:
                ans += costs[i][0]
            count += 1
        return ans