# 16.2.5  猜数游戏 OOP Version 5
# 1. 在 Version 3 的基础上，新建规则类 Rule
#   - 实例属性 rounds，记录游戏回合数
#   - 实例方法 judge()，游戏结束时，根据庄家的奖励，修改玩家的得分
import random
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
            return [0, n-1]
        elif n < self.num_z:
            print("猜小了")
            return [1, n+1]
        elif n == self.num_z:
            print("猜对了")
            self.win = True

    def award(self, rounds):
        return 11 - rounds


class Rule:
    def __init__(self):
        self.rounds = 0
        self.prize = 0
    def judge(self, deealer, player):
        player.point = deealer.award(self.rounds)


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
        choice = dealer.hint(player.guess_number(a, b))
        if dealer.win == True:
            break
        elif choice[0] == 0:
            b = choice[1]
        elif choice[0] == 1:
            a = choice[1]
        times += 1
        if dealer.award(times) < -10:
            print("玩家得分小于-10，结束游戏")
            return dealer.award(times)
    print(dealer.award(times))


game()





