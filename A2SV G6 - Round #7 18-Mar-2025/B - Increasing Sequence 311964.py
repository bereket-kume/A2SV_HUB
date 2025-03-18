# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    count = 1
    ans = []
    for i in range(n):
        if nums[i] == count:
            count += 1
            ans.append(count)
            count += 1 
        elif nums[i] < count:
            ans.append(count)
            count += 1
        elif nums[i] > count:
            ans.append(count)
            count += 1
    print(ans[-1])