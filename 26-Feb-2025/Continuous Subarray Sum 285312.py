# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = {0:-1}
        current_sum = 0

        for idx, val in enumerate(nums):
            current_sum += val
            rem = current_sum % k

            if rem < 0:
                rem += k

            if rem in count and idx - count[rem] >= 2:
                return True

            if rem not in count:
                count[rem] = idx

        return False
            