class Animal:
    def __init__(self):
        self.health = 100


class Manager:
    def __init__(self, performance):
        self.performance = performance

    def feed(self, health: Animal):
        self.health += 20
        print("喂")

    def perform(self, health: Animal):
        self.health -= 20
        print("演")

    def __inspect(self, health: Animal):
        if self.health < 80:
            self.performance -= 20
            print("扣")


class Keeper(Manager):
    def __init__(self):
        super().__init__()

    def perform(self):
        pass


class Trainer(Manager):
    def __init__(self):
        super().__init__()

    def feed(self):
        pass


def everyday():
    manager_0 = Manager(100)
    keeper_0 = Keeper()
    trainer_0 = Trainer()
    pig = Animal()
    keeper_0.feed()
    trainer_0.perform()
    manager_0._Manager__inspect


everyday()
