# 栈的常用操作为：
# 1. 弹栈，通常命名为pop
# 2. 压栈，通常命名为push
# 3. 求栈的大小
# 4. 判断栈是否为空
# 5. 获取栈顶元素的值
class Stack:
    def __init__(self):
        self.thing = []

    def pop(self):  # 弹栈
        return self.thing.pop()

    def push(self, n):  # 压栈
        return self.thing.append(n)

    def lens(self):  # 大小
        return len(self.thing)

    def empty(self):  # 空不空
        if not self.thing:  # 空
            return False
        else:  # 不空
            return True

    def first(self):  # 栈首元素
        return self.thing[0]




