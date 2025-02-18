# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash_m = Counter({0:1})

        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            if current_sum - goal in hash_m:
                count += hash_m[current_sum-goal]
            hash_m[current_sum] += 1
            
        return count

    