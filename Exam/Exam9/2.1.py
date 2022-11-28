# 2.1  探究 finally 的执行机制
# 在 try……finally 结构中，无论 try 语句是否出现异常，finally 语句都会执行
# 在函数中，finally 的执行顺序在 return 之前还是之后？
# 设计一段代码，探究以上问题，在设计并运行代码后，用多行注释简单说明 finally 的执行机
try:
    print(int("m"))
except ValueError:
    print(111)
finally:
    print("finally")

try:
    print(int(1))
except Exception as a:
    print(a)
finally:
    print("finally")
print("----------------------")


def no():
    try:
        print(int("m"))
    except ValueError:
        return "except"
    finally:
        print("finally")


print(no())
"""
在try...finally中，无论try语句是否出现异常，finally语句都会执行，且优先级在return之后
"""

