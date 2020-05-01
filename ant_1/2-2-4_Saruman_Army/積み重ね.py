N = int(input())

w = [int(input()) for i in range(N)]

# 考え方
# 無理なら横へ。いけるなら最も差が小さいところに置く

# 場所
room = [100000]
for i in w:
    # 載せられるなら
    min_diff = 100000
    # 更新する位置
    locate = 100
    for ind, j in enumerate(room):
        diff = j - i
        if diff < 0:
            continue
        else:
            if diff <=  min_diff:
                min_diff = diff
                locate = ind
    if locate != 100:
        room[locate] = i
    else:
        room.append(i)

print(len(room))

