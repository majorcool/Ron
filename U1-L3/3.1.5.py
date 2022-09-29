# 3.1.5 猜数游戏 v2.1
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，用户可以一直猜，直到猜对为止
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，告知误差范围：如果误差超过 50，打印 '离谱'；误差超过 30，打印 'nonono'；误差不超过 10，打印 'close!'

import random
num = random.randint(1,100)
b = 0
while b == 0:
    a = int(input("请猜一个数字"))
    if a == num:
        print("猜对了")
        break
    elif a > num:
        if a - num > 50:
            print("离谱")
        elif 50 >= a - num > 30:
            print("nonono")
        elif a - num <= 10:
            print("close!")
        else:
            print("?")
    elif a < num:
        if num - a > 50:
            print("离谱")
        elif 50 >= num - a > 30:
            print("nonono")
        elif num - a <= 10:
            print("close!")
        else:
            print("?")