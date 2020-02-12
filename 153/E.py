a,N=map(int,input().split())

AB = [tuple(map(int,input().split())) for i in range(N)]

kouritu = []

for i, x in enumerate(AB):
    kouritu.append([(x[0] / x[1]), i])

kouritu.sort(reverse=True)

print(kouritu)

    