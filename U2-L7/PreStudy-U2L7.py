# 1. 什么是多态？
# 不同的子类对象调用相同的父类方法，产生不同的执行结果（同样的行为产生不一样的结果）
# 增加代码的灵活程度
# 以继承和重写父类方法为前提
# 是调用方法的技巧，不会影响类的内部设计

# 2. 如何实现多态？
# 一般来说！！！！！！
# 继承：多态发生在子类和父类之间（多态可以不建立在继承的基础上[可以只有相同的方法名]{只有Python可以！！！！！！}）
# 重写：子类重写了父类的方法
# 对象调用同一个函数/方法/属性，改变传入对象的实参
def show(animal):
    animal.kind(animal)


class Animal:
    def kind(self):
        print("animal")


class Dog(Animal):
    def kind(self):
        print("dog")


class Cat(Animal):
    def kind(self):
        print("cat")


dog = Dog
cat = Cat
show(dog)
show(cat)


# -------------分界


def add(a, b):
    print(a + b)


add(1, 2)
add("1", "2")
add([1], [2])
# 以上皆为多态
