# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        op = 0
        count = 0

        for char in s:
            if char == '1':
                count += 1
            else:
                op += count
        return op