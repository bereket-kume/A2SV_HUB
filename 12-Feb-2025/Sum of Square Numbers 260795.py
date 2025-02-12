# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        print(right)
        currentSum = 0
        while left <= right:
            currentSum = left * left + right*right
            if currentSum == c:
                return True

            if currentSum < c:
                left += 1
            elif currentSum > c:
                right -= 1
        return False