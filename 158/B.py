n, b, r  = map(int, input().split())
 
b_set = b + r
 
re = n % b_set
 
if re <= b:
    print(b * (int(n/b_set)) + re)
else:
    print(b*(int(n /b_set)+1))
