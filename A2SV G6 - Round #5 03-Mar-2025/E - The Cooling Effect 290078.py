# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

t = int(input())

for _ in range(t):
    while True:
        line = input().strip()
        if line:
            break
    
    n, k = map(int, line.split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    left = [float('inf')] * (n + 2)
    right = [float('inf')] * (n + 2)

    for i in range(k):
        pos = a[i]
        temp = b[i]
        left[pos] = min(left[pos], temp)
    
    for i in range(2, n + 1):
        left[i] = min(left[i], left[i-1] + 1)
    
    for i in range(k):
        pos = a[i]
        temp = b[i]
        right[pos] = min(right[pos], temp)

    for i in range(n-1, 0, -1):
        right[i] = min(right[i], right[i+1]+1)

    result = []

    for i in range(1, n+1):
        result.append(min(left[i], right[i]))
    print(*result)