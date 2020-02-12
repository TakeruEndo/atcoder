a,b=map(int,input().split())

a_list = list(map(int, input().split()))

a_list.sort()

sum_d = 0

for i in range(b):
    sum_d += a_list[i-1]

if (a > sum_d):
    print('No')
else:
    print('Yes')

