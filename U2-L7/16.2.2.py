# 16.2.2  猜数游戏 OOP Version 2
# 1. 在  Version 1 的基础上，修改主程序
#   - 不断进行游戏 game()
#   - 玩家得分小于 -10 时，结束程序
import random


class Dealer:
    def __init__(self):
        self.num = 0
        self.win = False

    def set_number(self):
        self.num_z = random.randint(0, 100)
        return self.num_z

    def hint(self, n):
        if n > self.num_z:
            print("猜大了")
        elif n < self.num_z:
            print("猜小了")
        elif n == self.num_z:
            print("猜对了")
            self.win = True

    def award(self, rounds):
        return 11 - rounds


class Player:
    def __init__(self):
        self.point = 0

    def guess_number(self):
        self.num_p = random.randint(0, 100)
        return self.num_p


def game(dealer, player):
    dealer.win = False
    times = 0
    dealer.set_number()
    print("Dealer", dealer.num_z)
    while not dealer.win:
        dealer.hint(player.guess_number())
        times += 1
        if dealer.award(times) < -10:
            print("玩家得分小于-10，结束游戏")
            return player.point
    print("Player", dealer.award(times))
    return player.point


dealer = Dealer()
player = Player()


while game(dealer, player) < -10:
    pass
# global 变量,设为全局变量




