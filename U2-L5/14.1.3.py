# 14.1.3  定义 Point 类和 Segment 类
# Point 类包含 2 个属性，分别为点的横坐标与纵坐标
# Segment 类包含 2 个私有属性，分别为两个端点的坐标
# Segment 类包含 get_len() 方法，可以获得直线的长度
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))


class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.__start = Point(x1, y1)
        self.__end = Point(x2, y2)

    def get_len(self):
        x1, y1 = self.__start.x, self.__start.y
        x2, y2 = self.__end.x, self.__end.y
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


a = Point(1, 3)
b = Point(2, 4)
c = Segment(1, 3, 2, 4)
print(c.get_len())



