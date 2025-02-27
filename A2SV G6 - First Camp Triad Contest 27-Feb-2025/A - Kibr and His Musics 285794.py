# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

t, m = map(int, input().split())
prefix = []

for i in range(t):
    x, y = map(int, input().split())

    prefix.append(x*y)
    if i > 0:
        prefix[i] += prefix[i-1]

mo = list(map(int, input().split()))
i=0
for j in range(m):
    while prefix[i] < mo[j]:
        i += 1
    print(i+1)
