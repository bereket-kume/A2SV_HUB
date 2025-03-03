# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

def main():
    t = int(input())
    for _ in range(t):
        nr = int(input())
        r = list(map(int, input().split()))
        
        nl = int(input())
        b = list(map(int, input().split()))

        max_r, max_b = 0, 0
        sum_r, sum_b = 0, 0

        for num in r:
            sum_r += num
            max_r = max(max_r, sum_r)
        
        for num in b:
            sum_b += num
            max_b = max(max_b, sum_b)

        print(max_r + max_b)

if __name__ == '__main__':
    main()
