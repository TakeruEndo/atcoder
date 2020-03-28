a = int(input())

ans = 0
# 余り
b = a % 500
# 商
c = int(a/500)

ans += c * 1000

d = int(b/5)

ans += d * 5

print(ans)

