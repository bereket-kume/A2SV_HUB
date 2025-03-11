# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(k):
            if k == 0 or k == 1:
                return 1

            return k * factorial(k - 1)
        
        val = factorial(n)
        zero_count = 0

        while True:
            if val % 10 == 0:
                zero_count += 1
                val //=10
            else:
                break
        return zero_count