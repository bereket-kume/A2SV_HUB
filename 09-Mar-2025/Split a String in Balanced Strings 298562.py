# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_r=count_l=0
        ans=0

        for i in s:
            if i == 'R':
                count_r += 1
            else:
                count_l += 1
            
            if count_r == count_l:
                ans += 1
                count_l = 0
                count_r = 0
        return ans