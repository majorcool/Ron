# 6.1.2 定义一个函数，参数为 1 个字符串，判断它是否为 '回文数'
# 如果一个数字左右对称，就是 '回文数'，如 123454321, 1221
def number(num):
    if len(num) % 2 == 0:
        long_1_1 = int(len(num) / 2)
        long_1_2 = int(len(num) / -2 - 1)
        num_1_1 = num[0: long_1_1]
        num_1_2 = num[-1: long_1_2: -1]
        if num_1_1 == num_1_2:
            print("是回文数")
        else:
            print("不是回文数")
    if len(num) % 2 == 1:
        long_2_1 = int(len(num) / 2)
        long_2_2 = int(len(num) / -2 - 1)
        num_2_1 = num[0: long_2_1]
        num_2_2 = num[-1: long_2_2: -1]
        if num_2_1 == num_2_2:
            print("是回文数")
        else:
            print("不是回文数")


a = str(input("请输入数字："))

number(a)