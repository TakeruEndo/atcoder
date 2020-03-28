if __name__ == '__main__':
    h, w, k = map(int, input().split())
    s = [[int(i) for i in input()] for j in range(h)]
    for i in range(2**(h-1)): # 2^(H-1)の全探索
        
        for j in range(h):

