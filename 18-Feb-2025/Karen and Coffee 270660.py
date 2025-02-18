# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k , q = map(int, input().split())

recipes = []
for _ in range(n):
    start, end = map(int, input().split())
    recipes.append([start, end])

queries = []
for _ in range(q):
    a, b = map(int, input().split())
    queries.append([a, b])


prefix = [0] * (200000 + 2)
for s, e in recipes:

    prefix[s] += 1
    if e +1 < len(prefix):
        prefix[e+1] -= 1

for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]

for i in range(len(prefix)):
    if prefix[i] >= k:
        prefix[i] = 1
    else:
        prefix[i] = 0

for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]

for start, end in queries:
    print(prefix[end] - (prefix[start-1] if start > 0 else 0))
