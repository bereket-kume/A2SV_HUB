# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    t = int(input())


    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    
    sorted_num = sorted(nums)
    sort_prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        sort_prefix[i] = sort_prefix[i - 1] + sorted_num[i - 1]
    val = 0
    for _ in range(t):
        ty, start, end = map(int, input().split())
        if ty == 1:
            val = prefix[end] - prefix[start-1]
        else:
            val = sort_prefix[end] - sort_prefix[start-1]

        print(val)

if __name__ == '__main__':
    main()