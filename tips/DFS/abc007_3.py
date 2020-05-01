
def dfs(h, w, gx, gy):
    global count
    # 通ったかどうか記録
    d[h][w] = 1
    print(gx, gy)
    for i in range(4):
        count += 1
        nh = h + dy[i]
        nw = w + dx[i]

        if nh < 0 or nw < 0 or nh >= H or nw >=W:
            count -= 1
            continue
        if d[nh][nw] == 1:
            count -= 1
            continue
        if field[nh][nw] == '#':
            count -= 1
            continue
        if nw == gx-1 and nh == gy-1:
            print(nh, nw)
            break
        dfs(nh, nw, gx, gy)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

H, W = map(int,input().split())
# スタート地点
sy, sx = map(int, input().split())
# ゴール地点
gx, gy = map(int, input().split())

field = []
for i in range(H):
    field.append(list(input()))

d = [[0]*W] * H

count = 0

# スタート地点を与える
dfs(sy-1, sx-1, gx, gy)
