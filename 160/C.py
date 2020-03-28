k, n = map(int, input().split())

a = list(map(int, input().split()))

# 最も感覚が広い家を探す
max_dis = 0
index = 0
for i in range(len(a)):
    if i+1 == n:
        if a[0] + k - a[i] > max_dis:
            max_dis = a[0] + k - a[i]
            index = i
    else:
        if a[i+1] - a[i] > max_dis:
            max_dis = a[i+1] - a[i]
            index = i

if index+1 == n:
    print(a[n-1]-a[0])
else:
    print(k - a[index+1] + a[index])
