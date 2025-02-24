# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
n = int(input())

for _ in range(n):
    orginal = input()
    goal = input()
    helper =input()
    myhash = Counter(helper)
    x=0

    flag=True
    for i in range(len(goal)):
        if x < len(orginal) and  orginal[x] == goal[i]:
            x += 1
        else:
            if goal[i] in myhash:
                myhash[goal[i]] -= 1
                if myhash[goal[i]] == 0:
                    del  myhash[goal[i]]
            else:
                flag=False
                break

    if x < len(orginal):
        flag = False
    
    if flag:
        print("YES")
    else:
        print('NO')