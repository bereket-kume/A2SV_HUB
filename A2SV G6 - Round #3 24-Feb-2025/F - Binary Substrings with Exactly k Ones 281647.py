# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())  
s = input()

n = len(s)
count = 0
left = 0
one_count = 0
zero_prefix = 0 

for i in range(n):
    for j in range(i+1, n+1):
            if s[i:j].count('1') == k:
                 count += 1

print(count)