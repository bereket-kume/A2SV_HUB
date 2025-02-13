# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

test_case = int(input())

for _ in range(test_case):
    n=int(input())
    nums = list(map(int, input().split()))
    max_sum = 0
    val = nums[0]
    

    for i in range(1, n):
        if (val < 0 and nums[i] > 0) or (val > 0 and nums[i] < 0):
            max_sum += val
            val = nums[i]
        else:
            val = max(val, nums[i])


    max_sum += val
    print(max_sum)
