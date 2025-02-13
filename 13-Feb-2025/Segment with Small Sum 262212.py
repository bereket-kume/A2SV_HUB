# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = list(map(int, input().split()))
myl = list(map(int, input().split()))



left = 0

max_val = 0
window_sum =0

for right in range(n):

    window_sum += myl[right]

    while window_sum > s:
        window_sum -= myl[left]

        left += 1

    max_val=max(max_val, right - left + 1)
print(max_val)