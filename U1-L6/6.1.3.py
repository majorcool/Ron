# 6.1.3 定义一个函数，参数为 1 个字符串，对该字符串进行逆序，返回逆序后的字符串
def first(n):
    last = len(n) + 1
    print(n[-1: -last: -1])


a = "286156"
first(a)