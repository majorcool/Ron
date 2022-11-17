# 16.2.3  猜数游戏 OOP Version 3
# 1. 在  Version 2 的基础上，修改玩家类的实例方法
#   - 添加两个参数 n1、n2，返回 n1-n2 之间的随机整数（包含 n1, n2）
#   - 根据庄家的提示，每次猜数时修改 n1 和 n2，以提高成功率
# 2. 按照 Version 1 修改主程序，只运行一次 game()
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




