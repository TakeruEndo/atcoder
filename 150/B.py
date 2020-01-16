def calc(num, word):
    word_len = len(word)
    none_abc = word.replace("ABC", "")
    none_abc_len = len(none_abc)
    print(int((word_len - none_abc_len) / 3))


num = int(input())
word = str(input())

calc(num, word)
