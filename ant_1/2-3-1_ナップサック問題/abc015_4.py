
W = int(input())

N, K = map(int, input().split())

w_v = [list(map(int, input().split())) for i in range(N)]

"""
考え方
n番目まで調べた時の,幅合計w, 使用枚数k
dp[n][w][k]のとり方は、
1. dp[n-1][j][k]を選んだ場合
dp[n-1][w-w_v[n-1][0]][k-1] + w_v[n-1][1]
2. 選ばなかった場合
dp[n-1][w][k]
"""
# 初期状態の設定
dp = [[[0]*(K+1) for i in range(W+1)] for j in range(N+1)]


# 読み取っている画像番号
for n in range(N):
    # 画像の幅
    for w in range(W+1):
        # 読み取れる画像枚数
        for k in range(K):
            # 選んだ場合
            # 幅を満たす
            if w >= w_v[n][0]:
                # 選んだ場合と選ばなかった場合の最大値を取る
                dp[n+1][w][k] = max(dp[n][w - w_v[n][0]][k-1] + w_v[n][1], dp[n][w][k])
            # 選ばなかった場合
            else:
                dp[n+1][w][k] = dp[n][w][k]

print(dp[N][W][K-1])

