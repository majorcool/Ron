# 6. 调用实例方法
# 已知一个可用的数学类 EasyMath，编写主程序，调用所有的实例方法
class EasyMath:
    def __init__(self):
        print(self)

    def easy_add(self, num1, num2):
        print(num1 + num2)

    def easy_minus(self, num1, num2):
        print(num1 - num2)


Math = EasyMath
Math.easy_add(Math,1,2)
Math.easy_minus(Math,2,1)