# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C


def transform(n, a, b):

    flip_pos = set()
    bal = 0

    for i in range(n):
        if a[i] == '1':
            bal += 1
        elif a[i] == '0':
            bal -= 1
        
        if bal == 0:
            flip_pos.add(i)
    
    flipped = False
    for i in range(n-1, -1, -1):

        if flipped:
            if a[i] == '0':
                current = '1'
            else:
                current = '0'
        else:
            current = a[i]

        if current != b[i]:
            if i  not in flip_pos:
                return 'NO'
            flipped = not flipped
    return 'YES'

t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    x= transform(n, a, b)
    print(x)