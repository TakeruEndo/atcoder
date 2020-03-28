s = input()
n = int(input())

# for t in try_list:
#     if t[0] == '1':
#         s = ''.join(list(reversed(s)))
#     if t[0] == '2':
#         if t[1] == '1':
#             s = t[2] + s
#         else:
#             s = s + t[2]

# 反転の処理に時間がかかる

t = ''
for i in range(n):
    q = input().split()
    if len(q) == 1:
        t, s = s, t
    elif len(q) == 3:
        if q[1] == '1':
            t += q[2]
        elif q[1] == '2':
            s += q[2]

t = t[::-1]
print(t + s)
