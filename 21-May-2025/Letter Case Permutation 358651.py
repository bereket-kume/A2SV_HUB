# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        result = []

        def backtrack(index, path):
            if index == n:
                result.append(path)
                return
            
            if s[index].isdigit():
                backtrack(index + 1, path + s[index])
            else:
                backtrack(index + 1, path + s[index].lower())
                backtrack(index + 1, path + s[index].upper())
            
        backtrack(0, "")
        return result