import itertools
N = int(input())
P = [int(x) for x in input().split()]
Q = [int(x) for x in input().split()]
 
X = list(range(1, N + 1))
Y = list(itertools.permutations(X))
 
a = Y.index(tuple(P)) + 1
 
b = Y.index(tuple(Q)) + 1
 
if a > b:
    print(a - b)
else:
    print(b - a)
