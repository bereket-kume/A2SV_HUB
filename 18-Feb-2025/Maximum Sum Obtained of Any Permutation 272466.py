# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        prefix = [0] * (n+1)

        for start, end in requests:
            prefix[start] += 1
            if end + 1 <= n:
                prefix[end + 1] -= 1

        for i in range(1, n+1):
            prefix[i] += prefix[i-1]

        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0

        for pre, num in zip(prefix, nums):
            ans += pre * num

        return ans % (10**9 + 7)