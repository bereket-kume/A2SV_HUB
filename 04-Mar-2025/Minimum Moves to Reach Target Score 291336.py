# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        if target == 1:
            return 0

        while maxDoubles and target > 1:
            if target % 2 == 0:
                if  maxDoubles > 0:
                    target = target // 2
                    maxDoubles -= 1
                else:
                    target -= 1
            else:
                target -= 1
            count += 1
        count += target - 1
        return count
            
        