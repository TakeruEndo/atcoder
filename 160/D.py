n, x, y = map(int,input().split())

ans_list = [0]*(n)
for i in range(1, n+1):
    for j in range(i+1, n+1):
            min_dis = min(abs(j-i), abs(x-i) + 1 + abs(j-y), abs(y-i)+1+abs(j-x))
            ans_list[min_dis] += 1

for i in range(1, len(ans_list)):
    print(ans_list[i])
