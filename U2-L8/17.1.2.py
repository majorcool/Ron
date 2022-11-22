# 17.1.2  统计水果数量 2.0
# 在 17.1.1 的基础上添加一个逻辑：如果在主程序中删除了水果实例，就要修改对应的类属性 nums
class Fruit:
    variety = 0

    def __init__(self):
        Fruit.variety += 1


class Apple(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Apple.nums += 1

    def __del__(self):
        Apple.nums -= 1


class Banana(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Banana.nums += 1

    def __del__(self):
        Banana.nums -= 1


class Orange(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Orange.nums += 1

    def __del__(self):
        Orange.nums -= 1


class Watermelon(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Watermelon.nums += 1

    def __del__(self):
        Watermelon.nums -= 1


class Pear(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Pear.nums += 1

    def __del__(self):
        Pear.nums -= 1


apple = Apple()
apple_2 = Apple()
apple_3 = Apple()
banana = Banana()
orange = Orange()
watermelon = Watermelon()
watermelon_2 = Watermelon()
pear = Pear()
del apple
del banana
print(Fruit.variety)
print(Apple.nums)
print(Banana.nums)
print(Orange.nums)
print(Watermelon.nums)
print(Pear.nums)
