import collections

n = int(input())

l = list(map(int, input().split()))

c = collections.Counter(l)

print(c[1])
for i,value in enumerate(l):
  print(c[i+2])
