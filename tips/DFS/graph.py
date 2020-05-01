


if __name__=='__main__':
    N, M = map(int,input().split())
    
    # グラフを表す辞書を作成
    G = {}
    for i in range(M):
        # つなぐ頂点a, bを入力
        a, b = map(int,inout().split())
        G[a].append(b)

        # 無向グラフの場合以下を追加
        G[b].append(a)


