# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    i, j = 0, 1
    ans = 0

    while i < n and j < n:
        if nums[i] > nums[j]:
            ans += 1
            i += 2
            j += 2
        else:
            i += 1
            j += 1
    print(ans)
