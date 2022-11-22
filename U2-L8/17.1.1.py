# 17.1.1  统计水果数量
# 定义水果类 Fruit，包含类属性品种 variety
# 定义 5 个品种的水果类，继承自 Fruit，包含类属性数量 nums
# 在主程序中分别为 5 种水果创建若干实例，打印水果的品种数以及各自品种的数量
class Fruit:
    variety = 0

    def __init__(self):
        Fruit.variety += 1


class Apple(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Apple.nums += 1


class Banana(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Banana.nums += 1


class Orange(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Orange.nums += 1


class Watermelon(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Watermelon.nums += 1


class Pear(Fruit):
    nums = 0

    def __init__(self):
        super().__init__()
        Pear.nums += 1


apple = Apple()
apple_2 = Apple()
apple_3 = Apple()
banana = Banana()
orange = Orange()
watermelon = Watermelon()
watermelon_2 = Watermelon()
pear = Pear()
print(Fruit.variety)
print(Apple.nums)
print(Banana.nums)
print(Orange.nums)
print(Watermelon.nums)
print(Pear.nums)
