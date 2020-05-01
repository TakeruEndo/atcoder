
def dfs(


if __name__=='__main__':
    N, M = map(int,input().split())
    vs = [list(map(int, input().split())) for i in range(M)]
    # グラフ
    G = [[] for i in range(N)]

    for v in vs:
        G[v[0]-1].append(v[1]-1)
        G[v[1]-1].append(v[0]-1)
        
