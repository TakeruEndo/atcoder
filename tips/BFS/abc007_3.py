from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

H, W = map(int,input().split())
# スタート地点
sy, sx = map(int, input().split())
# ゴール地点
gy, gx = map(int, input().split())

field = []
for i in range(H):
    field.append(list(input()))


que = deque()
que.append((sy-1,sx-1, 0))

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# BFSをスタート
def bfs(gy, gx):
    while len(que) > 0:
        # 左から取る
        y, x, depth = que.popleft()
        # ゴール
        if (y == gy and x == gx):
            return depth
        # 4通り探す
        for i in  range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if field[ny][nx] == '.':
                que.append((ny, nx, depth+1))
                # 一度行ったfieldは更新
                field[ny][nx] = '#'

print(bfs(gy-1,gx-1))



