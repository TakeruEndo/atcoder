import collections
import math


if __name__ == '__main__':
    N= int(input())
    a = list(map(int, input().split()))
    c = collections.Counter(a)
    result = 0
    for i in set(a):
        # c[i]の中から2個選ぶ
        result += (c[i]*(c[i]-1))/2

    for i in a:
        d = c[i]
        print(int(result - (d*(d-1))/2 + ((d-1)*(d-2))/2))

## 実行時間超過！！！！！！

