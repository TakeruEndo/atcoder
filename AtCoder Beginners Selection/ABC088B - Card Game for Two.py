n = int(input())
 
d = input().split()
for i in range(len(d)):
  d[i] = int(d[i])
 
d.sort(reverse=True)
alice = 0
bob = 0
 
for i in range(len(d)):
  if i % 2 == 0:
    alice += d[i]
  else: 
    bob += d[i]
  
print(alice-bob)