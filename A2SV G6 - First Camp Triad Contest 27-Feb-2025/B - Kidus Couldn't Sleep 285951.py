# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n, k = map(int, input().split())

a = list(map(int, input().split()))


d = n - k + 1

current = sum(a[:k])

total = current

for i in range(k, n):
    current += a[i] - a[i-k]
    total += current

print(total/d)