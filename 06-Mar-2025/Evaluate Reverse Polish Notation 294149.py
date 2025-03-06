# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {
            '+':lambda x, y: x + y,
            '-':lambda x, y: x-y, 
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
            }

        for token in tokens:
            if token in operator:
                x = stack.pop()
                y = stack.pop()
                stack.append(operator[token](y, x))
            else:
                stack.append(int(token))
        return stack[0]
