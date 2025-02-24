# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter

n = int(input())

for _ in range(n):
    x = int(input()) 
    word = input()
    total = 0
    set_left = set()
    counter_right = Counter(word) 

    for i in range(len(word)):
        set_left.add(word[i])
        counter_right[word[i]] -= 1
        if counter_right[word[i]] == 0:
            del counter_right[word[i]] 
        total = max(total, len(set_left) + len(counter_right))
    
    print(total)
