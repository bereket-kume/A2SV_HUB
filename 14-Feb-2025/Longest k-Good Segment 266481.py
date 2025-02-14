# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter

n, k = map(int, input().split())

nums = list(map(int, input().split()))

left, right = 0, 0

count_nums=Counter()
diff = 0
a=b=0

while right < n:
    count_nums[nums[right]] += 1

    while len(count_nums) > k:
        count_nums[nums[left]] -= 1
        if count_nums[nums[left]] == 0:
            del count_nums[nums[left]]
        left += 1

    if right - left + 1 > diff:
        a, b = left, right
        diff = right - left + 1

    right += 1

print(a+1, b+1)