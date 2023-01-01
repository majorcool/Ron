import pygame


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, images, position=(40, 147), size=[(44, 47), (59, 47)], **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)

        self.refresh_rate = 5
        self.refresh_counter = 0

        self.speed = 10

    def jump(self):
        pygame.mixer.Sound('resources/audios/jump.wav').play()

    def duck(self):
        pass

    def unduck(self):
        pass

    def die(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def refresh(self):  # load_image
        if self.image == self.images[0]:
            self.image = self.images[1]
        else:
            self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.refresh_counter == self.refresh_rate:
            self.refresh()
            self.refresh_counter = 0
        self.refresh_counter += 1
