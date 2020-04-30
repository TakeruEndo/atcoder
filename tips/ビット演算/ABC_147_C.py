# 人数
n = int(input())
# 人数分繰り返す
# 証言の個数を格納するリスト
a = []
# 証言を格納するリスト
xy = []
for i in range(n):
    # 証言の個数
    a_n = int(input())
    # 証言の個数分繰り返す
    xy_n = []
    for i in range(a_n):
        xy_n.append(list(map(int, input().split())))
    a.append(a_n)
    xy.append(xy_n)

def judge(bit):
    # こっちの方が直感的だが...
    # bit = bin(bit).replace('0b', '')
    # for i in bit:

    # bit....n人の証言を検証する
    for i in range(n):
        # 該当ビットが0なら無視
        if not(bit & (1 << i)):
            continue
        # 証言を検証
        for j in xy[i]:
            # その人を正直と言っているが、実際嘘つきだったらだめ
            # 人物番号とbitのズレは解消すること！
            if j[1] == 1 and not(bit & (1 << (j[0]-1))):
                return False

            # 不親切なのに実際は親切
            if j[1] == 0 and (bit & (1 << (j[0]-1))):
                return False

    return True

max_person = 0
# 2**N通りで考える
for bit in range(1 << n):
    if judge(bit):
        count = 0
        # bitに含まれる人数を数える
        for i in range(n):
            if bit & (1 << i):
                count += 1
        if max_person < count:
            max_person = count

print(max_person)
