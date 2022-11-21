# 4.4.2  骗子版  [20pts]
# 1. 添加骗子类 Fraud，包含方法 lie()，随机返回 'lose'，'tie'
# 2. 为 Player 类添加方法 challenge()，随机返回 'yes'，'no'
# 3. 修改 game()：玩家和电脑出拳后，玩家需要询问骗子结果，如果玩家不挑战，则按照骗子的结果进行计分；如果玩家挑战，则按照真实情况计分，但是分值 * 2
# 例1：玩家胜利，骗子告知 'lose'，如果玩家挑战（返回 'yes'），则获得 2 分
# 例2：玩家失败，骗子告知 'lose'，如果玩家挑战，则电脑获得 2 分
# 例3：玩家胜利，骗子告知 'tie'，如果玩家不挑战，则无事发生
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

    def win_2(self):
        self.points += 2

    def challenge(self):
        self.p = ["yes", "no"]
        self.a = random.randint(0, 1)
        return self.p[self.a]


class Computer(Player):
    def win(self):
        self.points += 1

    def win_2(self):
        self.points += 2


class Fraud:
    def __init__(self):
        self.x = ["lose", "tie"]
        self.b = None

    def lie(self):
        self.b = random.randint(0, 1)
        return self.x[self.b]


def game():
    player = Player()
    computer = Computer()
    fraud = Fraud()
    fraud.lie()
    if player.challenge() == "yes":
        if int(player.punch()) > int(computer.punch()):
            print("玩家赢*2")
            return player.win_2()
        elif int(computer.punch()) > int(player.punch()):
            print("电脑赢*2")
            return computer.win_2()
        else:
            print("平局")
    elif player.challenge() == "no":
        if fraud.lie() == "lose":
            print("电脑赢")
            return computer.win()
        else:
            print("玩家赢")
            return player.win()


game()






