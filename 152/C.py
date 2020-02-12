
def calc(n, p):
    min_p = 200000

    count = 0
    
    for i in p:
        # 最小値更新
        if (min_p >= i):
            min_p = i
        if (min_p >= i):
            count += 1

    print(count)


n = int(input())
p = [int(x) for x in input().split()]

calc(n, p)
