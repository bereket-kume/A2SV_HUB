# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

l1 = int(input())
arr1 = list(map(int, input().split()))
l2 = int(input())
arr2 = list(map(int, input().split()))

if sum(arr1) != sum(arr2):
    print(-1)
    exit()

p1=p2=0
a=arr1[0]
b=arr2[0]
op1=op2=0

while p1 < l1 and p2 < l2:
    if a == b:
        p1 += 1
        p2 += 1
        if p1 < l1:
            a=arr1[p1]
        
        if p2 < l2:
            b=arr2[p2]
        
    elif a < b:
        p1 += 1
        if p1 < l1:
            a += arr1[p1]
            op1 += 1
        
    else:
        p2 += 1
        if p2 < l2:
            b += arr2[p2]
        op2 += 1
print(min(l1 -op1,l2-op2))
    