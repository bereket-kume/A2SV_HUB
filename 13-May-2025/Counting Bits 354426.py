# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for num in range(n+1):
            count = 0
            for j in range(32):
                if num & (1 << j) != 0:
                    count += 1
            ans.append(count)
        return ans