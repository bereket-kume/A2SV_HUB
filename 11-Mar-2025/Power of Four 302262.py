# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(n, x=0, val=1):
            if val > n:
                return False
            if val == n:
                return True
            return helper(n, x + 1, val*4)

        return helper(n)