# 1. [多行注释] Python 的 self 是什么？
"""
由哪一个对象调用的方法，方法内的self就是哪一个对象的引用
在类封装的方法内部，self就表示当前调用方法的对象自己
"""
class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

tom = Cat()
tom.name = "Tom"
tom.eat()

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
# 2. [多行注释] Python 类的内置方法有哪些？
"""
https://docs.python.org/zh-cn/3/library/functions.html
"""
