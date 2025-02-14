# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        max_len = 0
        current_cost = 0

        for r in range(len(s)):
            current_cost += abs(ord(s[r]) - ord(t[r]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            max_len = max(max_len, r-l + 1)

        return max_len
