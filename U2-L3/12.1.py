# 12.1.1  探究 Python 的设计哲学
# 通过各种手段（除了问我），探究 Python 为什么没有真正的私有属性、私有方法
# 要求：① 50 字以内的结论（保证清晰的前提下，越精炼越好） ② 标明参考信息来源
# 使用伪私有属性方法是为了避免在类树中，多个类赋值相同的属性引发冲突问题。（不同类之间对象名相同的冲突）---百度贴吧
# 相信用户是一个高素质的人---teacher

# 12.1.2  判断输出
# foo

# 12.1.3  统计数量
# 下方代码中，有几个实例属性？几个实例方法？几个私有实例属性？几个私有实例方法？
class Fruit:
    def __init__(self):
        self.name = 'good'
        self._price = '100'
        self.__real_name = 'bad'
        self.__real_price = '1'

    def __del__(self):
        pass

    def __rot(self):
        print('no')

    def rot(self):
        print('yes')

    def _secret(self):
        print(self.__real_name)

    def __another_secret(self):
        print(self.__real_name)
# 实例属性2
# 实例方法4
# 私有实列属性2
# 私有实例方法2

# 12.1.4  判断输出
# 已知左侧的输出为 30，右侧的输出为？
# 30
# print(len(dir(test)))
# 统计所有方法等

# 12.1.5  修改实例属性
# 将下方代码中的实例属性改为私有属性
# 编写一个实例方法，功能是将私有属性重新赋值，但是要进行判断，新的值长度需要小于 10，否则保持不变


class Person:
    def __init__(self, name):
        self.thing = None
        self.__name = name

    def something(self, some):
        some = str(some)
        if len(some) < 10:
            self._Person__name = some
            print(self._Person__name)


a1 = Person("114")
a1.something(514)



