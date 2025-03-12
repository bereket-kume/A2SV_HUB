# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = ['a']
        def helper(x, ans):
            if x == 1 or len(ans) > k:
                return ans
                
            new_ans = ans[:]
            for i in ans:
                next_val = chr((ord(i) - ord('a') + 1) % 26 + ord('a'))
                new_ans.append(next_val)

            return helper(x-1, new_ans)

        ans = helper(k, ans)
        return ans[k-1]