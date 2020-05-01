import sys
sys.setrecursionlimit(1000000)

# 4方向への移動bベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(h, w, type_):
    if type_ == 'first':
        pass
    else:
        d[h][w] = 1
    global count
    count += 1
    # 4方向を探索
    for dire in range(4):
        nh = h + dy[dire]
        nw = w + dx[dire]

        # 場外アウト、壁ならスルー
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if d[nh][nw] == 1:
            continue
        if field[nh][nw] == 'x':
            continue
        dfs(nh, nw, 'other')

if __name__=='__main__':
    H, W = 10, 10
    field = []
    # 陸地のカウント数
    land_c = 0
    # 適当な陸地座標
    lx, ly = 0, 0
    for i in range(H):
        field.append(list(input()))

    # oの数をカウントする
    o_count = 0
    for h in range(H):
        for w in range(W):
            if field[h][w] == 'o':
                o_count += 1

    for h in range(H):
        for w in range(W):
            if field[h][w] == 'x':
                d = [[0]*W for i in range(H)]
                count = 0
                dfs(h, w, 'first')
                if count-1 == o_count:
                    print('YES')
                    sys.exit()

    print('NO')
