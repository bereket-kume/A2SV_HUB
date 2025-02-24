# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())

for _ in range(t):
    n = int(input())
    word = input()
    left = 0
    right = len(word) - 1
    count = float('inf')
    char = set(word)
    

    for ch in char:
        left,right=0, len(word)-1
        t=0
        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            elif word[left]  == ch:
                left += 1
                t += 1
            elif word[right] == ch:
                right -= 1
                t += 1
            else:
                t=float('inf')
                break
        count = min(count, t)
    if count == float('inf'):
        print(-1)
    else:
        print(count)