N, W = map(int, input().split())

V = []
W = []
for i in range(N):
    v, w = map(int, input().split())
    V.append(v)
    W.append(w)

"""
方針
dp[n][w] = 価値の最大値
"""


# n個までの荷物
for n in range(N):
    # 重さの最大値
    for w in range(W+1):
        if w => W[n]:
            dp[n][w] = max(dp[n-1][w], dp[n][w - 1] + V[i]
