"""
問題 2:　ナップサック問題
nn 個の品物があり、ii 番目の品物のそれぞれ重さと価値が weight[i],value[i]weight[i],value[i] となっている (i=0,1,...,n−1i=0,1,...,n−1)。
これらの品物から重さの総和が WW を超えないように選んだときの、価値の総和の最大値を求めよ。

【制約】
・1≤n≤1001≤n≤100
・weight[i],value[i]weight[i],value[i] は整数
・1≤weight[i],value[i]≤10001≤weight[i],value[i]≤1000
・1≤W≤100001≤W≤10000

【数値例】
1)
　n=6n=6
　(weight,value)=(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)(weight,value)=(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)
　W=9W=9
　答え: 94 ((3,6), (1,3), (5,85) を選んだときが最大です)
"""


dp = [[0]*110 for i in range(10010)]

n, W = map(int,input().split())

wv = []
for i in range(n):
    wv.append(list(map(int, input().split())))

# DPループ
for i in range(n):
    for w in range(W+1):
        if w >= wv[i][0]:
            dp[i+1][w] = max(dp[i][w-wv[i][0]] + wv[i][1], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
print(dp[n][W])

