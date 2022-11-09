# 1. [多行注释] Python 的 self 是什么？
"""
由哪一个对象调用的方法，方法内的self就是哪一个对象的引用
在类封装的方法内部，self就表示当前调用方法的对象自己
self是实例
"""
class Cat:
    def aa(self):
        print("zxcbn")
        self.name = "123"

    def bb(self):
        print("waesfdg")
        self.name = "321"


Ton = Cat()
TT = Cat()
Ton.aa()
TT.bb()
print(Ton.name)


print(TT.name)
# 2. [多行注释] Python 类的内置方法有哪些？
"""
https://docs.python.org/zh-cn/3/library/functions.html
"""
