a,b=map(int,input().split())

a_4 = int(str(a)*b)

b_4 = int(str(b)*a)

if (a_4 > b_4):
    print(a_4)
else:
    print(b_4)