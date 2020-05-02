
n = int(input())

p = list(map(int, input().split()))

# p1...pnそれぞれまでの得点の撮り方をdpとする
dp = [[0]*10010 for i in range(110)]

# 漸化式を考える
"""
