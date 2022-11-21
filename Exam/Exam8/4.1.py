# 4.1  全字母短句
# 定义一个函数，参数为一个小写英文字母组成的字符串，判断字符串是否为 '全字母短句'
# 全字母短句，是指一个句子中包含所有的英文字母（小写 a-z）
def check_if_pangram(sentence: str) -> bool:
    all = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for a in sentence:
        for b in range(0, len(all)):
            if b == len(all):
                pass
            elif a == all[b]:
                all.pop(b)
    if not all:
        return True
    else:
        return False


m = "thequickbrownfoxjumpsoverthelazydog"
print(check_if_pangram(m))


