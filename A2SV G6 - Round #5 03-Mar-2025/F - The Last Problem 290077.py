# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

prefix = [0]

for i in range(n):
    prefix.append(prefix[-1]+a[i]*b[i])


ans = prefix[-1]

for i in range(n):

    #odd
    profit = a[i] * b[i]

    l = i - 1
    r = i + 1

    while l >= 0 and r < n:
        profit += a[r] * b[l]
        profit += a[l] * b[r]

        ans = max(ans, profit + prefix[l] + (prefix[-1] - prefix[r + 1]))
        l -= 1
        r += 1

    #even 
    profit = 0

    l = i
    r = i + 1

    while l >= 0 and r < n:
        profit += a[r] * b[l]
        profit += a[l] * b[r]

        ans = max(ans, profit + prefix[l] + (prefix[-1] - prefix[r + 1]))
        l -= 1
        r += 1
print(ans)