s = input()
t = input()

len_s = len(s)
len_t = len(t)

# 一致する位置を探して返す
def search(s, t):
    head = len(s)-len(t)
    tail = len(s)
    for i in range(head+1):
        s_ = s[head:tail]
        # 一致するか確認
        for j in range(len(t)):
            if t[j] != s_[j]:
                if s_[j] != '?':
                    break
        # 正常終了した
        else:
            return head, tail
        head -= 1
        tail -= 1
        continue
    return None, None

# tの文字列分後ろからみて一致したら入れる
if len_s < len_t:
    print('UNRESTORABLE')
else:
    head, tail = search(s, t)
    if head is None:
        print('UNRESTORABLE')
    else:
        s = list(s)
        s[head:tail] = t
        s = "".join(s)
        s = s.replace('?', 'a')
        print(s)
