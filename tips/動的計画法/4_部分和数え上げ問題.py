
n, A = map(int, input().split())

a = list(map(int, input().split()))

# dpを初期化
dp = [[0]*(10010) for i in range(1000)]
dp[0][0] = 1

# aのループ
for i in range(n):
    # aiまでで何通りか+
    for j in range(A+1):
        # 最大値より小さいなら加算できる
        if j >= a[i]:
                dp[i+1][j] = dp[i][j-a[i]] + dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

Print(dp[n][A]) 
