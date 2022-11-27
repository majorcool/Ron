# 19.1.3  分母异常
# 定义一个函数，参数为两个数字 a，b，计算 a / b 的值
# 如果 b 等于零，抛出异常
def ab(a, b):
    if b == 0:
        raise Exception("除数不为0")
    return a/b


print(ab(1, 0))





