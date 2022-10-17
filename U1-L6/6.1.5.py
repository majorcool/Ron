# 6.1.5 定义一个函数，参数为 1 个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数，将所有数量保存在 1 个元祖返回
def number(str_0):
    E = 0
    K = 0
    S = 0
    for a in range(0, len(str_0) - 1):
        b = str_0[a]
        if b.isalpha():
            E += 1
        elif b.isspace():
            K += 1
        elif b.isdigit():
            S += 1
    Q = len(str_0) - E - K - S
    num = (E, K, S, Q)
    print(num)


zifu = "aA    1s4?'"
number(zifu)

