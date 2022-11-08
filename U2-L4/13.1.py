# 13.1.1  了解术语
# 查询下列术语的英文词汇，添加在属于后方
# 1. 基类bass class
# 2. 超类superclass
# 3. 父类parent class
# 4. 子类subclass
# 5. 派生类derived class

# 13.1.2  定义 Exam 类和 Test 类
# Exam 类包含 4 个实例属性：id，start_time，end_time，points
# Test 类继承自 Exam 类，不同的是，Test 类不包含起始和终止时间，points 属性永远为 10


class Exam:
    def __init__(self, id, start_time, end_time, points):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.points = points


class Test(Exam):
    def __init__(self, points):
        super().id
        self.points = 10


