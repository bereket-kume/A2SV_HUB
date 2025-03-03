# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count('1')
        zero_count = s.count('0')

        ans = '1' * (one_count - 1) + '0' * (zero_count) + '1'

        return ans