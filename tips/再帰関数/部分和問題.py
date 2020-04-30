
def func(i, x, a):
    if i == 0:
        if x == 0:
            return True
        else:
            False

    if func(i-1, x, a): return True
    if func(i-1, x-a[i-1], a): return True

    return False

if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    if func(n, x, a):
        print('Yes')
    else:
        print('No')
