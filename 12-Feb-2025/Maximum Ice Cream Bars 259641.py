# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        count = [0] * (max_val +1)

        for cost in costs:
            count[cost] += 1

        t=0
        for idx, val in enumerate(count):
            for i in range(val):
                costs[t] = idx
                t += 1
        
        total = 0
        c = 0
        for cost in costs:
            if total + cost <= coins:
                total += cost
                c += 1
            else:
                break
        return c