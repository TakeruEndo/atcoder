import itertools

n = int(input())
k = int(input())
cl = []
for i in range(n):
    cl.append(int(input()))

ans_list = []
# 3枚とる組み合わせ
comb = list(itertools.permutations(cl, k))
for li in comb:
    comb_2 = list(itertools.permutations(li))
    for li_2 in comb_2:
        ans = ''
        for i in li_2:
            ans += str(i)
        ans_list.append(ans)

print(len(set(ans_list)))
