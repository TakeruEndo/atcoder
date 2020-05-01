
N = int(input())

xl = [list(map(int,input().split())) for i in range(N)]

# 区間の座標に変換
robot_range = []
for i in xl:
    robot_range.append([i[0]+i[1], i[0]-i[1]])

robot_range = sorted(robot_range)

tail = robot_range[0][0]
ans = 1

for rl in robot_range:
    if rl[1] < tail:
        continue
    else:
        ans += 1
        tail = rl[0]

print(ans)
