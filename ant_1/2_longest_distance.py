import math

n = int(input())
co = []
for i in range(n):
    co.append(list(map(int, input().split())))

def calc_dis(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

max_dis = 0

for i in co:
    for j in co:
        dis = calc_dis(i, j)
        if max_dis < dis:
            max_dis = dis

print(max_dis)
