x, y, a,b,c = map(int,input().split())
pa = list(map(int, input().split()))
qb = list(map(int, input().split()))
rc = list(map(int, input().split()))

pa.sort(reverse=True)
qb.sort(reverse=True)
rc.sort(reverse=True)

pa = pa[:x]
qb = qb[:y]

_all = rc + pa + qb
_all.sort(reverse=True)

ans = 0
for i in range(x+y):
    ans += _all[i]

print(ans)
