
def dfs(G, v):
    """
    G: 探索するグラフ
    v:
    """
    # vを訪問済みにする
    seen[v] = True
    
    # vからいける各頂点next_vについて
    for next_v in G[v]:
        # 探索済みだったらスルー
        if seen[next_v]:
            continue
        dfs(G, next_v)


if __name__=='__main__':
    # 頂点の数と辺数
    N, M, s, t = map(int, input().split())

    # グラフの初期化
    # To DO いい方法あるはず
    G = {}
    for i in range(N):
        G[i] = []
    for i in range(M):
        a, b = map(int,input().split())
        # ここでは無向グラフを想定
        G[a].append(b)
        G[b].append(a)

    seen = [False]*N
    # 頂点sをスタートとした探索
    dfs(G, s)

    print(seen)
