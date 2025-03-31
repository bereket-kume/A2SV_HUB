# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(s, idx, current, target):
            if current > target:
                return False

            if idx == len(s):
                return current == target

            for i in range(idx, len(s)):
                num = int(s[idx:i+1])
                if backtrack(s, i + 1, current + num, target):
                    return True
            return False

        result = 0
        for i in range(1, n+1):
            val = str(i * i)
            if backtrack(val, 0, 0, i):
                result += i*i

        return result