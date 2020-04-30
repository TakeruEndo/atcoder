"""
問題
N 個の正の整数 a0,a1,…,aN−1 と、正の整数 W とが与えられます。

a0,a1,…,aN−1 の中から何個か選んで総和を W とすることができるかどうかを判定してください
"""

def intTovect(bit, n):
    # 選んだものを格納するリスト
    S = [0]
    for i in range(n):
        if bit & (1 << i):
            S.append(i)

    return S

if __name__=='__main__':
    n,m = map(int, input().split())
    a = list(map(int, input().split()))

    exist = False
    # 1 << N (2**N通り)
    for i in range(1 << n):
        # どれを選ぶか
        S = intTovect(i, n)
        # 部分集合の総和
        print(S)
        sum_ = 0
        for i in S:
            sum_ += a[i]

        if sum_ == m:
            exist = True

    if exist == True:
        print('Yes')
    else:
        print('No')
