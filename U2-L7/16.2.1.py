# 16.2.1  猜数游戏 OOP Version 1
# 1. 定义庄家类 Dealer
#   - 实例方法 set_number()，返回一个 0-100 的随机整数
#   - 实例方法 hint(n)，根据 n 和设定数字的关系，打印 '猜大了'，'猜小了'，'猜对了'
#   - 实例方法 award(rounds)，根据回合数[1, 2, 3 ..., 20, ...] 返回奖励得分 [10, 9, 8, ..., -9, ...]
# 2. 定义玩家类 Player
#   - 实例属性 point，记录玩家的得分
#   - 实例方法 guess_number()，返回一个 0-100 的随机整数
# 3. 定义函数 game()
#   - 游戏开始时，庄家设定一个随机整数
#   - 每一回合，由玩家猜数，随后庄家进行判定
#   - 玩家猜对时，获取得分，游戏结束
# 4. 编写主程序
#   - 运行 1 次 game()
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


def game():
    dealer = Dealer()
    player = Player()
    times = 0
    dealer.set_number()
    print(dealer.num_z)
    while dealer.win == False:
        dealer.hint(player.guess_number())
        times += 1
    print(dealer.award(times))


game()
