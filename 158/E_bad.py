n, p = map(int, input().split())
s = input()

ans = 0
for i in range(len(s)):
    t = s[i:]
    for j in range(0, len(t)+1):
        if t[:j] != '':
            if int(t[:j]) % p == 0:
                ans += 1

print(ans)
