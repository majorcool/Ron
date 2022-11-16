# 16.2.4  猜数游戏 OOP Version 4
# 1. 在  Version 3 的基础上，修改庄家类的实例方法 award()，直接修改玩家的得分
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

    def award(self, rounds, play_not_rise=0):
        if play_not_rise != 0:
            self.q = int(input("修改分数："))
            return self.q
        return 11 - rounds


class Player:
    def __init__(self):
        self.point = 0

    def guess_number(self, a, b):
        self.num_p = random.randint(a, b)
        return self.num_p


def game():
    dealer = Dealer()
    player = Player()
    times = 0
    dealer.set_number()
    print(dealer.num_z)
    a = 0
    b = 100
    while dealer.win == False:
        if times > 0:
            a = int(input("输入范围（起始值）："))
            b = int(input("输入范围（终止值）："))
        dealer.hint(player.guess_number(a, b))
        times += 1
        play_not_rise = int(input("play not rise?import 1 to change points;else import 0:"))
        dealer.award(times, play_not_rise)
        if dealer.award(times) < -10:
            print("玩家得分小于-10，结束游戏")
            return dealer.award(times)
    print(dealer.award(times))


game()





