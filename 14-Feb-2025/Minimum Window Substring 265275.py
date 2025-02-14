# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(first, second):
            for char in first:
                if  second[char] < first[char]:
                    return False
            return True
        
        left = 0
        count_t=Counter(t)
        window=defaultdict(int)
        diff=float('inf')
        a, b = 0, 0
        current_length = 0

        for right in range(len(s)):
            window[s[right]] += 1
            while left <= right and check(count_t, window):
                current_length = (right - left) + 1

                if current_length < diff:
                    a, b = left, right
                    diff = current_length
                window[s[left]] -= 1
                left += 1
            
        if diff == float('inf'):
            return ""

        return s[a:b+1]