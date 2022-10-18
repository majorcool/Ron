# 6.2.2 计算以列表形式表示的数字 +1 的值
# 定义一个函数，参数为一个由单位正整数组成的列表，用于表示一个数字
# 最高位数字存放在数组的首位，除了整数 0 之外，这个整数不会以零开头
def add_1(lise_num):
    a = ""
    d = []
    for b in range(0, len(lise_num)):
        a += str(lise_num[b])
    a = str(int(a) + 1)
    for c in range(0, len(a)):
        d.append(int(a[c]))
    d.sort()
    return d


print(add_1([1, 2, 3]))