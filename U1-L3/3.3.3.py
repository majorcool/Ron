# 3.3.3 按照下列格式打印九九乘法表
'''
1 * 1 = 1
1 * 2 = 2    2 * 2 = 4
1 * 3 = 3    2 * 3 = 6    3 * 3 = 9
……
'''
num = 0
for a in range(1, 10):
    print("\n")
    for b in range(1, a+1):
        num = a * b
        print(a, " * ", b, end=" = ")
        print(num, end="\t")
