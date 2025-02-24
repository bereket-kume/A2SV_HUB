# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

test=int(input())



for _ in range(test):
    n=int(input())
    matrix = []

    for _ in range(n):
        lrow = list(input().strip())
        matrix.append(lrow)
    visted = set()
    total = 0

    for i in range(n):
        for j in range(n):
            if (i, j) not in visted:
                val = [
                    matrix[i][j],
                    matrix[j][n-1-i],
                    matrix[n-1-i][n-1-j],
                    matrix[n-1-j][i]
                ]
                
                total += min(val.count('0'), val.count('1'))
                visted.add((i, j))
                visted.add((j, n-1-i))
                visted.add((n-1-i, n-1-j))
                visted.add((n-1-j, i))
    print(total)





