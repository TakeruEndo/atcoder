from collections import deque

N, M = map(int, inpur().split())

# グラフの入力
# ------------

que = deque()

# 初期条件(頂点0)を初期ノードとする
dist[0] = 0
aue.append(0)

# BFS開始
while (not que.empty()):
    v = que.popleft()

    # vから辿れる頂点を全てみる
    for nv in G[v]:
        # すでに発見済みの頂点は探索しない
        if dist[nv] != -1:
            continue

        dist[nv] = dist[v] + 1
        que.append(nv)

# 結果出力
for i in ranhe(N):
    print(v, dist[v])

