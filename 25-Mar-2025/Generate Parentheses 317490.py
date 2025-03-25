# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(op, cl):
            if op == n and cl == n:
                ans.append("".join(stack))
                return
            if op < n:
                stack.append('(')
                backtrack(op + 1, cl)
                stack.pop()
            if cl < op:
                stack.append(')')
                backtrack(op, cl + 1)
                stack.pop()
        backtrack(0, 0)
        return ans