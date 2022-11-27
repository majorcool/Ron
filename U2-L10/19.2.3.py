# 19.2.3  计算班级平均成绩
# 定义函数 input_score
# - 允许用户输入 1 次成绩（0-100）、最多两位小数（可以是整数）
# - 如果输入的数字不符合要求，抛出自定义异常 ScoreError
# 在主程序中，完成 30 名学生成绩的录入，并捕获 2 类异常
# 1. 输入的不是数字
# 2. 输入的数字不符合要求
class ScoreError(Exception):
    pass


class NotNumber(Exception):
    pass


def input_score(grade):
    if not int(grade):
        raise NotNumber
    if 100 >= grade >= 0:
        return grade
    else:
        raise ScoreError


try:
    print(input_score(555))
except NotNumber:
    print("输入的不是数字")
except ScoreError:
    print("输入的数字不符合要求")

