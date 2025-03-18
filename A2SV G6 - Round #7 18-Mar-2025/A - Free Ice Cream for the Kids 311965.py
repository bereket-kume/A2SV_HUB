# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

n, x = map(int, input().split())
count = 0
val = x
for _ in range(n):
    op = input()
    op = op.split()
   
    if op[0] == '+':
        val += int(op[1])
    else:
        if val >= int(op[1]):
            val -= int(op[1])
        else:
            count += 1
print(val, count)