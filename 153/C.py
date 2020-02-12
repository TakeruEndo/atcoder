a,b=map(int,input().split())

a_list = list(map(int, input().split()))

a_list.sort(reverse=True)

sum_d = 0

for i, x in enumerate(a_list):
    if(b != 0):
        b -= 1 
    else:
        sum_d += x

print(sum_d)

    