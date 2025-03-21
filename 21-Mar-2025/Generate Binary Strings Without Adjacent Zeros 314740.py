# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        path = [0] * n

        def backtrack(start, path):
            if start == n:
                for i in range(1, len(path)):
                    if path[i-1] == 0 and path[i] == 0:
                        return
                else:
                    ans.append("".join(str(p) for p in path))
                    return
            
            path[start] = 0
            backtrack(start + 1, path)
            path[start] = 1
            backtrack(start + 1, path)
        backtrack(0, path)
        return ans