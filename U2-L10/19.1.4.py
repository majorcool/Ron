# 19.1.4  计算圆面积
# 定义一个函数，参数为半径 r，计算圆的面积
# 自定义一个异常类 RadiusError，如果半径为负值，抛出 RadiusError
class RadiusError(Exception):
    pass


def area(r):
    if r < 0:
        raise RadiusError("半径不为负值")
    return r ** 2 * 3.14


print(area(-1))

