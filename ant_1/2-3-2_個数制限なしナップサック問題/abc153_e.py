H, N = map(int, input().split())

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

"""
方針
dp[i] = モンスターの体力をi減らすために消耗する魔力の最小値
"""

INF = 1 << 30
dp = [INF]*10000

# モンスターの体力
for h in range(H):
    # 使う魔法(何回でも使える)
    for n in range(N):
        dp[h] = min(dp[h], dp[max(h-A[n], 0) ])

print(dp[H])
