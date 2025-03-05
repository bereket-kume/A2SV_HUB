# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = path.split('/')
        new_path = [i for i in new_path if len(i) > 0]

        stack = []

        for pa in new_path:
            if pa == '..':
                if stack:
                    stack.pop()
            else:
                if pa != '.':
                    stack.append(pa)
        print(stack)
        return "/"+"/".join(stack)