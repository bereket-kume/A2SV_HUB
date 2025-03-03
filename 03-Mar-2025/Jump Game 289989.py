# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        prev_jump = nums[0]
        

        for i in range(1, n):
            print(i, prev_jump)
            if prev_jump < i:
                return False
            prev_jump = max(prev_jump, i + nums[i])
        return True