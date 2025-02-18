# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = Counter({0: 1})
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            rem = 0
            rem = prefix % k
            if rem in count:
                result += count[rem]
            count[rem] += 1
        return result
        