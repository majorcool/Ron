# 15.1.2  大鱼吃小鱼 [50pts]
# 假设鱼塘的范围为 (x, y)，0 <= x, y <= 10；游戏开始时，在随机位置生成 1 只大鱼和 10 只小鱼11*11
# 大鱼和小鱼随机上下左右移动，每一次移动，大鱼在横竖方向分别最多移动 1 个单位(横竖各一次)， 小鱼最多移动 1 个单位；当移动到鱼塘边缘时，自动向反方向移动，可以不动
# 大鱼的体力值为 100，每移动 1 个单位，就消耗 1 点体力；小鱼没有体力值；一次移动结束后，如果大鱼和小鱼相遇，大鱼会吃掉小鱼，体力恢复 20（最多恢复到 100）
# 当大鱼体力为 0，或小鱼的数量为 0 时，游戏结束
# 最少两个类。---鱼类：移动|坐标，移动距离---大鱼：体力值---小鱼：数量。
import random


def set_real_coord(o):  # 撞墙返回，直接设置新坐标
    if o > 10:
        return 9
    if o < 0:
        return 1
    return o


class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.speed = 1

    def move(self):
        if random.randint(0, 1) == 0:
            self.x += random.randint(-1, 1)
            self.x = set_real_coord(self.x)
        else:
            self.y += random.randint(-1, 1)
            self.y = set_real_coord(self.y)


class BigFish(Fish):
    def __init__(self):
        super().__init__()
        self.hp = 100

    def move(self):
        self.x = self.x + random.randint(-1, 1)
        self.x = set_real_coord(self.x)
        self.y = self.y + random.randint(-1, 1)
        self.y = set_real_coord(self.y)
        self.hp -= 1

    def eat(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100


class SmallFish(Fish):
    def __init__(self):
        super().__init__()
        self.number = 10


big_fish = BigFish()
small_fishes = list()
eaten_fishes = list()
for n in range(10):
    small_fishes.append(SmallFish())
while big_fish.hp > 0 and small_fishes != []:
    big_fish.move()
    for small_fish in small_fishes:
        small_fish.move()
        if (big_fish.x, big_fish.y) == (small_fish.x, small_fish.y):
            big_fish.eat()
            eaten_fishes.append(small_fish)
        for a in eaten_fishes:
            del a

        if big_fish.hp <= 0:
            print("Big fish died")
            break
        if small_fishes == []:
            print("No small fishes")
            break
