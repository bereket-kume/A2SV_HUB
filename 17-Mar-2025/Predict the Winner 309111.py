# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(l, r):
            if l == r:
                return nums[l]
            
            left = nums[l] - dfs(l + 1, r)
            right = nums[r] - dfs(l, r - 1)
            
            return max(left, right)

        return dfs(0, len(nums) - 1) >= 0
