# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1 = []
        stack_2 = []

        for i in s:
            if stack_1 and i == '#':
                stack_1.pop()
            else:
                if i != '#':
                    stack_1.append(i)
        
        for i in t:
            if stack_2 and i == '#':
                stack_2.pop()
            else:
                if i != '#':
                    stack_2.append(i)
        
        return stack_1 == stack_2

        