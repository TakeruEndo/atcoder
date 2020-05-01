# pythonだとデフォルトの再帰処理回数の上限に引っかかってしまうので、それを変更
import sys
sys.setrecursionlimit(1000000)

# 4方向への移動bベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(h, w):
    d[h][w] = 1
    # 4方向を探索
    for dire in range(4):
        nh = h + dx[dire]
        nw = w + dy[dire]

        # 場外アウト、壁ならスルー
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == '#':
            continue
        if d[nh][nw] == 1:
            continue
        dfs(nh, nw)

if __name__=='__main__':
    H, W = map(int, input().split())
    field = []
    for i in range(H):
        field.append(list(input()))

    # sとgのマスを特定する
    for h in range(H):
        for w in range(W):
            if field[h][w] == 's':
                sh = h
                sw = w
            if field[h][w] == 'g':
                gh = h
                gw = w

    # 到達したがどうか管理する
    d = [[0]*W]*W
    # スタート地点から探索を始める
    dfs(sh, sw)
    print(d)
    print(field)
    if d[gh][gw] == 1:
        print('Yes')
    else:
        print('No')
