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



