import math
import time

if __name__ == '__main__':
    start = time.time()
    a = int(input())
    count = 0
    while(a != 1):
        count += 1
        a = math.floor(a / 2)
    elapsed_time = time.time() - start
    print("count:", count)
    sum_d = 0
    d = 1
    for i in range(count):
        sum_d += 2 ** d
        d += 1
    print(sum_d + 1)
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")



