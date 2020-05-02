"""
問題 3:　部分和問題　
nn 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 AA が与えられる。これらの整数から何個かの整数を選んで総和が AA になるようにすることが可能か判定せよ。可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。
"""

n, A = map(int, input().split())

a = list(map(int, input().split()))

# dpを初期化
dp = [[False]*(A+5) for i in range(n+5)]
dp[0][0] = True

# aのループ
for i in range(n):
    # aiまでで最大値Aと等しい値を取れるかどうか判断
    for j in range(A+1):
        # 最大値より小さいなら加算できる
        if j >= a[i]:
            if dp[i][j-a[i]]:
                dp[i+1][j] = True
            else:
                dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

print(dp)
if dp[n][A] == True:
    print('YES')
else:
    print('NO')

            

