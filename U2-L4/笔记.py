class Exam:
    def __init__(self, id, start_time, end_time, points):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.points = points


class Test(Exam):
    def __init__(self):  # 根本没有用从Exam中继承的方法
        self.id = ""
        self.points = 10


# 继承，覆盖写法重写
class Animals:
    def call(self):  # self是实例
        print("animals")

    def go(self):
        print("Pig is an animal")


class Cat(Animals):
    def call(self):
        print("cat")


dog = Animals()
cat = Cat()
dog.call()
cat.call()

# 继承，拓展写法内置函数super().实例方法名()


class Pig(Animals):

    def call(self):
        super().call()
        print("pig")


pig = Pig()
pig.call()
Animals.go(pig)