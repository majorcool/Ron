# 16.2.5  猜数游戏 OOP Version 5
# 1. 在 Version 3 的基础上，新建规则类 Rule
#   - 实例属性 rounds，记录游戏回合数
#   - 实例方法 judge()，游戏结束时，根据庄家的奖励，修改玩家的得分
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

    def guess_number(self, a, b):
        self.num_p = random.randint(a, b)
        return self.num_p


class Rule:
    def __init__(self):
        self.rounds = 0
        self.prize = 0

    def judge(self):
        self.prize = int(input("庄家奖励分数："))
        return self.prize


def game():
    times = 0
    time = Rule()
    dealer = Dealer()
    player = Player()
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
        time.rounds += 1
        if dealer.award(times) < -10:
            print("玩家得分小于-10，结束游戏")
            return dealer.award(times)
    print(dealer.award(times)+time.judge())


game()









