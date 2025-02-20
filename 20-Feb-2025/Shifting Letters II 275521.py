# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        ans = [0] *n

        for start, end, dirc in shifts:
            if dirc ==  1:
                ans[start] += 1
                if end + 1 < n:
                    ans[end+1] -= 1
            else:
                ans[start] -= 1
                if end + 1 < n:
                    ans[end + 1] += 1
        
        for i in range(1, n):
            ans[i] += ans[i-1]

        result = []
        for i in range(len(s)):
            val = (ord(s[i]) - ord('a') + ans[i]) % 26
         
            result.append(chr(val+ord('a')))
           

        return "".join(result)
