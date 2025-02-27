# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    a = list(map(int, input().split()))

    a.sort(reverse=True)
    current_sum = 0
    count = 0

    for i in range(n):
        current_sum += a[i]
        if current_sum / (i+1) < x:
            break
        count += 1
    print(count)
