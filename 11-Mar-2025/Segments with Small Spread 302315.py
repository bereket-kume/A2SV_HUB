# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))

in_queue = deque()
de_queue = deque()

left = 0
count = 0

for i in range(n):
    while in_queue and in_queue[-1] > nums[i]:
        in_queue.pop()
    in_queue.append(nums[i])

    while de_queue and de_queue[-1] < nums[i]:
        de_queue.pop()
    de_queue.append(nums[i])

    while de_queue[0] - in_queue[0] > k:
        if de_queue[0] == nums[left]:
            de_queue.popleft()
        if in_queue[0] == nums[left]:
            in_queue.popleft()
        left += 1

    count += (i - left + 1)

print(count)
