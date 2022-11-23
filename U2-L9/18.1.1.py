# 课堂练习 18.1（U2-L9）
# 18.1.1  理解 '对象'
# 定义 A 类
# 属性
# - 类属性 nums
# - 实例属性 nums
# 方法
# - 静态方法 test1，打印 dir(A)，但是，不打印其中的内置方法
# - 类方法 test2，打印 dir(cls)，但是，不打印其中的内置方法
# - 实例方法 test(3)，打印 dir(self)，但是，不打印其中的内置方法
# 主程序
# 调用静态方法 test1()
# 调用类方法 test2()
# 调用实例方法 test(3)
class A:
    nums = 0

    @staticmethod
    def test1():
        dir_A = []
        for a in dir(A):
            if a[:2] != "__" and a[::-1][:2] != "__":
                dir_A.append(a)
        print(dir_A)

    @classmethod
    def test2(cls):
        dir_cls = []
        for a in dir(cls):
            if a[:2] != "__" and a[::-1][:2] != "__":
                dir_cls.append(a)
        print(dir_cls)

    def __init__(self):
        self.nums = 0

    def test3(self):
        dir_self = []
        for a in dir(self):
            if a[:2] != "__" and a[::-1][:2] != "__":
                dir_self.append(a)
        print(dir_self)


A.test1()
A.test2()
A().test3()
