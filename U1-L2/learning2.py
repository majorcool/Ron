# 定义一个整数变量记录年龄
age = int(input("请输入年龄"))
# 判断年龄是否满18
if age >= 18:
# 如果满18可以进
    print("你已经成年，欢迎进网吧嗨皮")
    print("欢迎欢迎，热烈欢迎")
print("看看什么时候会执行")


age_else = int(input("请输入您的年龄"))
if age_else >= 18:
    print("你已经成年，欢迎来网吧嗨皮")
else:
    print("你还没有成年，请回家写作业吧")
# 这句代码无论条件如何都会执行
print("这句代码什么时候执行")


