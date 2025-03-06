# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        in_queue = deque()
        de_queue = deque()

        max_len = 0
        left = 0

        for i in range(len(nums)):
            while in_queue and in_queue[-1] > nums[i]:
                in_queue.pop()
            in_queue.append(nums[i])

            while de_queue and de_queue[-1] < nums[i]:
                de_queue.pop()
            de_queue.append(nums[i])

            while de_queue[0] - in_queue[0] > limit:
                if de_queue[0] == nums[left]:
                    de_queue.popleft()
                
                if in_queue[0] == nums[left]:
                    in_queue.popleft()
                left += 1
            max_len = max(max_len, i - left + 1)
        return max_len



