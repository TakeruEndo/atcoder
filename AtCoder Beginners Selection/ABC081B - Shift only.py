n = int(input())
 
d = input().split()
 
for i in range(len(d)):
	d[i] = int(d[i])
 
min_n = []
 
for i in d:
	count = 0
	while i % 2 == 0:
		i = i / 2
		count += 1
	min_n.append(count)