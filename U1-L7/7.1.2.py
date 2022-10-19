# 7.1.2  定义一个函数，参数为一个正整数 n，判断 n 是不是 哈哈数
# 哈哈数的定义如下：对于一个正整数，计算每一位数字的平方，求和，得到一个新的正整数
# 对于新的正整数，重复这个过程，直到和变为 1，也可能是无限循环但始终不为 1。
# 如果最终和为1，那么这个数就是哈哈数，返回 True，否则返回 False
# 不会
def hihi(n, num=0, tyr_nun = 0):
    n = str(n)
    if n == "1":
        tyr_nun += 1
        return True
    if tyr_nun > 900:
        return False
    else:
        for a in range(0, len(n)):
            num += a ** 2
    return hihi(num)


print(hihi(2))
