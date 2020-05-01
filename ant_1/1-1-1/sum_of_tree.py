k,s = map(int,input().split())

count = 0
for i in range(k+1):
    for j in range(k+1):
        for m in range(k+1):
            if i+j+m == s:
               count += 1

print(count)
