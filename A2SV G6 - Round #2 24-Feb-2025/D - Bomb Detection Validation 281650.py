# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

x, y = list(map(int, input().split()))

matrix = []

for _ in range(x):
    lrow = list(input().strip())
    matrix.append(lrow)

row=len(matrix)
col=len(matrix[0])

def count_bomb(i, j):
    count_bomb=0
   

    direction = [(-1, 0), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), (0, -1)]

    for dx, dy in direction:
        ni, nj = i + dx, j + dy

        if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == "*":
            count_bomb += 1
    return count_bomb
 
def check_bomb(i, j):
    return count_bomb(i, j) == 0
            
flag=True
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.':
            if not check_bomb(i, j):
                flag = False
                break
        elif matrix[i][j] == '*':
              continue
        else:
            v=count_bomb(i, j)
            if int(matrix[i][j]) != v:
                flag=False
                break
    if not flag:
        break
if flag:
      print("YES")
else:
      print("NO")
