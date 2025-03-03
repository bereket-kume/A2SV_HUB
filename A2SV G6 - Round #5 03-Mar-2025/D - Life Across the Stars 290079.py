# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

n = int(input())
event = []

for _ in range(n):
    b, d = map(int, input().split())
    event.append((b, 1))
    event.append((d, -1))

event.sort(key=lambda x: (x[0], x[1]))

maxalive = 0
best_year = 0
current = 0


for year, change in event:
    current += change
    if current > maxalive:
        maxalive = current
        best_year = year

print(best_year, maxalive)