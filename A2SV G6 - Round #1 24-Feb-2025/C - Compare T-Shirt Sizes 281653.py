# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

n = int(input())

def get_size_value(size):
    X_count = size.count('X')

    base = size[-1]

    return (base, X_count)

def compare(a, b):
    type_a, count_a = get_size_value(a)
    type_b, count_b = get_size_value(b)


    order = {'S': 0, 'M': 1, 'L': 3}

    if type_a == type_b:
        if type_a == 'S':
            if count_a > count_b:
                print('<')
            elif count_a < count_b:
                print('>')
            else:
                print('=')
        elif type_a == 'L':
            if count_a > count_b:
                print('>')
            elif count_a < count_b:
                print('<')
            else:
                print('=')
        else:
            print('=')
    else:
        if order[type_a] > order[type_b]:
            print('>')
        elif order[type_a] < order[type_b]:
            print('<')
        else:
            print('=')

for _ in range(n):
    x, y = map(str, input().split())
    compare(x, y)