# 6.2.3 二进制加法
# 定义一个函数，参数为 2 个二进制字符串 a, b，计算它们的和
def add_2(a, b):
    return str(bin((int(a, 2) + int(b, 2)))).removeprefix("0b")
"""
int(a, 2)将a转换为十进制
(int(a, 2) + int(b, 2))a和b的十进制加法
bin()转化为二进制，前面自带0b
转化为str后.removeprefix("0b")删除前缀
"""