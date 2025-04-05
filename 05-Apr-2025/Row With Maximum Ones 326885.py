# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        for i in range(len(mat)):
            if mat[i].count(1) > ans[1]:
                ans[0] = i
                ans[1] = mat[i].count(1)
        return ans