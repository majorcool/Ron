class queue:
    def __init__(self):
        self.thing = []

    def push(self, n):  # 入队
        return self.thing.append(n)

    def pop(self):  # 出队
        return self.thing.pop(0)

    def lens(self):  # 个数
        return len(self.thing)

    def empty(self):  # 空不空
        if not self.thing:  # 空
            return False
        else:  # 不空
            return True

    def first(self):  # 队首元素
        return self.thing[0]

    def max(self):  # 最大值
        a = -999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        for num in self.thing:
            if num > a:
                a = num
        return a

    def min(self):  # 最小值
        a = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        for num in self.thing:
            if num < a:
                a = num
        return a
