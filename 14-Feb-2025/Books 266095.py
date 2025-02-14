# Problem: Books - https://codeforces.com/contest/279/problem/B

x, y = map(int, input().split())
books = list(map(int, input().split()))

left, right = 0, 0
max_len = 0
current_sum = 0

while right < len(books):
    current_sum += books[right]

    while current_sum > y:
        current_sum -= books[left]
        left += 1
    
    max_len = max(max_len, right - left + 1)
    right += 1
print(max_len)