# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=set()
        left=0
        max_len=0

        for right in range(len(s)):
            while s[right] in count:
                count.remove(s[left])
                left += 1
            count.add(s[right])
            max_len=max(max_len, right-left+1)
        return max_len

