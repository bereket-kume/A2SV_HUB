# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
nums = list(map(int, input().split()))

sufix_sum = [0] * (n + 1)

for i in range(n-1, -1, -1):
    sufix_sum[i] = sufix_sum[i+1] + nums[i]
cost = sufix_sum[0]
num = sorted(sufix_sum[1:-1], reverse=True)
cost += sum(num[:k-1])
print(cost)