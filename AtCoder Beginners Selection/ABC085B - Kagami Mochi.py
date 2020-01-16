n = int(input())
d = []
 
for i in range(n):
  d.append(0)
 
for i in range(n):
  d[i] = int(input())
 
print(len(set(d)))