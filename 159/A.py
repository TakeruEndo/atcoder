import math

# 組み合わせ算出
def combinations_count(n, r):
    if n == 1:
        return 0
    if n == 0:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if __name__ == '__main__':
    a,b=map(int,input().split())
    # 偶数を2回引く
    e_2 =  combinations_count(a,2)
    # 奇数を２回引く引
    o_2 = combinations_count(b, 2)
    print(e_2 + o_2)
