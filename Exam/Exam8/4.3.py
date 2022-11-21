# 4.3  汉明距离
# 汉明距离是一个概念，表示两个相同长度的字符串对应位置的不同字符的数量
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目
# 定义一个函数，参数为 2 个整数 x 和 y，计算并返回它们之间的汉明距离
def hamming_distance(x: int, y: int) -> int:
    wrong = 0
    x = bin(x)
    y = bin(y)
    x = x[2::]
    y = y[2::]
    for a in range(0, len(x)-1):
        for b in range(0, len(y)-1):
            if x[a] == y[b]:
                x = x[1::]
                y = y[1::]
            else:
                wrong += 1
                x = x[1::]
                y = y[1::]
    return wrong


print(hamming_distance(3, 1))





