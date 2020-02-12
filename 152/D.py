# import itertools

# n = int(input())

# count = 0

# for i in list(itertools.permutations(range(n + 1), 2)):
#     # print(i)
#     a = str(i[0])
#     b = str(i[1])
#     a_head = a[0]
#     if (a_head == "0"):
#         continue
#     a_tail = a[len(a) - 1]

#     b_head = b[0]
#     if (b_head == "0"):
#         continue    
#     b_tail = b[len(b) - 1]
#     if (a_head == b_tail and a_tail == b_head):
#         count += 1
#         print(i)


#  https://atcoder.jp/contests/abc152/submissions/9618064

N = int(input())
 
c = [[0] * 10 for i in range(10)]
 
for i in range(1, N + 1):
    a = i % 10
    b = 0
    while i > 0:
        b = i
        i = i // 10
    c[a][b] += 1
 
ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j]*c[j][i]
 
print(ans)
