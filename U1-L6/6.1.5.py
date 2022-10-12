# 6.1.5 定义一个函数，参数为 1 个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数，将所有数量保存在 1 个元祖返回
def number(n):
    for a in range (0, len(n) - 1):
        b = n[a]
        E = 0
        K = 0
        S = 0
        Q = 0
        if b.isalpha():
            E += 1
        elif b.isspace():
            K += 1
        elif b.isdigit():
            S += 1
        else:
            Q += 1
    num = (E, K, S, Q)
    print(num)


zifu = "a 1?"
number(zifu)
# 废，我需要leeues......
