class Animal:
    def __init__(self):
        self.health = 49

    def feed_0(self):
        self.health = self.health + 20
        print("feed")
        return self.health

    def perform_0(self):
        self.health = self.health - 20
        print("perform")
        return self.health


class Manager:
    def __init__(self, performance):
        self.performance = performance

    def inspect(self, n: Animal):
        print(self.__inspect(n))

    def __inspect(self, n: Animal):
        if n.health < 80:
            self.performance -= 20
            print("cut")
            if self.performance < 0:
                return self.performance == 0
            else:
                return self.performance

    def feed(self, n: Animal):
        return Animal.feed_0(n)

    def perform(self, n: Animal):
        return Animal.perform_0(n)


class Keeper(Manager):
    def __init__(self):
        super().__init__(self)

    def perform(self):
        pass


class Trainer(Manager):
    def __init__(self):
        super().__init__(self)

    def feed(self):
        pass


def everyday():
    keeper_0 = Keeper()
    trainer_0 = Trainer()
    manager_0 = Manager(100)
    pig = Animal()
    keeper_0.feed(pig)
    trainer_0.perform(pig)
    manager_0.inspect(pig)


everyday()
