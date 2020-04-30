N, M = map(int, input().split())

a_list = list(map(int, input().split()))
ans = 0

for x in range(a_list[len(a_list)-1], M):
    ans_flag = 0
    for a in a_list:
        p = x/a -0.5
        if int(p) == p:
            ans_flag += 1
    if ans_flag == len(a_list):
        ans += 1

print(ans)
