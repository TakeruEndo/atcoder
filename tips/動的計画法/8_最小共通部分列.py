"""
LCS
"""

s = input()
t = input()

# 答えをdpの値にする
dp = [[0]*1010 for i in range(1010)]

for i in range(s):
    for j in range(t):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j] + 1, dp[i][j]+1)
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])

print(dp[s][t])
