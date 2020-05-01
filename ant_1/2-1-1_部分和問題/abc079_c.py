if __name__=='__main__':
    s = input()

    # bit全探索0-> -, 1-> +
    for i in range(1 << (len(s)-1)):
        bina = bin(i).replace('0b', '')
        bina = bina.zfill(len(s)-1)
        ans = int(s[0])
        ans_s = s[0]
        for j in range(len(bina)):
            if bina[j] == '1':
                ans_s += '+' + s[j+1]
                ans += int(s[j+1])
            else:
                ans_s += '-' + s[j+1]
                ans -= int(s[j+1])
        if ans == 7:
            print(ans_s + '=7')
            break
