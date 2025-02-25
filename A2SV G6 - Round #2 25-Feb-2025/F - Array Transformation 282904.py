# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter

n = int(input())

for _ in range(n):
    m = int(input())
    nums = list(map(int, input().split()))

    count = Counter(nums)
    min_val = float('inf')

    options = set(count.values())

    for c in options:
        deletion = 0
        for num, freq in count.items():
            if freq < c:
                deletion += freq
            else:
                deletion += freq - c  

        min_val = min(min_val, deletion)

    print(min_val)
