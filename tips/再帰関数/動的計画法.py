
def fibo(n, memo):
    # ベースケース
    if (n==0): return 0
    elif n==1: return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

if __name__=='__main__':
    memo = [-1]*50
    for i in range(50):
        print(i, "項目の値:", fibo(i, memo))
