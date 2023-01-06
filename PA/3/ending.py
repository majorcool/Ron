import pygame


class Ending(pygame.sprite.Sprite):
    def __init__(self, images, position1=(160, 100), position2=(324, 200)):
        pygame.sprite.Sprite.__init__(self)

        self.position1 = position1
        self.position2 = position2
        self.images = images
        self.image_0 = images[0]
        self.image = images[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect0 = self.image_0.get_rect()
        self.rect0.left, self.rect0.bottom = position1
        self.rect1 = self.image.get_rect()
        self.rect1.left, self.rect1.bottom = position2

        self.add = 1
        self.refresh_rate_0 = 0
        self.refresh_rate_1 = 60
        self.refresh_counter = 0

    def refresh(self):
        self.image_0 = self.images[0]
        if self.refresh_counter <= self.refresh_rate_1:
            self.image = self.images[1]
            self.mask = pygame.mask.from_surface(self.image)
        if self.refresh_counter > self.refresh_rate_1:
            if self.image == self.images[1]:
                self.image = self.images[2]
            elif self.image == self.images[2]:
                self.image = self.images[3]
            elif self.image == self.images[3]:
                self.image = self.images[4]
            elif self.image == self.images[4]:
                self.image = self.images[5]
            elif self.image == self.images[5]:
                self.image = self.images[6]
            elif self.image == self.images[6]:
                self.image = self.images[7]
            elif self.image == self.images[7]:
                self.image = self.images[8]
            self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.refresh_counter == self.refresh_rate_0:
            self.refresh()
        if self.refresh_counter < self.refresh_rate_1:
            self.refresh()
        if self.refresh_counter == self.refresh_rate_1:
            self.refresh()
            self.add = 2
        if self.refresh_counter > self.refresh_rate_1:
            self.refresh()
        if self.refresh_counter < self.refresh_rate_1 + self.add:
            self.refresh_counter += self.add

    def draw(self, screen):
        screen.blit(self.image, self.rect1)
        screen.blit(self.image_0, self.rect0)

