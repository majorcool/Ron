class Animal:
    def __init__(self):
        self.health = 100

    def feed_0(self):
        self.health = self.health + 20
        return self.health

    def perform_0(self):
        self.health = self.health - 20
        return self.health


class Manager:
    def __init__(self, performance):
        self.performance = performance

    def __inspect(self, health: Animal):
        if health < 80:
            self.performance -= 20
            if self.performance < 0:
                return self.performance == 0
            else:
                return self.performance

    def feed(self):
        return Animal.feed_0(self)

    def perform(self):
        return Animal.perform_0(self)


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
    keeper_0.feed()
    trainer_0.perform()
    manager_0._Manager__inspect()


everyday()
