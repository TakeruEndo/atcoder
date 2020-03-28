N = int(input())
s = list(input())
Q = int(input())

ans = []
for i in range(Q):
    que = list(input().split())
    if que[0] == '1':
        s[int(que[1])-1] = que[2]
    if que[0] == '2':
        ans.append(len(set(s[int(que[1])-1:int(que[2])])))

for i in ans:
    print(i)
