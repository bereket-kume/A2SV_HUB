# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            if start == len(nums):
                ans.append(path[:])
                return

            
            backtrack(start + 1, path)
            path.append(nums[start])
            backtrack(start + 1, path)
            path.pop()
        ans = [] 
        backtrack(0, [])
        return ans

