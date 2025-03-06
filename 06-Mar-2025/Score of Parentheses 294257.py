# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in s:
            if i == '(':
                stack.append(0)
            else:
                top = stack.pop()
                if top == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * top

        return stack[0]