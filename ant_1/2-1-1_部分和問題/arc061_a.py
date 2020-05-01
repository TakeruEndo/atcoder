
if __name__=='__main__':
    s = input()
    locate = len(s)-1

    # +を入れる箇所をbit探索で探す
    sum_all = 0
    for bit in range(1 << locate):
        binary = str(format(bit, 'b'))
        binary = binary.zfill(len(s)-1)
        head = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                sum_all += int(s[head:i+1])
                head = i+1
        sum_all += int(s[head:])

    print(sum_all)
