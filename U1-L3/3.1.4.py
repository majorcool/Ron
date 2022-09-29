# 3.1.4 猜数游戏 v2.0
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，最多有 5 次机会
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，显示 “猜大了” 或 “猜小了”

import random
num = random.randint(1,100)
a = 0
c = 0
while c == 0:
    b = int(input("请猜一个数字："))
    if b < num:
        print("猜小了")
    elif b > num:
        print("猜大了")
    elif b == num:
        print("猜对了")
        break
    a += 1
    if a == 5:
        print("你失败了，你没有机会了")
        break
