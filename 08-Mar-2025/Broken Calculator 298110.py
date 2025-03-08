# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0

        while startValue < target:
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
            count += 1
        count += startValue - target
        return count