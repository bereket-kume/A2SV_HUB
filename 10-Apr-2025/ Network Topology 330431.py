# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]


def toplogy(n, m, edges):
    deger = [0] * (n + 1)

    for u, v in edges:
        deger[u] += 1
        deger[v] += 1

    deger_count = defaultdict(int)

    for i in range(1, n+1):
        deger_count[deger[i]] += 1

    if m == n - 1:
        if deger_count[1] == 2 and deger_count[2] == n - 2:
            return "bus topology"
        elif deger_count[1] == n - 1:
            return "star topology"
    elif m == n:
        if deger_count[2] == n:
            return "ring topology"
    return "unknown topology"

print(toplogy(n, m, edges))