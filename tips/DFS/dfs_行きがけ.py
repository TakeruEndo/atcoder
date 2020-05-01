# 深さ優先探索（行きがけ）
import sys
from collections import deque

# グラフの作成
N = int(input())
G = [deque([]) for _ in range(N+1)]
for _ in range(N):
    u, k, * V
