# 19.2.1  随机数
# 让用户输入 2 个整数 start 和 end，打印这两个整数之间（包含两端）的一个随机整数
# 考虑用户输入不是整数的情况，以及 start > end 的情况，抛出异常并处理
import random


class StartEndError(Exception):
    pass


class Not(Exception):
    pass


def start_end():
    start = input("start:")
    end = input("end:")
    if start > end:
        raise StartEndError
    if start != int or end != int:
        raise Not
    return random.randint(start, end)


try:
    print(start_end())

except StartEndError:
    print("AreaError")
except Not:
    print("not int")




