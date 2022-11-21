# 4.4  猜拳游戏
# 4.4.1  基础版  [20pts]
# 1. 定义玩家类 Player，包含属性 points；方法 punch()，随机返回 '10'，'5'，'2'
# 2. 定义电脑类 Computer，继承自 Player
# 3. 定义函数 game()：玩家和电脑分别出拳（1 次），胜利方得 1 分；打印并返回结果
import random


class Player:
    def __init__(self):
        self.points = 0
        self.p = 0
        self.a = 0

    def punch(self):
        self.p = ["10", "5", "2"]
        self.a = random.randint(0, 2)
        return self.p[self.a]

    def win(self):
        self.points += 1


class Computer(Player):
    def win(self):
        self.points += 1


def game():
    player = Player()
    computer = Computer()
    m = player.punch()
    n = computer.punch()
    if int(m) > int(n):
        print("玩家赢")
        return player.win()
    elif int(n) > int(m):
        print("电脑赢")
        return computer.win()
    else:
        print("平局")


game()
