# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle=list(i for i in range(1, n+1))
        start_index=0

        def helper(circle, start_index, k):
            if len(circle) == 1:
                return circle

            index = (start_index + k - 1) % len(circle)
            circle.pop(index)
            start_index=index
            helper(circle, start_index, k)
        helper(circle, start_index, k)
        
        return circle[0]
